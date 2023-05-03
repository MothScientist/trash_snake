import re


def check_filename(name: str) -> bool:
    pattern = '[\\/:*?"<>|]|CON|PRN|AUX|NUL|COM1'  # Регулярное выражение для недопустимых символов
    if re.search(pattern, name) or len(name) > 255:
        return False
    return True


def check_keywords(name):
    pass
