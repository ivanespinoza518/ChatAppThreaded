import socket

from core.address import Address


class SocketFactory:
    @staticmethod
    def create_server_socket(username: str, address: Address) -> socket.socket:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((address.ip, address.port))
        server_socket.listen(5)
        print(f"{username}'s server started on {address}")
        return server_socket

    @staticmethod
    def create_client_socket(address: Address) -> socket.socket:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((address.ip, address.port))
        return client_socket
