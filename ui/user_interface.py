import socket
import threading

from peer.peer import Peer
from utils.user_input import UserInput


class UserInterface:
    def __init__(self):
        self.host = socket.gethostbyname(socket.gethostname())
        self.port = UserInput.get_available_port()
        self.username = input("Enter your username: ")
        self.peer = Peer(self.username, self.host, self.port)

    def run(self):
        """Start listening for peers and start the user interface"""
        threading.Thread(target=self.peer.start, daemon=True).start()
        self.main_menu()

    def main_menu(self):
        """Display the main menu and prompt the user for actions."""
        self.display_help()
        while True:
            choice = input("\nEnter your choice: ")

            if choice == "1":
                self.display_ip()
            elif choice == "2":
                self.display_port()
            elif choice == "3":
                self.connect_to_peer()
            elif choice == "4":
                self.send_message_to_peer()
            elif choice == "5":
                self.show_connected_peers()
            elif choice == "6":
                self.disconnect_from_peer()
            elif choice == "7":
                self.display_help()
            elif choice == "8":
                print("\nExiting application...")
                break
            else:
                print("Command not recognized. Enter \'7\' for list of recognized commands.")

    def connect_to_peer(self):
        """Prompt user to connect to another peer."""
        peer_ip = input("Enter the IP address of the peer to connect to: ")
        peer_port = int(input("Enter the port of the peer to connect to: "))

        # Connect to the peer
        self.peer.connect_to_peer(peer_ip, peer_port)

    def disconnect_from_peer(self):
        """Prompt user for username of peer to disconnect from"""
        peer_username = input("Enter the username of the peer to disconnect from: ")

        # Disconnect from the peer
        self.peer.disconnect_from_peer(peer_username)

    def send_message_to_peer(self):
        """Prompt user to send a message to a peer."""
        recipient = input("Enter the recipient's username: ")
        message = input("Enter the message: ")

        # Send the message
        self.peer.send_message(message, recipient)

    def show_connected_peers(self):
        """Display the list of connected peers."""
        self.peer.display_peers()

    def display_ip(self) -> None:
        print(f"Your ip: {self.host}")

    def display_port(self) -> None:
        print(f"Your port: {self.port}")

    @staticmethod
    def display_help() -> None:
        print("\nMain Menu:\n"
              "1. Display IP\n"
              "2. Display port\n"
              "3. Connect to another peer\n"
              "4. Send a message\n"
              "5. Show connected peers\n"
              "6. Disconnect from peer\n"
              "7. Display help menu\n"
              "8. Exit\n")