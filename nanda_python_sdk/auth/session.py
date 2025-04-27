import time
import httpx
from pydantic import BaseModel
from ..constants import BASE_URL


class Session(BaseModel):
    refresh_token: str
    access_token: str
    expiry_at: int

    def _is_expired(self) -> bool:
        return time.time() > self.expiry_at

    def _set_expiry(self) -> None:
        self.expiry_at = int(time.time()) + 3500

    def _create_header(self) -> dict:
        header = {"Authorization": f"Bearer {self.access_token}"}
        return header

    def _get_tokens(self, email: str, password: str) -> None:
        url = f"{BASE_URL}/auth/token/"
        payload = {
            "email": email,
            "password": password,
        }

        response = httpx.post(url, json=payload)
        response.raise_for_status()

        data = response.json()

        self.refresh_token = data["refresh"]
        self.access_token = data["access"]
        self._set_expiry()

    def _refresh_access_token(self) -> None:
        if not self._is_expired():
            return
        url = f"{BASE_URL}/auth/refresh"
        payload = {"refresh_token": self.refresh_token}
        header = self._create_header()

        response = httpx.post(url, json=payload, headers=header)
        response.raise_for_status()

        data = response.json()

        self.access_token = data["access_token"]
        self._set_expiry()

    def _get_header(self) -> dict:
        self._refresh_access_token()

        return {"Authorization": f"Bearer {self.access_token}"}


session = Session(refresh_token="", access_token="", expiry_at=-1)
