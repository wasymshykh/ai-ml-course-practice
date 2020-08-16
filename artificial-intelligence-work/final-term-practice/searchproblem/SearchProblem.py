from abc import abstractmethod
from searchproblem.SearchState import EightPuzzleState, SudokuState
import copy


class SearchProblem:
    @abstractmethod
    def __init__(self, initial_state, goal_state): pass

    @abstractmethod
    def successor(self, current_state): pass

    @abstractmethod
    def initial_state(self): pass

    @abstractmethod
    def is_goal(self, current_state): pass


class EightPuzzleProblem(SearchProblem):
    def __init__(self, initial_state, goal_state):
        super().__init__(initial_state, goal_state)
        self._initial_state = initial_state
        self._goal_state = goal_state

    def initial_state(self):
        return self._initial_state

    def successor(self, current: list):
        # [ [] [] [] ]

        # finding zero
        x, y = -1, -1

        for i in range(0, len(current)):
            for j in range(0, len(current[i])):
                if current[i][j] == 0:
                    x, y = i, j
                    break
            if not x == -1 and y == -1:
                break

        moves = []

        # up
        if x > 0:
            co = copy.deepcopy(current)
            co[x][y] = co[x - 1][y]
            co[x - 1][y] = 0
            n = EightPuzzleState(co, 'UP', 1)
            moves.append(n)

        # down
        if x < len(current) - 1:
            co = copy.deepcopy(current)
            co[x][y] = co[x + 1][y]
            co[x + 1][y] = 0
            n = EightPuzzleState(co, 'DOWN', 1)
            moves.append(n)

        # right
        if y < len(current) - 1:
            co = copy.deepcopy(current)
            co[x][y] = co[x][y + 1]
            co[x][y + 1] = 0
            n = EightPuzzleState(co, 'RIGHT', 1)
            moves.append(n)

        # left
        if y > 0:
            co = copy.deepcopy(current)
            co[x][y] = co[x][y - 1]
            co[x][y - 1] = 0
            n = EightPuzzleState(co, 'LEFT', 1)
            moves.append(n)

        return moves

    def is_goal(self, s_state):
        s_state = s_state.get_current_state()
        for i in range(0, len(self._goal_state)):
            for j in range(0, len(self._goal_state[i])):
                if s_state[i][j] != self._goal_state[i][j]:
                    return False
        return True


class SudokuProblem(SearchProblem):
    def __init__(self, initial_state, goal_state):
        super().__init__(initial_state, goal_state)
        self._initial_state = initial_state
        self._goal_state = goal_state

    def initial_state(self):
        return self._initial_state

    def successor(self, current_state):

        moves = []

        for box_row in range(0, len(current_state)):
            for box in range(0, len(current_state[box_row])):

                for row in range(0, len(current_state[box_row][box])):
                    for col in range(0, len(current_state[box_row][box][row])):

                        for n in range(1, 9):
                            if current_state[box_row][box][row][col] == -1:
                                if self.is_valid(n, box_row, box, row, col, current_state):
                                    cc = copy.deepcopy(current_state)
                                    cc[box_row][box][row][col] = n
                                    moves.append(SudokuState(cc, "placed {} at r[{}] b[{}] {}x{}".format(n, box_row, box, row, col), 1))

        return moves

    def is_valid(self, n, r, b, i, j, c):
        # checking box
        for row in range(0, len(c[r][b])):
            for col in range(0, len(c[r][b][row])):
                if c[r][b][row][col] == n:
                    return False

        # checking whole row
        for box in range(0, len(c[r])):
            for col in range(0, len(c[r][box][i])):
                if c[r][box][i][col] == n:
                    return False

        # checking whole column
        for row in range(0, len(c)):
            for ro in range(0, len(c[row][b])):
                if c[row][b][ro][j] == n:
                    return False

        return True

    def is_goal(self, current_state):
        current_state = current_state.get_current_state()
        for box_row in range(0, len(current_state)):
            for box in range(0, len(current_state[box_row])):

                for r in range(0, len(current_state[box_row][box])):
                    for c in range(0, len(current_state[box_row][box][r])):
                        if self._goal_state[box_row][box][r][c] != current_state[box_row][box][r][c]:
                            return False
        return True
