from main_classes.PancakeState import PancakeState

class Node:

    def __init__(self, state: PancakeState, parent=None, depth=0, cost=0, action=''):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.cost = cost
        self.action = action

    def __str__(self):
        return "State[" + self.state.string_rep() + "] - Action[" + self.action + "] - Cost[" + str(self.cost) + "]"
