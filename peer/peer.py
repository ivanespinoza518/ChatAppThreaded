import socket
import threading

from client.client import Client
from core.address import Address
from core.socket_factory import SocketFactory


class Peer:
    def __init__(self, username: str, address: Address):
        self.username = username
        self.address = Address(address.ip, address.port)
        self.server_socket = SocketFactory.create_server_socket(self.username, self.address)
        self.peers = {}  # Dictionary to track connected peers {username, client)}
        self.lock = threading.Lock()

    def start(self):
        """Listen for incoming connections in the background."""
        threading.Thread(target=self.accept_connections, daemon=True).start()

    def accept_connections(self):
        """Accept incoming connections from other peers."""
        while True:
            client_socket, (ip, port) = self.server_socket.accept()

            # Receive username from client
            username = client_socket.recv(1024).decode()

            # Send username to the client
            client_socket.send(self.username.encode())

            # Add the new peer to the list
            client = Client(client_socket, username, Address(ip, port))
            self.add_peer(username, client)

            threading.Thread(target=self.receive_messages, args=(client,), daemon=True).start()

    def add_peer(self, username: str, client: Client):
        """Add a new peer to the list."""
        with self.lock:
            self.peers[username] = client
            print(f"\nConnected to {username}")

    def connect_to_peer(self, address: Address):
        """Connect to another peer (client side)."""
        try:
            client_socket = SocketFactory.create_client_socket(address)

            # Send username to the connected peer
            client_socket.send(self.username.encode())

            # Receive username of the connected peer
            username = client_socket.recv(1024).decode()

            # Add client to the list
            client = Client(client_socket, username, address)
            self.add_peer(username, client)

            # Start receiving messages in the background
            threading.Thread(target=self.receive_messages, args=(client,), daemon=True).start()

        except Exception as e:
            print(f"Error connecting to peer: {e}")

    def disconnect_from_peer(self, peer_username: str):
        """Terminate connection to peer."""
        with self.lock:
            if peer_username in self.peers:
                client = self.peers[peer_username]
                try:
                    # Notify the peer about disconnection
                    client.socket.send(f"DISCONNECT".encode("utf-8"))

                    # Close the socket
                    client.socket.close()

                except Exception as e:
                    print(f"Error while disconnecting from {peer_username}: {e}")

                # Remove the peer from the local list
                del self.peers[peer_username]
            else:
                print(f"Peer {peer_username} not found.")

    def receive_messages(self, client: Client):
        """Handle receiving messages from the peer."""
        try:
            while True:
                    message = client.socket.recv(1024).decode()
                    if not message:
                        break

                    if message.startswith("DISCONNECT"):
                        print(f"\n{client.username} has disconnected.")
                        with self.lock:
                            if client.username in self.peers:
                                del self.peers[client.username]
                        break

                    print(f"\n{client.username}: {message}")

        except socket.error as e:
            if e.errno in [10053, 10054]:
                with self.lock:
                    if client.username in self.peers:
                        del self.peers[client.username]
                print(f"\nDisconnected from {client.username}.")
            else:
                print(f"\nError receiving message: {e}")

        finally:
            client.socket.close()

    def send_message(self, message: str, peer_username: str):
        """Send a message to a specific peer."""
        client = self.peers.get(peer_username)
        if client:
            client.socket.send(message.encode("utf-8"))
            print(f"Message sent to {peer_username}.")
        else:
            print(f"Recipient {peer_username} not found.")

    def display_peers(self):
        """Display a list of connected peers."""
        print("\nConnected Peers:")
        for _, client in self.peers.items():
            print(f"\t{client}")
