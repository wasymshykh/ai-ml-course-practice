from abc import abstractmethod


class SearchState:

    @abstractmethod
    def __init__(self, params):
        pass

    @abstractmethod
    def get_current_state(self):
        pass

    @abstractmethod
    def get_action(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def string_rep(self):
        pass

