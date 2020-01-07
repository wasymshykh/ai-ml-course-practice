from searchproblem.SearchProblem import SearchProblem, EightPuzzleProblem, SudokuProblem
from searchproblem.SearchState import SearchState, EightPuzzleState, SudokuState
from searchproblem.SearchStrategy import Search, BFSSearch

if __name__ == '__main__':
    '''
    initial_state = [[3, 4, 0], [6, 7, 2], [1, 5, 8]]
    goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    c = EightPuzzleState(initial_state, 1, 'initial')
    epp = EightPuzzleProblem(c, goal_state)

    bfs = BFSSearch()
    search = Search(epp, bfs)
    res = search.solve()
    search.get_result(res)
    '''

    '''
    initial_state = [
                        # row 1
                        [
                            [
                                [-1, -1, 9],
                                [-1, 3, -1],
                                [1, -1, 7]
                            ],
                            [
                                [-1, -1, 8],
                                [-1, 5, -1],
                                [4, -1, 2]
                            ],
                            [
                                [3, 6, -1],
                                [7, 4, -1],
                                [8, -1, 9]
                            ],
                        ],
                        # row 2
                        [
                            [
                                [3, -1, -1],
                                [-1, -1, 5],
                                [6, -1, -1]
                            ],
                            [
                                [8, -1, -1],
                                [-1, -1, -1],
                                [-1, -1, 3]
                            ],
                            [
                                [-1, -1, 5],
                                [9, -1, -1],
                                [-1, -1, 4]
                            ]
                        ],
                        # row 3
                        [
                            [
                                [5, -1, 3],
                                [-1, 7, 4],
                                [-1, 1, 6]
                            ],
                            [
                                [6, -1, 4],
                                [-1, 2, -1],
                                [3, -1, -1]
                            ],
                            [
                                [1, -1, 7],
                                [-1, 3, -1],
                                [4, -1, -1]
                            ]
                        ]
                    ]
    goal_state = [
                    # row 1
                    [
                        [
                            [4, 5, 9],
                            [2, 3, 8],
                            [1, 6, 7]
                        ],
                        [
                            [7, 1, 8],
                            [9, 5, 6],
                            [4, 3, 2]
                        ],
                        [
                            [3, 6, 2],
                            [7, 4, 1],
                            [8, 5, 9]
                        ],
                    ],
                    # row 2
                    [
                        [
                            [3, 9, 1],
                            [7, 4, 5],
                            [6, 8, 2]
                        ],
                        [
                            [8, 4, 7],
                            [2, 6, 1],
                            [5, 9, 3]
                        ],
                        [
                            [6, 2, 5],
                            [9, 8, 3],
                            [1, 7, 4]
                        ]
                    ],
                    # row 3
                    [
                        [
                            [5, 1, 3],
                            [8, 7, 4],
                            [9, 2, 6]
                        ],
                        [
                            [6, 8, 4],
                            [1, 2, 9],
                            [3, 7, 5]
                        ],
                        [
                            [1, 9, 7],
                            [5, 3, 6],
                            [4, 2, 8]
                        ]
                    ]
                ]

    c = SudokuState(initial_state, 1, 'initial')
    sp = SudokuProblem(c, goal_state)
    bfs = BFSSearch()
    search = Search(sp, bfs)
    res = search.solve()
    search.get_result(res)
    '''




