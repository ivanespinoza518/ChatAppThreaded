class SelfConnectionError(Exception):
    """Custom exception for when a user attempts to connect to self."""
    def __init__(self):
        super().__init__(f"Connection failed. Attempted to connect to self.")