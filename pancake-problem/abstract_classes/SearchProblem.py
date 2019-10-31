from abc import abstractmethod


class SearchProblem:

    @abstractmethod
    def __init__(self, params):
        pass

    @abstractmethod
    def initial_state(self):
        pass

    @abstractmethod
    def successor_function(self, cur_state):
        pass

    @abstractmethod
    def is_goal(self, cur_state):
        pass

    @abstractmethod
    def __str__(self):
        pass

