from abstract_classes.SearchProblem import SearchProblem
from main_classes.PancakeState import PancakeState
import copy

class PancakeProblem(SearchProblem):
    def __init__(self, initial_state, goal_state):
        self._initial_state = PancakeState(initial_state, None, 0)
        self._goal_state = goal_state

    def initial_state(self):
        return self._initial_state

    def successor_function(self, cur_state: PancakeState):

        '''
            Next flip -> from 1st index till last index (len minus one)
        '''

        next_move = []
        current_state = cur_state.get_current_state()

        for i in range(1, len(current_state)):
            new_state = self.flipping(copy.copy(current_state), i)
            new_action = "Flipping pancake #" + str(i+1) + " [" + str(current_state[i]) + "] bottom"
            next_move.append(PancakeState(new_state, new_action, 1))

        return next_move

    @staticmethod
    def flipping(state, to_index):
        temp = state[0: to_index+1]
        temp = temp[::-1]
        for i in range(len(temp)):
            state[i] = temp[i]
        return state

    def is_goal(self, cur_state):
        for i in range(len(cur_state)):
            if cur_state[i] != self._goal_state[i]:
                return False
        return True

    def __str__(self):
        pass