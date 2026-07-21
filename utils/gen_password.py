# utils/gen_password.py

import string
import secrets

def gen_password(length: int, chars: str | None = None) -> str:
    """
    Генерирует криптографический пароль

    Args:
        length (int): Длинна пароля
        chars (str | None): Из чего будет состоять пароль. По умолчанию берется из билиотеки string

    Returns:
        str: Сгенерированный пароль
    """
    chars = chars or string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(secrets.choice(chars) for _ in range(length))

    return password
