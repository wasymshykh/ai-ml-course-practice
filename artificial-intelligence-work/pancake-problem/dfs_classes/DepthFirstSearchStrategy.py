
from abstract_classes.SearchStrategy import SearchStrategy
from queue import LifoQueue

class DepthFirstSearchStrategy(SearchStrategy):

    def __init__(self):
        self.queue = LifoQueue()

    def is_empty(self):
        return self.queue.empty()

    def add_node(self, node):
        return self.queue.put(node)

    def remove_node(self):
        return self.queue.get()
