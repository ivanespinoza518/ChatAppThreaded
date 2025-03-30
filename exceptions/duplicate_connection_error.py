class DuplicateConnectionError(Exception):
    """Custom exception for when a peer disconnects."""
    def __init__(self, username):
        super().__init__(f"Connection failed. Already connected to {username}.")