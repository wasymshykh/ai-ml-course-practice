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
            return None
        return self._value_variable[var]

    def is_consistent(self, constraints: List[NonAttackingConstraint]):
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

    def __str__(self):
        result = []
        st = ""
        for i in range(1, 5):
            for j in range(1, 5):
                flag = False
                for var in self._variables:
                    if var[0] == i and var[1] == j:
                        st += " K"
                        flag = True
                if not flag:
                    st += " A"
            result.append(st)

        return str(result)
