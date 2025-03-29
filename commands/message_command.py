from commands.command import Command
from peer.peer import Peer


class MessageCommand(Command):
    def __init__(self, peer: Peer):
        self.peer = peer

    def execute(self):
        """Prompt user to send a message to a peer."""
        recipient = input("Enter the recipient's username: ")
        message = input("Enter the message: ")

        # Send the message
        self.peer.send_message(message, recipient)
