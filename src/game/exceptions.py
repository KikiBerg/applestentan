# Custom exception handling
class InvalidPlayerAction(Exception):
    """Raised when a player performs an invalid action."""
    pass


class NetworkError(Exception):
    """Raised for network-related issues."""
    pass
