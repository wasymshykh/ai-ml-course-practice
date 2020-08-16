class Variable:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def __eq__(self, other):
        other: Variable
        return self._name == other.get_name()