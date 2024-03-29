import socket
import urllib.request

from interactions.console import Console
from .network_base import NetworkBase


class Server(NetworkBase):
    def __init__(self, host="0.0.0.0", port=12345):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (host, port)
        self.external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
        self.client_socket = None
        self.client_address = None
        self.start_server()

    def start_server(self):
        self.server_socket.bind(self.server_address)
        self.server_socket.listen(1)
        Console.output("Dane tego hosta:")
        Console.output(f'IP: {self.external_ip} Port: {self.server_address[1]}')
        Console.output('Oczekiwanie na połączenie...')
        self.client_socket, self.client_address = self.server_socket.accept()
        Console.output(f'Połączono z klientem: {self.client_address}')

    def receive_message(self):
        data = self.client_socket.recv(1024)
        return data.decode()

    def send_message(self, message):
        self.client_socket.send(message.encode())

    def close(self):
        self.client_socket.close()
        self.server_socket.close()
