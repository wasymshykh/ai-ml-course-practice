#from assignment import Assignment
from variable import Variable


class NonAttackingConstraint:
    def __init__(self, one: Variable, two: Variable):
        self._scope = [one, two]

    def is_consistent(self, assignment):
        value_1 = assignment.get_assignment(self._scope[0])
        value_2 = assignment.get_assignment(self._scope[1])

        # checking unassigned
        if value_1 is None or value_2 is None:
            return False

        # checking same position
        if value_1[0] == value_2[0] and value_1[1] == value_2[1]:
            return False

        # checking x+2 y+1
        if value_1[0] + 2 == value_2[0] and value_1[1] + 1 == value_2[1]:
            return False

        # checking x+2 y-1
        if value_1[0] + 2 == value_2[0] and value_1[1] - 1 == value_2[1]:
            return False

        # checking x-2 y+1
        if value_1[0] - 2 == value_2[0] and value_1[1] + 1 == value_2[1]:
            return False

        # checking x-2 y-1
        if value_1[0] - 2 == value_2[0] and value_1[1] - 1 == value_2[1]:
            return False

        # checking x+1 y+2
        if value_1[0] + 1 == value_2[0] and value_1[1] + 2 == value_2[1]:
            return False

        # checking x-1 y+2
        if value_1[0] - 1 == value_2[0] and value_1[1] + 2 == value_2[1]:
            return False

        # checking x+1 y-2
        if value_1[0] + 1 == value_2[0] and value_1[1] - 2 == value_2[1]:
            return False

        # checking x-1 y-2
        if value_1[0] - 1 == value_2[0] and value_1[1] - 2 == value_2[1]:
            return False

        return True

    def scope(self):
        return self._scope
