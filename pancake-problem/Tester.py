from main_classes.PancakeProblem import PancakeProblem
from bfs_classes.Search import Search
from bfs_classes.BreadthFirstSearchStrategy import BreadthFirstSearchStrategy

# initial = [1, 3, 2, 4, 5]
# goal = [1, 2, 3, 4, 5]

# initial = [1, 3, 2, 4, 5, 7, 6]
# goal = [1, 2, 3, 4, 5, 6, 7]

initial = [1, 3, 2]
goal = [1, 2, 3]

pp = PancakeProblem(initial, goal)
bfs = BreadthFirstSearchStrategy()
bf_search = Search(pp, bfs)

bfs_result = bf_search.start_bfs()
bf_search.print_result(bfs_result)



