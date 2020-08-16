from adversarial.TictactoeGame import TictactoeGame

class SimpleMinimax(object):

    def __init__(self, game, listeners=[]):
        self._game = game
        self.listeners = listeners
        self._expandedNodes = 0
        self._duplicateStates = {}

    def minimax_decision(self, state):
        self._duplicateStates[str(state)] = state

        if self._game.terminal_test(state):
            return state._utility

        if state.is_max():
            return self.maxvalue(state)
        else:
            return self.minvalue(state)

    def minvalue(self, state):
        ss = str(state)
        if ss in self._duplicateStates and self._duplicateStates[ss]._utility > state._utility:
            return state._utility
        else:
            self._duplicateStates[str(state)] = state

        self._expandedNodes += 1

        retValue = 1000000000000

        #         player = self._game.getPlayer(state)
        actions = self._game.get_actions(state)

        for action in actions:
            tempValue = self.minimax_decision(self._game.get_result(state, action))
            if tempValue < retValue:
                retValue = tempValue
                state._utility = retValue
                state._action = action

        return retValue

    def maxvalue(self, state):

        ss = str(state)
        if ss in self._duplicateStates and self._duplicateStates[ss].get_utility() > state.get_utility():
            return state._utility
        else:
            self._duplicateStates[str(state)] = state

        self._expandedNodes += 1

        retValue = -1000000000000

        #         player = self._game.getPlayer(state)
        actions = self._game.get_actions(state)

        for action in actions:
            tempValue = self.minimax_decision(self._game.get_result(state, action))
            if tempValue > retValue:
                retValue = tempValue
                state._utility = retValue
                state._action = action

        return retValue



if __name__ == "__main__":

    game = TictactoeGame()
    mm = SimpleMinimax(game)
    initial_state = game.get_initial_state()
    mm.minimax_decision(initial_state)
    print(str(initial_state))
