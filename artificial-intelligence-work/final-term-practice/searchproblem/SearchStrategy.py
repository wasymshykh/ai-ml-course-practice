from abc import abstractmethod
from queue import Queue
from searchproblem.Node import Node
from searchproblem.SearchProblem import SearchProblem

class SearchStrategy:
    @abstractmethod
    def __init__(self): pass

    @abstractmethod
    def is_empty(self): pass

    @abstractmethod
    def add_node(self, node): pass

    @abstractmethod
    def remove_node(self): pass


class BFSSearch(SearchStrategy):
    def __init__(self):
        super().__init__()
        self.queue: "Queue[Node]" = Queue()

    def is_empty(self):
        return self.queue.empty()

    def add_node(self, node):
        self.queue.put(node)

    def remove_node(self):
        return self.queue.get()


class Search:
    def __init__(self, problem: SearchProblem, strategy: SearchStrategy):
        self._problem = problem
        self._strategy = strategy

    def solve(self):

        init_node = Node(self._problem.initial_state(), None, 0, 0, 'initial')
        self._strategy.add_node(init_node)

        duplicate = {init_node.state.string_rep(): init_node.state.string_rep()}

        result = None

        while not self._strategy.is_empty():
            current_node = self._strategy.remove_node()

            if self._problem.is_goal(current_node.state):
                result = current_node
                break

            next_moves = self._problem.successor(current_node.state.get_current_state())

            for n_s in next_moves:
                if n_s.string_rep() not in duplicate:
                    new_node = Node(n_s, current_node, current_node.depth+1, current_node.cost+n_s.get_cost(), n_s.get_action())
                    duplicate[new_node.state.string_rep()] = new_node.state.string_rep()
                    self._strategy.add_node(new_node)
        return result

    def get_result(self, result):

        if result.parent_node is None:
            print("Started!")
            return

        self.get_result(result.parent_node)
        print(result)


