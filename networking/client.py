import socket

from .network_base import NetworkBase


class Client(NetworkBase):
    def __init__(self, host="localhost", port=12345):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (host, port)
        self.connect_to_server()

    def connect_to_server(self):
        self.client_socket.connect(self.server_address)
        print(f"Połączono z serwerem: {self.server_address}")

    def send_message(self, message):
        self.client_socket.send(message.encode())

    def receive_message(self):
        data = self.client_socket.recv(1024)
        return data.decode()

    def close(self):
        self.client_socket.close()
