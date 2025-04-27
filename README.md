# Nanda Python SDK

This is a python SDK for working with the NANDA Regsitry API.
More details about NANDA can be found at [NANDA MIT](https://nanda.media.mit.edu/).


Testing this repository requires a deployed MCP server with SSE enabled, instructions for which can found [here](https://github.com/aidecentralized/nanda-servers).

It also required a NANDA registry account, which can be created here: [NANDA registry](https://ui.nanda-registry.com/).

## Implementation Details

Python, pydantic for data validation and httpx for making api requests were used for this project.

## Usage

The SDK is incomplete but is able to do registration and testing while also having a mock system (for now) for reputation.

To test the server you will need a deployed MCP server and its associated URL.

```python
from nanda-python-sdk import authenticate, Server, register_server, ping_server, test_server

# Authenticate into the sdk with the email and password you used on NANDA registry
authenticate("email", "password")

# Use the Server class or import a server.json file
server = Server(name="name", slug="slug", description="description", url="url", types=["tool"], contact_email="email")

# Register the server on the NANDA registry
# Once this is done, you should be able to see it on the link above as well
# Has built in verification of server, will exit if incorrect config
register_server(server)

# Test to see that the server is running
ping_response = ping_server("name of server"")
print(ping_response.status_up)
if not ping_response.status_up:
    print(ping_response.error_message)

get_reputation("url")

```


## Installation and Testing

The only option is to build from source right now. Make sure you have uv installed.

Create an account on [NANDA registry](https://ui.nanda-registry.com/).

```bash
git clone https://github.com/atuining/nanda-python-sdk.git
cd nanda-python-sdk
```

Fill in `test.py` with your MCP server details or edit the `sever.json` file in the root directory.

```bash
uv run test.py
```

## What's next?

A lot of functionality remains to be added to make the SDK more functional and robust. These include

- [ ] Improve error handling
- [ ] Package and publish on PyPI
- [ ] Improve reputation system
- [ ] Increase coverage of the NANDA registry API
- [ ] Allow more ways of testing registered server
- [ ] Add CI
- [ ] Build a CLI
