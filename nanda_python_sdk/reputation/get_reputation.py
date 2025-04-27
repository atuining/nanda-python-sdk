import httpx
from ..auth import session
from ..constants import BASE_URL
from ..find_server import find_server


def reputation_formula(
    verified: bool, rating: float, uptime: float, usage_count: int
) -> float:
    """A mock formula to calculate reputation based on server characteristic"""
    reputation = 0.0
    if verified:
        reputation += 50
    reputation += rating * 2
    reputation += uptime * 0.2
    reputation += 20 if usage_count > 50 else 10 if usage_count > 0 else 0
    return reputation


def get_reputation(server_name: str) -> float:
    """Get reputation for a server based on an arbitraty formula (for now)

    Args:
        server_name: name of the server
    """
    server_data = find_server(server_name)
    id = server_data["data"]["id"]

    url = f"{BASE_URL}/servers/{id}/ratings/"
    payload = {
        "id": id,
    }
    response = httpx.get(url, params=payload, headers=session._get_header())
    response.raise_for_status()
    data = response.json()["data"]
    reputation = reputation_formula(
        data["verified"],
        data["rating"],
        data["uptime"],
        data["usage_count"],
    )
    return reputation
