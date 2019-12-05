from nonattackingconstraint import NonAttackingConstraint
from csp import CSP
from variable import Variable

if __name__ == '__main__':

    n = 3
    m = 3
    k = 5

    variables = []

    for knight in range(1, k+1):
        variables.append(Variable("K" + str(knight)))
    # variables = [Variable("K1"), Variable("K2")]

    domains = []
    for i in range(1, n):
        for j in range(1, m):
            domains.append((i, j))

    constraints = []
    for knight in range(0, k-1):
        for i in range(knight + 1, k):
            constraints.append(NonAttackingConstraint(variables[knight], variables[i]))

    csp = CSP(variables, domains, constraints)



