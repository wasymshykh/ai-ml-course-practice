from abstract_classes.SearchState import SearchState


class EightPuzzleState(SearchState):

    def __init__(self, state, action, cost):
        self.current_state = state
        self.action = action
        self.cost = cost
        self.string = None

    def get_current_state(self):
        return self.current_state

    def get_action(self):
        return self.action

    def get_cost(self):
        return self.cost

    def string_rep(self):
        if self.string is None:
            e = ''
            for i in range(len(self.current_state)):
                for j in range(len(self.current_state[i])):
                    e += str(self.current_state[i][j])
            self.string = e

        return self.string
