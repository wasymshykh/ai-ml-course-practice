from csp.Variable import Variable


class NonAttacking:
    def __init__(self, var_1: Variable, var_2: Variable):
        self._scope = [var_1, var_2]

    def get_scope(self):
        return self._scope

    def is_consistent_with(self, assignment):
        v_1 = assignment.get_assignment(self._scope[0])
        v_2 = assignment.get_assignment(self._scope[1])

        return v_1 is None or v_2 is None or v_1 != v_2

