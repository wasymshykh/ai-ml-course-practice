from nonattackingconstraint import NonAttackingConstraint
from csp import CSP
from variable import Variable
from backtrackingSearch import BactrackingSearch
from inferenceInfo import InferenceInfo
from simpleInference import SimpleInference
from consoleListener import ConsoleListener
from forwardCheckingInference import ForwardCheckingInference
import time

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
    for knight in range(0, k):
        for i in range(knight+1, k):
            if knight != i:
                # print("K" + str(knight+1) + " and K" + str(i+1))
                constraints.append(NonAttackingConstraint(variables[knight], variables[i]))





    csp = CSP(variables, domains, constraints)


    '''
    inPro = ForwardCheckingInference()
    bts = BactrackingSearch(inPro, [ConsoleListener(n, m)], variableOrdering=True)
    start_at = time.time()
    bts.solve(csp)
    print(time.time() - start_at)
    '''

    ''''''
    #inPro = SimpleInference()
    inPro = ForwardCheckingInference()
    bts = BactrackingSearch(inPro, [ConsoleListener(n, m)], variableOrdering=True, valueOrdering=True)
    start_at = time.time()
    bts.solve(csp)
    print(time.time() - start_at)
    ''''''







