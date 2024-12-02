# Network-related functionality for online play
import socket


class NetworkManager:
    """
    Manages client-server communication.
    """
    def __init__(self, ip_address: str, port: int):
        self.connection = socket.create_connection((ip_address, port))

    def send_message(self, message: str):
        """Send a message to the server."""
        self.connection.sendall(message.encode())

    def receive_message(self) -> str:
        """Receive a message from the server."""
        return self.connection.recv(1024).decode()
