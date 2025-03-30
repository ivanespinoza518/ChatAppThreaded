from commands.command import Command
from core.address import Address
from exceptions.duplicate_connection_error import DuplicateConnectionError
from exceptions.self_connection_error import SelfConnectionError
from peer.peer import Peer
from utils.user_input import UserInput


class ConnectCommand(Command):
    def __init__(self, peer: Peer):
        self.peer = peer

    def execute(self):
        """Prompt user to connect to another peer."""
        try:
            peer_ip = UserInput.get_valid_ip()
            peer_port = UserInput.get_valid_port()

            if peer_port == self.peer.address.port:
                raise SelfConnectionError

            for _, client in self.peer.peers.items():
                if peer_ip == client.address.ip and peer_port == client.address.port:
                    raise DuplicateConnectionError(client.username)

            # Connect to the peer
            self.peer.connect_to_peer(Address(peer_ip, peer_port))

        except SelfConnectionError as e:
            print(e)

        except DuplicateConnectionError as e:
            print(e)
