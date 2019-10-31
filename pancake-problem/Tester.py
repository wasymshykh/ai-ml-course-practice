from main_classes.PancakeProblem import PancakeProblem
from bfs_classes.Search import Search as BFS_Search
from bfs_classes.BreadthFirstSearchStrategy import BreadthFirstSearchStrategy
from dfs_classes.Search import Search as DFS_Search
from dfs_classes.DepthFirstSearchStrategy import DepthFirstSearchStrategy


# initial = [1, 3, 2, 4, 5]
# goal = [1, 2, 3, 4, 5]

# initial = [1, 3, 2, 4, 5, 7, 6]
# goal = [1, 2, 3, 4, 5, 6, 7]

initial = [1, 3, 2]
goal = [1, 2, 3]

pp = PancakeProblem(initial, goal)

'''
# BFS
bfs = BreadthFirstSearchStrategy()
bf_search = BFS_Search(pp, bfs)

bfs_result = bf_search.start_bfs()
bf_search.print_result(bfs_result)
'''

# '''
# DFS
dfs = DepthFirstSearchStrategy()
df_search = DFS_Search(pp, dfs)

dfs_result = df_search.start_dfs()
df_search.print_result(dfs_result)
# '''



