from nanda_python_sdk import authenticate, Server, register_server, ping_server, get_reputation

def main():
    authenticate("your_email", "your_password")
    print("Hello from nanda-python-sdk!")


if __name__ == "__main__":
    main()
