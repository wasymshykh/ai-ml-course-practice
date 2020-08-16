from nonattackingconstraint import NonAttackingConstraint
from nqueenconstraint import NQueenConstraint
from csp import CSP
from variable import Variable
from backtrackingSearch import BactrackingSearch
from inferenceInfo import InferenceInfo
from simpleInference import SimpleInference
from consoleListener import ConsoleListener
from forwardCheckingInference import ForwardCheckingInference
import time

if __name__ == '__main__':

    n = 5
    m = 5
    k = 10

    variables = []

    for knight in range(1, k+1):
        variables.append(Variable("K" + str(knight)))
    # variables = [Variable("K1"), Variable("K2")]

    domains = []
    for i in range(1, n+1):
        for j in range(1, m+1):
            domains.append((i, j))

    constraints = []
    for knight in range(0, k):
        for i in range(knight+1, k):
            if knight != i:
                # print("K" + str(knight+1) + " and K" + str(i+1))
                constraints.append(NonAttackingConstraint(variables[knight], variables[i]))

    '''n_q = 5
    m_q = 5
    q = 2
    variables = []
    for queen in range(1, q+1):
        variables.append(Variable("Q" + str(queen)))

    domains = []
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            domains.append((i, j))

    constraints = []
    for queen in range(0, q):
        for i in range(queen+1, q):
            if queen != i:
                constraints.append(NQueenConstraint(variables[queen], variables[i], [n_q,m_q]))
'''

    csp = CSP(variables, domains, constraints)


    inf = SimpleInference()
    # inf = ForwardCheckingInference()
    bts = BactrackingSearch(inf, [ConsoleListener(n, m)])
    start_at = time.time()
    bts.solve(csp)
    print(time.time() - start_at)







