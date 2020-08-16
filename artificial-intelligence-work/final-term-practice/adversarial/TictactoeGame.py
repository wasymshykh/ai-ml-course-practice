from adversarial.TictactoePlayer import TictactoePlayer
from adversarial.TictactoeState import TictactoeState


class TictactoeGame:
    def __init__(self, move=0, rows=3, cols=3):
        self._board = []
        for i in range(0, rows):
            self._board.append([])
            for j in range(0, cols):
                self._board[i].append(0)

        self._move = move

        self._agents = [
            TictactoePlayer("Ali", "X"),
            TictactoePlayer("Waseem", "O")
        ]

        self._winning_positions = [
            [(0, 0), (0, 1), (0, 2)],
             [(1, 0), (1, 1), (1, 2)],
             [(2, 0), (2, 1), (2, 2)],
             [(0, 0), (1, 0), (2, 0)],
             [(0, 1), (1, 1), (2, 1)],
             [(0, 2), (1, 2), (2, 2)],
             [(0, 0), (1, 1), (2, 2)],
             [(2, 0), (1, 1), (0, 2)]
        ]

    # @methods -> get_initial_state, get_player, get_actions, getresult, terminal_test, utility, get_agent_count

    def get_agent_count(self):
        return len(self._agents)

    def terminal_test(self, state):
        return state.get_move() == -1

    def get_initial_state(self):
        return TictactoeState(self._board, self._move)

    def utility(self, state):
        return state.get_utility()

    def get_player(self, state):
        return self._agents[state.get_move()]

    def get_actions(self, state):
        actions = []
        state_board = state.get_board()
        for i in range(0, len(self._board)):
            for j in range(0, len(self._board[i])):
                if state_board[i][j] == 0:
                    actions.append((i, j))
        return actions

    def get_result(self, state, action):
        new_state = state.copy()
        player = self.get_player(state)

        new_state.get_board()[action[0]][action[1]] = player.symbol
        new_state.set_move((new_state.get_move() + 1) % 2)

        win_found = True

        for p in self._winning_positions:
            win_found = True
            for t_p in p:
                if new_state.get_board()[t_p[0]][t_p[1]] != player.symbol:
                    win_found = False
                    break
            if win_found:
                break

        if win_found:
            new_state.set_move(-1)
            if player.symbol == "X":
                new_state.set_utility(1)
            else:
                new_state.set_utility(-1)
        else:
            zero = False
            state_board = state.get_board()
            for i in range(0, len(self._board)):
                for j in range(0, len(self._board[i])):
                    if state_board[i][j] == 0:
                        zero = True
                        break
                if zero:
                    break
            if not zero:
                new_state.set_move(-1)
                new_state.set_utility(0)

        return new_state
