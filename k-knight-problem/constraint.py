from variable import Variable
from assignment import Assignment
from abc import abstractmethod


class Constraint:
    def __init__(self):
        pass

    @abstractmethod
    def is_consistent(self, assignment: Assignment):
        pass

    @abstractmethod
    def scope(self):
        pass
