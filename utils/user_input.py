import socket


class UserInput:
    @staticmethod
    def get_valid_port():
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
    def get_valid_ip():
        return False

    @staticmethod
    def get_available_port():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(("", 0))  # Bind to an available port
            return s.getsockname()[1]
