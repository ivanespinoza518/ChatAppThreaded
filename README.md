# Peer-to-Peer Threaded Chat Application

## Overview

This project is a Python-based Peer-to-Peer Chat Application that enables direct communication between users without relying on a central server. The application uses sockets and multithreading to manage multiple connections and incorporates the Command Pattern to ensure modular and maintainable code.

## Features

- Direct Peer-to-Peer Communication – Connect with other users by entering their IP and port.

- Multiple Active Connections – Maintain multiple simultaneous peer connections.

- Command Pattern Implementation – Enhances modularity, making it easy to add new commands.

- User-Friendly Terminal Interface – Execute commands such as connecting, sending messages, listing peers, and disconnecting.

- Graceful Disconnection Handling – Ensures peers are properly notified when a user disconnects.

## Technologies Used

- Python – Core language for networking and application logic.

- Sockets – For handling peer-to-peer connections.

- Multithreading – To allow concurrent connections and message handling.

- Design Patterns:

    - Command Pattern – For modular command execution.

    - Factory Pattern – For flexible and reusable socket creation.

## Installation & Usage

### Prerequisites

Python 3.11 installed

### Installation

Clone the Repository:

<pre>git clone https://github.com/ivanespinoza518/ChatAppThreaded.git 
cd ChatAppThreaded</pre>

### Running the Application

1.   Start the application:

<pre>python chat.py</pre>

2.   Enter a username when prompted.

3.   Use the available commands to interact with the chat system.

### Available Commands

| Command | Description |
|:--------------|:--------------|
| help  | Display available commands  |
| ip | Show your assigned IP address   |
| port  | Show your assigned port number   |
| list  | Display all connected peers   |
| connect  | Connect to another peer (requires IP and port)   |
| disconnect  | Disconnect from a specific peer   |
| send  | Send a message to a peer   |
| exit  | Exit the application   |


### Code Structure

<pre>peer-to-peer-chat/
│── peer/                    # Peer connection logic
│   ├── peer.py               # Handles connections and messaging
│   
│── client/                  # Client logic
│   ├── client.py             # Encapsulates client socket and metadata
│
│── core/                    # Core logic
│   ├── address.py            # Encapsulates IP and port information
│   ├── socket_factory.py     # Implements Factory Pattern for socket creation
│
│── commands/                 # Command Pattern implementation
│   ├── command.py            # Abstract command class
│   ├── connect_command.py    # Handles peer connections
│   ├── disconnect_command.py # Handles disconnections
│   ├── message_command.py    # Handles sending messages
│   ├── ...                   # Other command implementations
│
│── ui/                       # User interface logic
│   ├── user_input.py         # Handles user input and available ports
│
│── utils/
│   ├── socket_factory.py     # Implements Factory Pattern for socket creation
│   ├── user_input.py         # Handles user input and available ports
│
│── chat.py                   # Entry point for the application
│── README.md                 # Project documentation</pre>


### Why This Project Matters

- This project demonstrates sone of my software development skills relevant to networking and design patterns:

- Networking & Sockets – Understanding real-world peer-to-peer communication.

- Software Design Patterns – Command Pattern for better scalability and encapsulation.

- Multithreading – Managing concurrent peer connections efficiently.

- Error Handling & Robustness – Handling disconnections and connection failures gracefully.

## Potential Future Enhancements

✅ Implement a GUI version.

✅ Add encryption for secure messaging.

✅ Implement peer discovery for automatic connection.


## Author

Ivan Espinoza

[GitHub](https://github.com/ivanespinoza518) | [LinkedIn](https://www.linkedin.com/in/ivanespinoza7887/)
