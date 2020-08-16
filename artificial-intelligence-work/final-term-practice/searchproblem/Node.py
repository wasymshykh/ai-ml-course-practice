class Node:
    def __init__(self, state, parent_node, depth, cost, action):
        self.state = state
        self.parent_node = parent_node
        self.depth = depth
        self.cost = cost
        self.action = action

    def __str__(self):
        return "{} -- {} -- {}".format(self.state.string_rep(), self.cost, self.action)

