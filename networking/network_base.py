from abc import ABC, abstractmethod


class NetworkBase(ABC):
    @abstractmethod
    def send_message(self, message):
        pass

    @abstractmethod
    def receive_message(self):
        pass
