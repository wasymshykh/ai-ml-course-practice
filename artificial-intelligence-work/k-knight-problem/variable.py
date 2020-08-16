class Variable:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def __eq__(self, other):
        return self._name == other.get_name

    def __hash__(self):
        return hash(self._name)

    def __str__(self):
        return self._name
