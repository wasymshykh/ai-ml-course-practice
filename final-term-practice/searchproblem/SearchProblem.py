from abc import abstractmethod


class SearchProblem:
    @abstractmethod
    def __init__(self, initial_state, goal_state): pass

    @abstractmethod
    def successor(self, current_state): pass

    @abstractmethod
    def initial_state(self): pass

    @abstractmethod
    def is_goal(self, current_state): pass

