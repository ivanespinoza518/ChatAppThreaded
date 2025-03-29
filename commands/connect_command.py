from commands.command import Command
from core.address import Address
from peer.peer import Peer


class ConnectCommand(Command):
    def __init__(self, peer: Peer):
        self.peer = peer

    def execute(self):
        """Prompt user to connect to another peer."""
        peer_ip = input("Enter the IP address of the peer to connect to: ")
        peer_port = int(input("Enter the port of the peer to connect to: "))

        # Connect to the peer
        self.peer.connect_to_peer(Address(peer_ip, peer_port))
