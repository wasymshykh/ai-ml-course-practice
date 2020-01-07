from typing import List, Dict
from csp.Constraint import NonAttacking


class Assignment:
    def __init__(self):
        self._variables: List[str] = []
        self._variable_values: Dict[str, str] = {}

    def add_variable(self, variable, value):
        if variable not in self._variable_values:
            self._variables.append(variable)
        self._variable_values[variable] = value

    def remove_variable(self, variable):
        if variable in self._variable_values:
            self._variables.remove(variable)
            del self._variable_values[variable]

    def get_assignment(self, variable):
        if variable not in self._variable_values:
            return None
        return self._variable_values[variable]

    def is_consistent(self, constraints):
        constraints: List[NonAttacking]

        for c in constraints:
            if not c.is_consistent_with(self):
                return False

        return True

    def has_assignment(self, variable):
        return variable in self._variable_values

    def is_complete(self, variables):
        for v in variables:
            if not self.has_assignment(v):
                return False
        return True

    def is_solution(self, csp):
        return self.is_complete(csp.get_variables()) and self.is_consistent(csp.get_constraints())

    def __str__(self):
        result = []
        for v in self._variable_values:
            result.append("%s = %s" % (v, self._variable_values[v]))
