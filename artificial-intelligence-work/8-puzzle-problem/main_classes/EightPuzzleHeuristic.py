from abstract_classes.Heuristic import Heuristic


class EightPuzzleHeuristic(Heuristic):
    def __init__(self, goal):
        self.goal = goal

    def evaluate(self, state):
        heuristic_cost = 0

        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] != self.goal[i][j]:
                    heuristic_cost += 1

        return heuristic_cost
