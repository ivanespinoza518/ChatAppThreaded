from commands.command import Command


class ExitCommand(Command):
    def execute(self):
        print("\nExiting application...")
        exit(0)
