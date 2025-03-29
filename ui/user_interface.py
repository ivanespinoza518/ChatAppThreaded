import socket
import threading

from commands.connect_command import ConnectCommand
from commands.disconnect_command import DisconnectCommand
from commands.display_ip_command import DisplayIPCommand
from commands.display_peers_command import DisplayPeersCommand
from commands.display_port_command import DisplayPortCommand
from commands.exit_command import ExitCommand
from commands.help_command import HelpCommand
from commands.message_command import MessageCommand
from core.address import Address
from peer.peer import Peer
from utils.user_input import UserInput


class UserInterface:
    def __init__(self):
        self.address = Address(socket.gethostbyname(socket.gethostname()), UserInput.get_available_port())
        self.username = input("Enter your username: ")
        self.peer = Peer(self.username, self.address)
        self.commands = {
            "help": HelpCommand(),
            "ip": DisplayIPCommand(self.address.ip),
            "port": DisplayPortCommand(self.address.port),
            "list": DisplayPeersCommand(self.peer),
            "connect": ConnectCommand(self.peer),
            "disconnect": DisconnectCommand(self.peer),
            "send": MessageCommand(self.peer),
            "exit": ExitCommand(),
        }

    def run(self):
        """Start listening for peers and start the user interface"""
        threading.Thread(target=self.peer.start, daemon=True).start()
        self.main_menu()

    def main_menu(self):
        """Display the main menu and prompt the user for actions."""
        print("\nEnter a command. Enter 'help' for list of recognized commands.")
        while True:
            command = input("\nEnter a command: ").strip().split()
            if not command:
                continue
            cmd, args = command[0], command[1:]
            if cmd in self.commands:
                self.commands[cmd].execute()
            else:
                print("\nInvalid command. Type 'help' for assistance.")
