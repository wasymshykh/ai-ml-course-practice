# from assignment import Assignment
from variable import Variable


class NQueenConstraint:
    def __init__(self, one: Variable, two: Variable, board):
        self._scope = [one, two]
        self._board = board

    def is_consistent(self, assignment):
        value_1 = assignment.get_assignment(self._scope[0])
        value_2 = assignment.get_assignment(self._scope[1])

        # checking unassigned
        if value_1 is None or value_2 is None:
            return False

        # checking same position
        if value_1[0] == value_2[0] and value_1[1] == value_2[1]:
            return False

        # checking from right
        x_r = value_1[0]
        while x_r > -1:
            if x_r == value_2[0] and value_1[1] == value_2[1]:
                return False
            x_r -= 1

        # checking from left
        x_l = value_1[0]
        while x_l < self._board[0]:
            if x_l == value_2[0] and value_1[1] == value_2[1]:
                return False
            x_l += 1

        # checking from bottom
        y_b = value_1[1]
        while y_b > -1:
            if y_b == value_2[1] and value_1[0] == value_2[0]:
                return False
            y_b -= 1

        # checking from top
        y_t = value_1[1]
        while y_t < self._board[1]:
            if y_t == value_2[1] and value_1[0] == value_2[0]:
                return False
            y_t += 1

        # checking diagonal
        # diagonal from top
        d_x = value_1[0]
        d_y = value_1[1]
        while d_x < self._board[0] and d_y < self._board[1]:
            if (d_x == value_2[0] and d_y == value_2[1]):
                return False
            d_x += 1
            d_y += 1

        # diagonal from bottom
        d_x = value_1[0]
        d_y = value_1[1]
        while d_x > -1 and d_y > -1:
            if d_x == value_2[0] and d_y == value_2[1]:
                return False
            d_x -= 1
            d_y -= 1

        d_x = value_1[0]
        d_y = value_1[1]
        while d_x > -1 and d_y < self._board[1]:
            if d_x == value_2[0] and d_y == value_2[1]:
                return False
            d_x -= 1
            d_y += 1

        d_x = value_1[0]
        d_y = value_1[1]
        while d_x < self._board[0] and d_y > -1:
            if d_x == value_2[0] and d_y == value_2[1]:
                return False
            d_x += 1
            d_y -= 1

        return True

    def scope(self):
        return self._scope
