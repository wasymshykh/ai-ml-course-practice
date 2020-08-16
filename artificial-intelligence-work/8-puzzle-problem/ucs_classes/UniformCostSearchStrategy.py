from abstract_classes.SearchStrategy import SearchStrategy
from queue import PriorityQueue


class UniformCostSearchStrategy(SearchStrategy):
    def __init__(self):
        self.queue = PriorityQueue()

    def is_empty(self):
        return self.queue.empty()

    def add_node(self, node):
        cost = node.state.cost
        return self.queue.put((cost, node))

    def remove_node(self):
        return self.queue.get()[1]
