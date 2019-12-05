from nonattackingconstraint import NonAttackingConstraint
from csp import CSP
from variable import Variable
from backtrackingSearch import BactrackingSearch
from inferenceInfo import InferenceInfo
from simpleInference import SimpleInference
from consoleListener import ConsoleListener

if __name__ == '__main__':

    n = 3
    m = 3
    k = 5

    variables = []

    for knight in range(1, k+1):
        variables.append(Variable("K" + str(knight)))
    # variables = [Variable("K1"), Variable("K2")]

    domains = []
    for i in range(1, n+1):
        for j in range(1, m+1):
            domains.append((i, j))

    constraints = []
    for knight in range(0, k-1):
        for i in range(knight + 1, k):
            constraints.append(NonAttackingConstraint(variables[knight], variables[i]))

    csp = CSP(variables, domains, constraints)

    inPro = SimpleInference()
    bts = BactrackingSearch(inPro, [ConsoleListener()], variableOrdering=True)
    bts.solve(csp)


