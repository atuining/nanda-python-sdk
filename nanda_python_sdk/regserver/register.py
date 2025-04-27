import json
import sys

import httpx
from pydantic import FilePath, ValidationError

from ..auth import session
from ..constants import BASE_URL
from ..server import Server


def register_server(server: Server | FilePath):
    """Register an MCP server to the NANDA registry

    Args:
        server: can be either a Server object or a json file that follows the correct schema
    """
    cur_server: Server
    if isinstance(server, Server):
        cur_server = server
    else:
        try:
            with open(server, "r") as f:
                file = json.load(f)
                cur_server = Server(**file)
        except ValidationError as e:
            print(f"Error validating your server json file: {e}", file=sys.stderr)
            return
        except Exception as e:
            print(f"Error with your server json file: {e}", file=sys.stderr)
            return

    url = f"{BASE_URL}/servers/"

    print(cur_server.model_dump())

    response = httpx.post(
        url,
        json=cur_server.model_dump(exclude_none=True),
        headers=session._get_header(),
    )

    response.raise_for_status()

    print("successfully registered server to NANDA registry.")
