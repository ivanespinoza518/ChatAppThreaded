from core.address import Address


class Client:
    def __init__(self, socket, username, address: Address):
        self.socket = socket
        self.username = username
        self.address = address

    def __str__(self):
        return f"{self.username}: {self.address}"