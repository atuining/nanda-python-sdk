from pydantic import EmailStr
from .session import session


def authenticate(email: EmailStr, password: str) -> None:
    """Authenticates user to NANDA registry for this session"""
    session._get_tokens(email, password)
    print("successfully authenticated")
