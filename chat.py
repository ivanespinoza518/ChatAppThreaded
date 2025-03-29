import socket
import sys
import threading
import ipaddress


class ChatApp:
    # Initialize by creating a socket for host with
    # host IP, port, a list of connections (initially empty),
    # and a server_socket that will be used to listen for incoming connections
    def __init__(self, port):
        self.host = socket.gethostbyname(socket.gethostname())
        self.port = port
        self.connections = []
        self.server_socket = None
        self.weTerminated = False

    def start(self):
        # Start the server socket to accept incoming connections and initiate the manager()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server listening on {self.host}:{self.port}")

        # Create a thread to handle the incoming connections in the background
        accept_thread = threading.Thread(target=self.accept_connections)
        accept_thread.start()

        # Start the main loop for user interaction
        self.manager()

    # create connect socket to accept incoming connection and opens a thread for each connection
    # to receive messages
    def accept_connections(self):
        while True:
            try:
                # get client socket and client address using server socket's accept method
                connectionSocket, addr = self.server_socket.accept()

                # add the client socket and address to the connections list
                self.connections.append((connectionSocket, addr))

                print(f"Connection established with {addr} by other party")

                recv_thread = threading.Thread(target=self.receive_messages,
                                               args=(connectionSocket,))
                recv_thread.start()
            except:
                break

    # checks for messages from given connection socket
    # if a connection is closed or terminated receive messages will update the connections list
    def receive_messages(self, connectionSocket):
        consIndex = self.connections.index((connectionSocket, connectionSocket.getpeername()))
        conName = connectionSocket.getpeername()
        while True:
            try:
                # update the stored index of this connection (in case others are removed in the meantime)
                consIndex = self.connections.index((connectionSocket, connectionSocket.getpeername()))
                receivedMessage = connectionSocket.recv(1024)
                if not receivedMessage:
                    break
                receivedMessage = receivedMessage.decode()
                print(
                    f"Message received from {connectionSocket.getpeername()[0]} : "
                    f"{connectionSocket.getpeername()[1]}\nMessage: \"{receivedMessage}\"")
            except:
                if not self.weTerminated:
                    print(f"Peer {conName} terminated the connection.")
                else:
                    self.weTerminated = False
                    print(f"Terminated connection to {conName}")
                break
        consIndex = self.connections.index((connectionSocket, conName))
        print(f"Peer list has been updated.")
        self.displayConnections()
        del self.connections[consIndex]

    # Attempt to establish connection with given destination and port
    # Open thread to receive messages along that connection if successful
    def connect(self, destination, port):
        try:
            # Create a new TCP socket object for the client
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Check for duplicate or self connection attempts
            if destination == self.host and port == self.port:
                raise SelfConnectionError
            for c in self.connections:
                if (destination, port) == c[1]:
                    raise DuplicateConnectionError

            # Initiate connection to the specified destination IP and port number
            client_socket.connect((destination, port))

            # Add the new connection to the list of connections
            self.connections.append((client_socket, (destination, port)))
            # Print message to indicate that connection was successful
            print(f"Connected to peer {len(self.connections)} at {destination}:{port}")
            # Start a thread to receive messages from peer
            client_thread = threading.Thread(target=self.receive_messages, args=(client_socket,))
            client_thread.start()
        except SelfConnectionError:
            print(f"Connection failed. Attempted connection to self. Try another port or address.")
        except DuplicateConnectionError:
            print(f"Connection failed. Already connected to {destination}:{port}")
        except:
            print(f"Connection failed. Invalid destination or port")

    # Attempt to send given message to peer identified by connection id
    def send_message(self, connection_id, message):
        # Check for valid connection id
        if 1 <= connection_id <= len(self.connections):
            clientsocket, _ = self.connections[connection_id - 1]
            clientsocket.send(message.encode("utf-8"))
            if not message:
                print(f"Message to {connection_id} is empty.")
            else:
                print(f"Message sent to {connection_id}.")
        else:
            print(
                "Invalid connection ID. Enter a number between the IDs in connection list. "
                "Can use 'list' command to get a list of valid connections.")

    # Menu system to receive user input. Checks for valid formatting for specified command.
    def manager(self) -> None:
        print("Enter a command. Enter 'help' for list of recognized commands.")
        while True:
            inputComponents = input(">> ").split(' ')
            match inputComponents[0]:
                case 'help':
                    self.displayHelp()
                case 'myip':
                    self.displayIp()
                case 'myport':
                    self.displayPort()
                case 'connect':
                    if len(inputComponents) >= 2:
                        try:
                            ipaddress.ip_address(inputComponents[1])
                            if len(inputComponents) >= 3 and inputComponents[2].isnumeric():
                                self.connect(inputComponents[1], int(inputComponents[2]))
                            else:
                                print("Enter a valid port number after the ip address.")
                        except ValueError:
                            print("Invalid ip address. Must provide IPv4 address followed by port #.")
                    else:
                        print(f"Enter an ip address followed by a port number.")
                case 'list':
                    self.displayConnections()
                case 'terminate':
                    if len(inputComponents) >= 2 and inputComponents[1].isnumeric():
                        self.terminate(int(inputComponents[1]) - 1)
                    else:
                        print("Enter a valid id to terminate the connection to.")
                case 'send':
                    if len(inputComponents) >= 2 and inputComponents[1].isnumeric():
                        self.send_message(int(inputComponents[1]), ' '.join(inputComponents[2:]))
                    else:
                        print("Enter a valid id to send a message to, followed by the message.")
                case 'exit':
                    self.terminateAll()
                    break
                case _:
                    print('command not recognized. enter \'help\' for list of recognized commands.')

    # Attempts to close connection specified by the connection index, if within valid range,
    # closes the connection socket.
    def terminate(self, termIndex) -> None:
        if 0 > termIndex or termIndex >= len(self.connections):
            print("Not an id in connections.")
        else:
            self.weTerminated = True
            self.connections[termIndex][0].close()

    # Terminates all open connections, closes our server socket, and exits program.
    def terminateAll(self) -> None:
        while len(self.connections) > 0:
            self.terminate(0)
        self.server_socket.close()
        print("All connections closed.\nServer closed.\nExiting program.")
        sys.exit()

    def displayHelp(self) -> None:
        print('Recognized commands are:\n'
              '\'help\' to display recognized commands\n'
              '\'myip\' to display your IP address\n'
              '\'myport\' to display your receiving port\n'
              '\'connect <destination address> <port no.>\' to open a connection\n'
              '\'list\' to display current connections\n'
              '\'terminate <connection id>\' to close the specified connection\n'
              '\'send <connection id> <message>\' to send a message to the corresponding connection\n'
              '\'exit\' to close all connections and end this process'
              )

    def displayIp(self) -> None:
        print(f"Your ip: {self.host}")

    def displayPort(self) -> None:
        print(f"Your port: {self.port}")

    # Display a numbered list of all connections.
    def displayConnections(self):
        print("id: IP address      Port No.")
        for i, (_, address) in enumerate(self.connections, start=1):
            print(f" {i}: {address[0]:15} {address[1]}")


class SelfConnectionError(Exception):
    "Raised when attempting to connect to your own server socket's ip address and port"
    pass


class DuplicateConnectionError(Exception):
    "Raised when attempting to connect to a socket you have already connected to."
    pass


if __name__ == '__main__':
    # Get the port number from the command-line argument and start the chat application
    port = int(sys.argv[1])
    chat_app = ChatApp(port)
    chat_app.start()
