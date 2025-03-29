from commands.command import Command


class DisplayPortCommand(Command):
    def __init__(self, port):
        self.port = port

    def execute(self):
        print(f"\n\tport={self.port}")
