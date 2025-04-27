import httpx
from pydantic import BaseModel

from ..auth import session
from ..constants import BASE_URL
from ..find_server import find_server


class PingResponse(BaseModel):
    found_url: bool = False
    status_up: bool = False
    server_name: str = "Could not find a server that matched your query"
    error_message: str | None = None


def ping_server(server_name: str | None) -> PingResponse:
    """Get a health verification from NANDA registry for any server

    Args:
        server_name: name of the server, defaults to latest deployed server by user if name not provided
    """
    server_data: dict
    if not server_name:
        url = f"{BASE_URL}/servers/me"
        payload = {
            "limit": 1,
            "page": 1,
        }
        response = httpx.get(url, params=payload, headers=session._get_header())
        response.raise_for_status()
        server_data = response.json()
    else:
        server_data = find_server(server_name)

    if len(server_data) == 0:
        return PingResponse()

    id = server_data["data"]["id"]

    verify_url = f"{BASE_URL}/verification/health-checks/{id}"

    verify_payload = {
        "server_id": id,
        "limit": 1,
        "page": 1,
    }

    verify_response = httpx.get(
        verify_url, params=verify_payload, headers=session._get_header()
    )

    verify_response.raise_for_status()

    verify_data = verify_response.json()

    return PingResponse(
        found_url=True,
        status_up=verify_data["data"]["is_up"],
        server_name=verify_data["data"]["server_name"],
        error_message=verify_data["data"]["error_message"],
    )
