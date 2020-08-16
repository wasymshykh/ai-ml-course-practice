from main_classes.EightPuzzleProblem import EightPuzzleProblem
from main_classes.EightPuzzleHeuristic import EightPuzzleHeuristic

from queue import PriorityQueue

from bfs_classes.BreadthFirstSearchStrategy import BreadthFirstSearchStrategy
from dfs_classes.DepthFirstSearchStrategy import DepthFirstSearchStrategy
from ucs_classes.UniformCostSearchStrategy import UniformCostSearchStrategy

from greedy_classes.GreedySearchStrategy import GreedySearchStrategy

from a_star_classes.AStarSearchStrategy import AStarSearchStrategy

from main_classes.Search import Search


if __name__ == '__main__':

    goal = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 0]]

    search_problem = EightPuzzleProblem(
        [[3, 1, 0],
         [6, 7, 2],
         [4, 5, 8]], goal)

    # search_strategy = BreadthFirstSearchStrategy()
    # search_strategy = DepthFirstSearchStrategy()
    # search_strategy = UniformCostSearchStrategy()

    # search_strategy = GreedySearchStrategy(EightPuzzleHeuristic(goal))
    search_strategy = AStarSearchStrategy(EightPuzzleHeuristic(goal))

    search = Search(search_problem, search_strategy)
    result = search.solve_problem()

    print("nodes expanded", search.node_expanded)

    if result is not None:
        search.print_result(result)
