import copy


class Domain:
    def __init__(self, values):
        self._values = copy.deepcopy(values)

    def get_values(self):
        return self._values
