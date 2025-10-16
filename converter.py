from typing import Optional


def to_url_style(text: str) -> Optional[str]:
    if not text:
        return text

    text = text.strip()
    text = text.replace("'", '')  # Let's go! -> lets-go

    url_txt = ''
    for ch in text:
        url_txt += ch if ch.isalnum() or ch == '.' else ' '

    count: int = -1
    while count != len(url_txt):
        count = len(url_txt)
        url_txt = url_txt.strip()

        url_txt = url_txt.replace('  ', ' ')
        url_txt = url_txt.replace(' ', '-')
        url_txt = url_txt.replace('--', '-')

    return url_txt.lower().strip()


def strip(text: str) -> Optional[str]:
    if text is None:
        return None

    return text.strip()


def lowercase(text: str) -> Optional[str]:
    if text is None:
        return None

    return text.lower()


def uppercase(text: str) -> Optional[str]:
    if text is None:
        return None

    return text.upper()


def excel_friendly(text: str) -> Optional[str]:
    if text is None:
        return None

    allowed = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'}
    result = ''
    for ch in text:
        if ch in allowed:
            result += ch

    return result


def capitalize_all(text: str) -> Optional[str]:
    if text is None:
        return None

    return ' '.join(w.capitalize() for w in text.split(' '))


def capitalize_first(text: str) -> Optional[str]:
    if text is None:
        return None

    return text.capitalize()


def strip_querystring_from_url(url: str) -> Optional[str]:
    if url is None:
        return None

    if '?' not in url:
        return url

    return url.split('?')[0]
