import ipaddress
import socket


class UserInput:
    @staticmethod
    def get_valid_ip() -> str:
        """Prompt the user for a valid IPv4 address."""
        while True:
            try:
                address = input("Enter IPv4 address: ")
                if ipaddress.ip_address(address):
                    return address
                else:
                    print("IPv4 address not found.")
            except ValueError:
                print(f"Invalid IPv4 address.")

    @staticmethod
    def get_valid_port() -> int:
        """Prompt the user for a valid port number"""
        while True:
            try:
                port = int(input("Enter port number: "))
                if 1024 <= port <= 65535:
                    return port
                else:
                    print("Port must be between 1024 and 65535.")
            except ValueError:
                print("Invalid input. Please enter a number within range.")

    @staticmethod
    def get_available_port() -> int:
        """Get available port number"""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(("", 0))  # Bind to an available port
            return s.getsockname()[1]
