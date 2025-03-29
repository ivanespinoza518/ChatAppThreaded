from commands.command import Command


class ExitCommand(Command):
    """TODO: terminate connection to all remaining peers before exiting"""
    def execute(self):
        print("\nExiting application...")
        exit(0)
