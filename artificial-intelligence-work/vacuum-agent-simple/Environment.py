from abc import abstractmethod


class Environment:

    @abstractmethod
    def __init__(self, agent):
        pass

    @abstractmethod
    def execute_step(self, n=1):
        pass

    @abstractmethod
    def execute_all(self):
        pass

    @abstractmethod
    def set_delay(self, delay):
        pass

