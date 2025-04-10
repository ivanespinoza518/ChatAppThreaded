from commands.command import Command


class DisplayIPCommand(Command):
    def __init__(self, ip):
        self.ip = ip

    def execute(self):
        print(f"\n\taddr={self.ip}")
