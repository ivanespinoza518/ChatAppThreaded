from commands.command import Command


class HelpCommand(Command):
    def execute(self):
        print("\nAvailable commands:\n"
              "\thelp - Display information about the available user interface options or command manual.\n"
              "\tip - Display the IP address of this process.\n"
              "\tport - Display the port on which this process is listening for incoming connections.\n"
              "\tlist - Display a numbered list of all the connections.\n"
              "\tconnect - Establish a new TCP connection.\n"
              "\tdisconnect - Terminate the connection listed under the specified number.\n"
              "\tsend - Send a message to the host on the specified connection.\n"
              "\texit - Close all connections and terminate this process.\n")
