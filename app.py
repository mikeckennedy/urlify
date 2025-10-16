from typing import Callable

import pyperclip
import rumps
from colorama import Fore

import converter

VERSION = '2025.4'


class UrlifyApp(rumps.App):
    @rumps.clicked('🌟 URLify Text')
    def urlify_command(self, _):
        successful, message = update_text(converter.to_url_style)
        if successful:
            rumps.notification('urlify 📋', 'Updated clipboard text', message)
        else:
            rumps.notification('urlify 📋', 'Error, count not convert', message)

    @rumps.clicked('🌐 Remove query string')
    def trim_command(self, _):
        successful, message = update_text(converter.strip_querystring_from_url)
        if successful:
            rumps.notification('qs removed 📋', 'Updated clipboard text', message)
        else:
            rumps.notification('qs error 📋', 'Error, count not convert', message)

    @rumps.clicked('↹  Trim Text')
    def trim_command(self, _):
        successful, message = update_text(converter.strip)
        if successful:
            rumps.notification('stripped 📋', 'Updated clipboard text', message)
        else:
            rumps.notification('stripped 📋', 'Error, count not convert', message)

    @rumps.clicked('↧    Lowercase Text')
    def lowercase_command(self, _):
        successful, message = update_text(converter.lowercase)
        if successful:
            rumps.notification('lowercased 📋', 'Updated clipboard text', message)
        else:
            rumps.notification('lowercased 📋', 'Error, count not convert', message)

    @rumps.clicked('↥    Uppercase Text')
    def uppercase_command(self, _):
        successful, message = update_text(converter.uppercase)
        if successful:
            rumps.notification('uppercased 📋', 'Updated clipboard text', message)
        else:
            rumps.notification('uppercased 📋', 'Error, count not convert', message)

    @rumps.clicked('🧾 Excel friendly')
    def excel_command(self, _):
        successful, message = update_text(converter.excel_friendly)
        if successful:
            rumps.notification('Excelified 📋', 'Updated clipboard text', message)
        else:
            rumps.notification('Excelified 📋', 'Error, count not convert', message)

    @rumps.clicked('Aa aa - Capitalize')
    def capitalize_command(self, _):
        successful, message = update_text(converter.capitalize_first)
        if successful:
            rumps.notification('Excelified 📋', 'Updated clipboard text', message)
        else:
            rumps.notification('Excelified 📋', 'Error, count not convert', message)

    @rumps.clicked('Aa Aa - Capitalize All')
    def capitalize_all_command(self, _):
        successful, message = update_text(converter.capitalize_all)
        if successful:
            rumps.notification('Excelified 📋', 'Updated clipboard text', message)
        else:
            rumps.notification('Excelified 📋', 'Error, count not convert', message)

    @rumps.clicked('About URLify')
    def about_command(self, _):
        msg = (
            'URLify is a little application that quickly cleans up text so you can use it in other locations '
            '(e.g. convert a title to a file name).\n\n'
            "It's created by Michael Kennedy and is built with Python 3 and RUMPS. "
            '\n'
            '\n'
            'Updates at https://github.com/mikeckennedy/urlify'
        )
        rumps.alert(message=msg, title=f'URLify v{VERSION}')

    @rumps.clicked('__________________')
    def divider_command(self, _):
        pass


def update_text(action: Callable):
    try:
        text = pyperclip.paste()
        if not text or not text.strip():
            msg = Fore.LIGHTRED_EX + '⚠️ ERROR: No data available in clipboard. 😢'
            print(msg)
            return False, msg

        url_text = action(text)
        msg = (
            Fore.WHITE
            + f"Original '{text}'\n"
            + Fore.LIGHTYELLOW_EX
            + 'Converted text to '
            + Fore.LIGHTGREEN_EX
            + f"'{url_text}' 🌟🌟🌟✨\n"
            + Fore.WHITE
            + 'Copied to clipboard 📋'
        )
        pyperclip.copy(url_text)
        print(msg)
        return True, url_text

    except Exception as x:
        msg = f'⚠️⚠️⚠️⚠️   Error: Unexpected crash: {x}.'
        print(msg)
        return False, msg


if __name__ == '__main__':
    UrlifyApp('📋').run()
