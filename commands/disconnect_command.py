from commands.command import Command
from peer.peer import Peer


class DisconnectCommand(Command):
    def __init__(self, peer: Peer):
        self.peer = peer

    def execute(self):
        """Prompt user for username of peer to disconnect from"""
        peer_username = input("Enter the username of the peer to disconnect from: ")

        # Disconnect from the peer
        self.peer.disconnect_from_peer(peer_username)
