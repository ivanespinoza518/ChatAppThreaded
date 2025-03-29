from commands.command import Command
from peer.peer import Peer


class DisplayPeersCommand(Command):
    def __init__(self, peer: Peer):
        self.peer = peer

    def execute(self):
        """Display the list of connected peers."""
        self.peer.display_peers()
