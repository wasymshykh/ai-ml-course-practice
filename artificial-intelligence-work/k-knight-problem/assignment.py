from variable import Variable
#from nonattackingconstraint import NonAttackingConstraint
from csp import CSP
from typing import List, Set


class Assignment:
    def __init__(self):
        self._variables = []
        self._value_variable = {}

    def add_variable(self, var: Variable, value: Set):
        if var not in self._value_variable:
            self._variables.append(var)
        self._value_variable[var] = value

    def remove_variable(self, var: Variable):
        if var in self._value_variable:
            self._variables.remove(var)
        del self._value_variable[var]

    def get_assignment(self, var: Variable):
        if var not in self._value_variable:
            return 0, 0
        return self._value_variable[var]

    def is_consistent(self, constraints: List):
        for con in constraints:
            if not con.is_consistent(self):
                return False
        return True

    def is_complete(self, variables: List[Variable]):
        for var in variables:
            if not self.has_assignment(var):
                return False
        return True

    def is_solution(self, csp: CSP):
        return self.is_complete(csp.getVariables()) and self.is_consistent(csp.getListOfConstraints())

    def has_assignment(self, var):
        return var in self._value_variable

    def get_variables(self):
        return self._variables

    def __str__(self):
        result = []

        for _ in range(1, 4):
            temp = []
            for _ in range(1, 4):
                temp.append("A")
            result.append(temp)

        for var in self._variables:
            val = self._value_variable[var]
            result[val[0]-1][val[1]-1] = var.get_name()

        toprint = ""
        for i in range(0, len(result)):
            toprint += str(result[i]) + "\n"

        return toprint
