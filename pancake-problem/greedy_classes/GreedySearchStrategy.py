
from abstract_classes.SearchStrategy import SearchStrategy
from queue import PriorityQueue

class GreedySearchStrategy(SearchStrategy):

    def __init__(self, heuristic):
        self.heuristic = heuristic
        self.queue = PriorityQueue()

    def is_empty(self):
        return self.queue.empty()

    def add_node(self, node):
        return self.queue.put((self.heuristic.evaluate(node.state.current_state), node))

    def remove_node(self):
        return self.queue.get()

