from main_classes.PancakeProblem import PancakeProblem

from bfs_classes.Search import Search as BFS_Search
from bfs_classes.BreadthFirstSearchStrategy import BreadthFirstSearchStrategy

from dfs_classes.Search import Search as DFS_Search
from dfs_classes.DepthFirstSearchStrategy import DepthFirstSearchStrategy

from ucs_classes.Search import Search as UCS_Search
from ucs_classes.UniformCostSearchStrategy import UniformCostSearchStrategy

from greedy_classes.Search import Search as Greedy_Search
from greedy_classes.GreedySearchStrategy import GreedySearchStrategy
from greedy_classes.LargestPancakePositionHeuristic import LargestPancakePositionHeuristic

from a_star_classes.Search import Search as AStar_Search
from a_star_classes.AStarSearchStrategy import AStarSearchStrategy
from a_star_classes.PancakePositionHeuristic import PancakePositionHeuristic


# initial = [1, 3, 2, 4, 5]
# goal = [1, 2, 3, 4, 5]

# initial = [1, 3, 2, 4, 5, 7, 6]
# goal = [1, 2, 3, 4, 5, 6, 7]

# initial = [1, 3, 2, 4, 5, 7, 6, 10, 8, 9]
# goal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

initial = [1, 3, 2, 4]
goal = [1, 2, 3, 4]

pp = PancakeProblem(initial, goal)

'''
# BFS
bfs = BreadthFirstSearchStrategy()
bf_search = BFS_Search(pp, bfs)

bfs_result = bf_search.start_bfs()
bf_search.print_result(bfs_result)
'''

'''
# DFS
dfs = DepthFirstSearchStrategy()
df_search = DFS_Search(pp, dfs)

dfs_result = df_search.start_dfs()
df_search.print_result(dfs_result)
'''

'''
# UCS
ucs = UniformCostSearchStrategy()
uc_search = UCS_Search(pp, ucs)

ucs_result = uc_search.start_ucs()
uc_search.print_result(ucs_result)
'''

'''
# Greedy Search
heuristic = LargestPancakePositionHeuristic(goal)
greedy = GreedySearchStrategy(heuristic)
greedy_search = Greedy_Search(pp, greedy)

greedy_result = greedy_search.start_greedy()
greedy_search.print_result(greedy_result)
'''

# '''
# A* Search
heuristic = PancakePositionHeuristic(goal)
a_star = AStarSearchStrategy(heuristic)
a_star_search = AStar_Search(pp, a_star)

a_star_result = a_star_search.start_a_star()
a_star_search.print_result(a_star_result)
# '''



