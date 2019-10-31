from abstract_classes.SearchState import SearchState


class PancakeState(SearchState):

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
        pancake_str = ""
        for i in range(len(self.current_state)):
            pancake_str += str(self.current_state[i])
        self.string = pancake_str
        return self.string

    def draw_state(self):
        pancake_str = ""
        for i in range(len(self.current_state)):
            for _ in range(0, self.current_state[i]):
                pancake_str += "-"
            if i == len(self.current_state) - 1:
                pancake_str += "     =>" + str(self.current_state)
            pancake_str += "\n"
        return pancake_str
