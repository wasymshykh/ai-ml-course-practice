from abc import abstractmethod


class SearchState:
    @abstractmethod
    def __init__(self, current_state, action, cost): pass

    @abstractmethod
    def get_current_state(self): pass

    @abstractmethod
    def get_action(self): pass

    @abstractmethod
    def get_cost(self): pass

    @abstractmethod
    def string_rep(self): pass


class EightPuzzleState(SearchState):
    def __init__(self, current_state, action, cost):
        self._current_state = current_state
        self._action = action
        self._cost = cost

    def get_current_state(self):
        return self._current_state

    def get_action(self):
        return self._action

    def get_cost(self):
        return self._cost

    def string_rep(self):
        # [[] [] []]
        s = ""
        for i in range(0, len(self._current_state)):
            for j in range(0, len(self._current_state[i])):
                s += str(self._current_state[i][j])
        return s


class SudokuState(SearchState):
    def __init__(self, current_state, action, cost):
        self._current_state = current_state
        self._action = action
        self._cost = cost

    def get_current_state(self):
        return self._current_state

    def get_action(self):
        return self._action

    def get_cost(self):
        return self._cost

    def string_rep(self):
        # [[] [] []]
        s = ""
        for i in range(0, len(self._current_state)):
            for j in range(0, len(self._current_state[i])):
                s += str(self._current_state[i][j]) + "\n"
        return s
