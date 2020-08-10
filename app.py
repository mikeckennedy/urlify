import pyperclip
import rumps
from colorama import Fore

from converter import to_url_style


class UrlifyApp(rumps.App):
    @rumps.clicked("🌟 Convert Text")
    def sayhi(self, _):
        successful, message = update_text()
        if successful:
            rumps.notification("urlify 📋", "Updated clipboard text", message)
        else:
            rumps.notification("urlify 📋", "Error, count not convert", message)


def update_text():
    try:
        text = pyperclip.paste()
        if not text or not text.strip():
            msg = Fore.LIGHTRED_EX + "⚠️ ERROR: No data available in clipboard. 😢"
            print(msg)
            return False, msg

        if len(text) > 300:
            msg = Fore.LIGHTRED_EX + f"⚠️ ERROR: The text was really long, too long: {len(text):,}..."
            print(msg)
            return False, msg

        url_text = to_url_style(text)
        msg = (Fore.WHITE + f"Original '{text}'\n" +
               Fore.LIGHTYELLOW_EX + "Converted text to " + Fore.LIGHTGREEN_EX + f"'{url_text}' 🌟🌟🌟✨\n" +
               Fore.WHITE + "Copied to clipboard 📋")
        pyperclip.copy(url_text)
        print(msg)
        return True, msg

    except Exception as x:
        msg = f"⚠️⚠️⚠️⚠️   Error: Unexpected crash: {x}."
        print(msg)
        return False, msg


if __name__ == "__main__":
    UrlifyApp("📋").run()
