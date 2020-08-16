class TictactoePlayer:
    # @properties -> name, symbol, moves
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.moves = []

    def __str__(self):
        return str("{}_{}".format(self.name, self.symbol))
