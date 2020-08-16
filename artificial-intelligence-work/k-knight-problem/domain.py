from variable import Variable
import copy
from typing import List


class Domain:
    def __init__(self, values: List[Variable]):
        self._values = copy.deepcopy(values)

    def get_values(self):
        return self._values
