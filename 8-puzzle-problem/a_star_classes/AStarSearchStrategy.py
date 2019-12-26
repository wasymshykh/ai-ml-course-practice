from abstract_classes.SearchStrategy import SearchStrategy
from queue import PriorityQueue


class AStarSearchStrategy(SearchStrategy):

    def __init__(self, heuristic):
        self.heuristic = heuristic
        self.queue = PriorityQueue()

    def is_empty(self):
        return self.queue.empty()

    def add_node(self, node):
        hu = self.heuristic.evaluate(node.state.current_state)
        return self.queue.put((hu + node.depth, node))

    def remove_node(self):
        return self.queue.get()[1]
