from abstract_classes.Heuristic import Heuristic

class LargestPancakePositionHeuristic(Heuristic):
    def __init__(self, goal):
        self.goal = goal

    def evaluate(self, state):
        heuristic_cost = 0

        for i in range(len(state)):
            if state[i] > self.goal[i]:
                heuristic_cost += 1

        return heuristic_cost
