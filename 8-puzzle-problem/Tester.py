from main_classes.EightPuzzleProblem import EightPuzzleProblem
from bfs_classes.BreadthFirstSearchStrategy import BreadthFirstSearchStrategy
from bfs_classes.Search import Search

search_problem = EightPuzzleProblem(
    [[3, 1, 0],
     [6, 7, 2],
     [4, 5, 8]],

    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 0]]
)

search_strategy = BreadthFirstSearchStrategy()

search = Search(search_problem, search_strategy)
result = search.solve_problem()

if result is not None:
    search.print_result(result)
