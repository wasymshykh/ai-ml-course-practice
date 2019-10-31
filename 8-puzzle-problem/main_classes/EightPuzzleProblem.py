from abstract_classes.SearchProblem import SearchProblem
from main_classes.EightPuzzleState import EightPuzzleState
import copy


class EightPuzzleProblem(SearchProblem):

    def is_goal(self, cur_state: EightPuzzleState):
        current_state = cur_state.get_current_state()
        for i in range(len(current_state)):
            for j in range(len(current_state[i])):
                if current_state[i][j] != self._goal_state[i][j]:
                    return False
        return True

    def __str__(self):
        pass

    def __init__(self, initial_state, goal_state):
        self._initial_state = EightPuzzleState(initial_state, '', 0)
        self._goal_state = goal_state
        self._rows = len(initial_state)
        self._cols = len(initial_state[0])

    def initial_state(self):
        return self._initial_state

    def successor_function(self, cur_state: EightPuzzleState):

        next_moves = []
        empty_row, empty_col = 0, 0
        current_state = cur_state.get_current_state()

        empty_found = False
        for i in range(len(current_state)):
            for j in range(len(current_state[i])):
                if current_state[i][j] == 0:
                    empty_row, empty_col = i, j
                    empty_found = True
                    break
            if empty_found:
                break

        # Up move?
        if empty_row != 0:
            new_state = copy.deepcopy(current_state)
            temp = new_state[empty_row - 1][empty_col]
            new_state[empty_row - 1][empty_col] = new_state[empty_row][empty_col]
            new_state[empty_row][empty_col] = temp
            next_move_state = EightPuzzleState(new_state, 'Move Up', 1)
            next_moves.append(next_move_state)

        # Down move?
        if empty_row + 1 != self._rows:
            new_state = copy.deepcopy(current_state)
            temp = new_state[empty_row + 1][empty_col]
            new_state[empty_row + 1][empty_col] = new_state[empty_row][empty_col]
            new_state[empty_row][empty_col] = temp
            next_move_state = EightPuzzleState(new_state, 'Move Down', 1)
            next_moves.append(next_move_state)

        # Left move?
        if empty_col != 0:
            new_state = copy.deepcopy(current_state)
            temp = new_state[empty_row][empty_col - 1]
            new_state[empty_row][empty_col - 1] = new_state[empty_row][empty_col]
            new_state[empty_row][empty_col] = temp
            next_move_state = EightPuzzleState(new_state, 'Move Left', 1)
            next_moves.append(next_move_state)

        # Right move?
        if empty_col + 1 != self._cols:
            new_state = copy.deepcopy(current_state)
            temp = new_state[empty_row][empty_col + 1]
            new_state[empty_row][empty_col + 1] = new_state[empty_row][empty_col]
            new_state[empty_row][empty_col] = temp
            next_move_state = EightPuzzleState(new_state, 'Move Right', 1)
            next_moves.append(next_move_state)

        return next_moves

