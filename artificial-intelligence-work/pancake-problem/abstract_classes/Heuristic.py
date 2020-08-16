from abc import abstractmethod


class Heuristic:
    @abstractmethod
    def __init__(self, goal):
        pass

    @abstractmethod
    def evaluate(self, state):
        pass

