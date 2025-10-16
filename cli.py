#!/usr/bin/env python3
"""
URLify CLI - Command line version of the URLify text conversion tool.

This CLI mirrors the functionality of the GUI app, allowing you to convert text
using various transformation functions. Text can be provided via stdin, clipboard,
or as arguments, and output can go to stdout or clipboard.
"""

import argparse
import sys
from typing import Callable, Optional

import pyperclip
from colorama import Fore, Style
from colorama import init as colorama_init

import converter

VERSION = '2025.4'

# Initialize colorama for cross-platform colored output
colorama_init(autoreset=True)


class ColoredHelpFormatter(argparse.RawDescriptionHelpFormatter):
    """Custom help formatter that adds colors to help output."""

    def _format_usage(self, usage, actions, groups, prefix):
        if prefix is None:
            prefix = f'{Fore.CYAN}usage: {Style.RESET_ALL}'
        return super()._format_usage(usage, actions, groups, prefix)

    def format_help(self):
        help_text = super().format_help()

        # Color different sections
        help_text = help_text.replace(
            'positional arguments:',
            f'{Fore.GREEN}positional arguments:{Style.RESET_ALL}',
        )
        help_text = help_text.replace('options:', f'{Fore.GREEN}options:{Style.RESET_ALL}')
        help_text = help_text.replace('Input options:', f'{Fore.GREEN}Input options:{Style.RESET_ALL}')
        help_text = help_text.replace('Output options:', f'{Fore.GREEN}Output options:{Style.RESET_ALL}')

        # Color command names in the command list
        lines = help_text.split('\n')
        colored_lines = []
        in_command_section = False

        for line in lines:
            if 'positional arguments:' in line:
                in_command_section = True
                colored_lines.append(line)
            elif line.strip() and not line.startswith('  ') and in_command_section:
                in_command_section = False
                colored_lines.append(line)
            elif in_command_section and line.strip() and line.startswith('    '):
                # This is a command description line
                parts = line.split(None, 1)
                if len(parts) >= 2:
                    command = parts[0]
                    description = parts[1] if len(parts) > 1 else ''
                    colored_line = f'    {Fore.YELLOW}{command}{Style.RESET_ALL} {description}'
                    colored_lines.append(colored_line)
                else:
                    colored_lines.append(line)
            else:
                colored_lines.append(line)

        help_text = '\n'.join(colored_lines)

        # Color examples section
        help_text = help_text.replace('Examples:', f'{Fore.CYAN}Examples:{Style.RESET_ALL}')

        # Color input sources section
        help_text = help_text.replace(
            'Input sources (in order of priority):',
            f'{Fore.CYAN}Input sources (in order of priority):{Style.RESET_ALL}',
        )

        # Color default command section
        help_text = help_text.replace('Default command:', f'{Fore.CYAN}Default command:{Style.RESET_ALL}')

        return help_text


class ColoredArgumentParser(argparse.ArgumentParser):
    """Custom ArgumentParser that uses colored help formatter."""

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('formatter_class', ColoredHelpFormatter)
        super().__init__(*args, **kwargs)


def get_input_text(args) -> Optional[str]:
    """Get input text from various sources based on command line arguments."""
    if args.text:
        # Text provided as argument
        return ' '.join(args.text)
    elif not sys.stdin.isatty():
        # Text from stdin (piped input)
        return sys.stdin.read().strip()
    else:
        # Text from clipboard (default)
        try:
            text = pyperclip.paste()
            if not text or not text.strip():
                print(f'{Fore.LIGHTRED_EX}⚠️ ERROR: No data available in clipboard. 😢')
                return None
            return text
        except Exception as e:
            print(f'{Fore.LIGHTRED_EX}⚠️ ERROR: Could not access clipboard: {e}')
            return None


def output_result(result: str, original: str, operation: str, args) -> None:
    """Output the result to stdout and/or clipboard based on arguments."""
    if args.quiet:
        # Quiet mode: just output the result
        print(result)
    else:
        # Verbose mode: show transformation details
        print(f"{Fore.WHITE}Original: '{original}'")
        print(f'{Fore.LIGHTYELLOW_EX}Operation: {operation}')
        print(f"{Fore.LIGHTGREEN_EX}Result: '{result}' 🌟✨")

        if args.copy_to_clipboard:
            print(f'{Fore.WHITE}Copied to clipboard 📋')

    # Copy to clipboard if requested
    if args.copy_to_clipboard:
        try:
            pyperclip.copy(result)
        except Exception as e:
            print(f'{Fore.LIGHTRED_EX}⚠️ WARNING: Could not copy to clipboard: {e}')


def execute_conversion(converter_func: Callable, operation_name: str, args) -> None:
    """Execute a conversion function with error handling."""
    try:
        text = get_input_text(args)
        if text is None:
            print(f'{Fore.LIGHTRED_EX}⚠️ ERROR: No input text provided.')
            print("Provide text via: --text 'your text', stdin pipe, or clipboard")
            sys.exit(1)

        result = converter_func(text)
        if result is None:
            print(f'{Fore.LIGHTRED_EX}⚠️ ERROR: Conversion failed')
            sys.exit(1)

        output_result(result, text, operation_name, args)

    except Exception as e:
        print(f'{Fore.LIGHTRED_EX}⚠️⚠️⚠️⚠️ Error: Unexpected crash: {e}')
        sys.exit(1)


def add_common_arguments(parser):
    """Add common arguments to a parser."""
    # Input options
    input_group = parser.add_argument_group('Input options')
    input_group.add_argument(
        '--text',
        '-t',
        nargs='+',
        help='Text to convert (multiple words will be joined with spaces)',
    )
    input_group.add_argument(
        '--clipboard',
        '-c',
        action='store_true',
        help='Read from clipboard (this is the default)',
    )

    # Output options
    output_group = parser.add_argument_group('Output options')
    output_group.add_argument(
        '--no-clipboard',
        dest='copy_to_clipboard',
        action='store_false',
        help="Don't copy result to clipboard (by default, result is copied)",
    )
    output_group.add_argument(
        '--quiet',
        '-q',
        action='store_true',
        help='Quiet mode: only output the converted text',
    )


def create_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
    parser = ColoredArgumentParser(
        description=f'{Fore.CYAN}URLify CLI{Style.RESET_ALL} - Convert and transform text using various methods',
        epilog=f"""
Examples:
  {Fore.LIGHTGREEN_EX}%(prog)s --text "Hello World!"{Style.RESET_ALL}                          # urlify (default) with text input
  {Fore.LIGHTGREEN_EX}%(prog)s{Style.RESET_ALL}                                                # urlify (default) with clipboard input (default)
  {Fore.LIGHTGREEN_EX}%(prog)s lowercase --text "HELLO WORLD"{Style.RESET_ALL}                 # lowercase with text input
  {Fore.LIGHTGREEN_EX}echo "SOME TEXT" | %(prog)s uppercase{Style.RESET_ALL}                   # uppercase with stdin input
  {Fore.LIGHTGREEN_EX}%(prog)s trim --text "  spaced text  " --no-clipboard{Style.RESET_ALL}
  {Fore.LIGHTGREEN_EX}%(prog)s remove-query --text "https://example.com?param=value"{Style.RESET_ALL}
  
Input sources (in order of priority):
  {Fore.YELLOW}1.{Style.RESET_ALL} --text argument
  {Fore.YELLOW}2.{Style.RESET_ALL} stdin (piped input)
  {Fore.YELLOW}3.{Style.RESET_ALL} clipboard (default)
  
Default command: {Fore.LIGHTYELLOW_EX}urlify{Style.RESET_ALL} (if no command specified)
        """,
    )

    parser.add_argument('--version', action='version', version=f'URLify CLI v{VERSION}')

    # Subcommands for each conversion type
    subparsers = parser.add_subparsers(
        dest='command',
        help='Available conversion commands (default: urlify)',
        metavar='[COMMAND]',
    )

    # URLify command
    urlify_parser = subparsers.add_parser(
        'urlify',
        help='Convert text to URL-friendly format (lowercase, replace spaces with hyphens)',
    )
    add_common_arguments(urlify_parser)

    # Remove query string command
    remove_query_parser = subparsers.add_parser('remove-query', aliases=['rq'], help='Remove query string from URL')
    add_common_arguments(remove_query_parser)

    # Trim command
    trim_parser = subparsers.add_parser('trim', help='Remove leading and trailing whitespace')
    add_common_arguments(trim_parser)

    # Lowercase command
    lower_parser = subparsers.add_parser('lowercase', aliases=['lower', 'lc'], help='Convert text to lowercase')
    add_common_arguments(lower_parser)

    # Uppercase command
    upper_parser = subparsers.add_parser('uppercase', aliases=['upper', 'uc'], help='Convert text to uppercase')
    add_common_arguments(upper_parser)

    # Excel friendly command
    excel_parser = subparsers.add_parser(
        'excel-friendly',
        aliases=['excel'],
        help='Extract only numbers and dots (Excel-friendly format)',
    )
    add_common_arguments(excel_parser)

    # Capitalize first command
    cap_first_parser = subparsers.add_parser(
        'capitalize-first',
        aliases=['cap-first', 'cf'],
        help='Capitalize the first letter of text',
    )
    add_common_arguments(cap_first_parser)

    # Capitalize all command
    cap_all_parser = subparsers.add_parser(
        'capitalize-all',
        aliases=['cap-all', 'ca'],
        help='Capitalize the first letter of each word',
    )
    add_common_arguments(cap_all_parser)

    return parser


def main():
    """Main CLI entry point."""
    # Check if no command provided and add default
    commands = [
        'urlify',
        'remove-query',
        'rq',
        'trim',
        'lowercase',
        'lower',
        'lc',
        'uppercase',
        'upper',
        'uc',
        'excel-friendly',
        'excel',
        'capitalize-first',
        'cap-first',
        'cf',
        'capitalize-all',
        'cap-all',
        'ca',
    ]

    # Check for global options that don't need a command
    global_only_args = {'--help', '-h', '--version'}
    has_global_only = any(arg in global_only_args for arg in sys.argv[1:])

    if len(sys.argv) == 1:
        # No arguments at all, use default command with clipboard
        sys.argv.append('urlify')
    elif not has_global_only and not any(arg in commands for arg in sys.argv[1:]):
        # Arguments provided but no command and no global-only args
        # Insert urlify at the beginning of arguments (after script name)
        sys.argv.insert(1, 'urlify')

    parser = create_parser()
    args = parser.parse_args()

    # Map commands to converter functions and descriptions
    command_map = {
        'urlify': (converter.to_url_style, 'URLify'),
        'remove-query': (converter.strip_querystring_from_url, 'Remove query string'),
        'rq': (converter.strip_querystring_from_url, 'Remove query string'),
        'trim': (converter.strip, 'Trim whitespace'),
        'lowercase': (converter.lowercase, 'Lowercase'),
        'lower': (converter.lowercase, 'Lowercase'),
        'lc': (converter.lowercase, 'Lowercase'),
        'uppercase': (converter.uppercase, 'Uppercase'),
        'upper': (converter.uppercase, 'Uppercase'),
        'uc': (converter.uppercase, 'Uppercase'),
        'excel-friendly': (converter.excel_friendly, 'Excel-friendly'),
        'excel': (converter.excel_friendly, 'Excel-friendly'),
        'capitalize-first': (converter.capitalize_first, 'Capitalize first'),
        'cap-first': (converter.capitalize_first, 'Capitalize first'),
        'cf': (converter.capitalize_first, 'Capitalize first'),
        'capitalize-all': (converter.capitalize_all, 'Capitalize all'),
        'cap-all': (converter.capitalize_all, 'Capitalize all'),
        'ca': (converter.capitalize_all, 'Capitalize all'),
    }

    if args.command in command_map:
        converter_func, operation_name = command_map[args.command]
        execute_conversion(converter_func, operation_name, args)
    else:
        print(f'{Fore.LIGHTRED_EX}⚠️ ERROR: Unknown command: {args.command}')
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
