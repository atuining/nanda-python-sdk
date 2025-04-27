import httpx
from .constants import BASE_URL
from .auth import session


def find_server(server_name: str) -> dict:
    url = f"{BASE_URL}/discovery/search/"

    payload = {
        "q": server_name,
        "limit": 1,
        "page": 1,
    }

    response = httpx.get(url, params=payload, headers=session._get_header())
    response.raise_for_status()
    return response.json()
