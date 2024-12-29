import secrets
import socket
import string
from datetime import datetime


def get_random_key(length=32):
    characters = string.ascii_letters + string.digits
    return "".join(secrets.choice(characters) for _ in range(length))


def get_ipv4_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ipV4 = s.getsockname()[0]
    s.close()
    return ipV4


def get_time_now(format: str = "%H:%M:%S") -> str:
    result = datetime.now().time().strftime(format)
    return result
