from main_classes.PancakeProblem import PancakeProblem
from greedy_classes.Node import Node
from greedy_classes.GreedySearchStrategy import GreedySearchStrategy


class Search:
    search_problem: PancakeProblem
    search_strategy: GreedySearchStrategy

    def __init__(self, search_problem, search_strategy):
        self.search_problem = search_problem
        self.search_strategy = search_strategy
        self.explored = 0

    def start_greedy(self):

        node = Node(self.search_problem.initial_state(), None, 0, 0, '')
        self.search_strategy.add_node(node)

        duplicate_map = {node.state.string_rep(): node.state.string_rep()}

        result = None

        while not self.search_strategy.is_empty():
            current_node = self.search_strategy.remove_node()[1]

            if self.search_problem.is_goal(current_node.state.get_current_state()):
                result = current_node
                break
            else:
                self.explored += 1

            next_moves = self.search_problem.successor_function(current_node.state)

            for next_state in next_moves:
                if next_state.string_rep() not in duplicate_map:
                    new_node = Node(next_state, current_node, current_node.depth + 1,
                                    current_node.cost + next_state.cost, next_state.action)

                    self.search_strategy.add_node(new_node)

                    duplicate_map[new_node.state.string_rep()] = new_node.state.string_rep()

        return result

    def print_result(self, result: Node):
        if result.parent is None:
            print("Nodes Explored " + str(self.explored))
            print("Initial State: %s" % result.state.get_current_state())
            return
        self.print_result(result.parent)
        print("Perform: action[%s] - new state[%s] - cost[%d]" % (
            result.action, result.state.get_current_state(), result.cost))
