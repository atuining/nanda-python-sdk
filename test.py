from nanda_python_sdk import authenticate, register_server, Server


def main():
    authenticate("email", "password")
    server = Server(
        name="name of server",
        slug="slug",
        description="description",
        provider="provider",
        url="url",
        types=["tool"],
        contact_email="email",
    )
    register_server(server)


if __name__ == "__main__":
    main()
