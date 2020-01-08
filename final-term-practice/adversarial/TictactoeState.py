from copy import deepcopy


class TictactoeState:
    # @properties -> board, move, utility, action

    def __init__(self, board, move, utility = 0):
        self._board = board
        self._move = move
        self._utility = utility
        self._action = None

    # @methods -> copy, is_max, is_next_agent_max, get_action, str

    def copy(self):
        return TictactoeState(deepcopy(self._board), self._move, self._utility)

    def is_max(self):
        return self._move == 0

    def is_next_agent_max(self):
        return (self._move + 1) % 2 == 0

    def get_move(self):
        return self._move

    def set_move(self, move):
        self._move = move

    def get_utility(self):
        return self._utility

    def set_utility(self, utility):
        self._utility = utility

    def get_action(self):
        return self._action

    def str(self):
        return "{}_{}".format(str(self._board), self._move)

