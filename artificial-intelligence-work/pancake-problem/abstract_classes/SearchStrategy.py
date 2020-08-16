from abc import abstractmethod


class SearchStrategy:

    @abstractmethod
    def __init__(self, params):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def add_node(self, node):
        pass

    @abstractmethod
    def remove_node(self):
        pass

