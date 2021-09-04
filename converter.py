def to_url_style(text):
    if not text:
        return text

    text = text.strip()
    url_txt = ''
    for ch in text:
        url_txt += ch if ch.isalnum() or ch == '.' else ' '

    count = -1
    while count != len(url_txt):
        count = len(url_txt)
        url_txt = url_txt.strip()
        url_txt = url_txt.replace('  ', ' ')
        url_txt = url_txt.replace(' ', '-')
        url_txt = url_txt.replace('--', '-')

    return url_txt.lower().strip()


def strip(text: str):
    if text is None:
        return None

    return text.strip()


def lowercase(text: str):
    if text is None:
        return None

    return text.lower()


def uppercase(text: str):
    if text is None:
        return None

    return text.upper()


def excel_friendly(text: str):
    if text is None:
        return None

    allowed = {'0', '1', '2', '3', '4', '4', '6', '7', '8', '9', '.'}
    result = ''
    for ch in text:
        if ch in allowed:
            result += ch

    return result
