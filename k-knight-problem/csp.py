import copy


class CSP:
    def __init__(self, variables=[], domains=[], constraints=[]):
        self._variables = variables
        self._domain = domains
        self._constraints = constraints
        self._domainOfVariable = {}
        self._constraintsOfVariable = {}
        self.setUpVariableDomains()
        self.setUpConstraints()

    def setUpVariableDomains(self):
        for var in self._variables:
            self.addVariableDomain(var, self._domain)

    def setUpConstraints(self):
        for constraint in self._constraints:
            self.addConstraint(constraint)

    def addVariableDomain(self, var, domain):
        self._domainOfVariable[var] = copy.deepcopy(domain)

    def addConstraint(self, constraint):
        for var in constraint.scope():
            if var not in self._constraintsOfVariable:
                self._constraintsOfVariable[var] = []
            self._constraintsOfVariable[var].append(constraint)

    def addSingleConstraint(self, constraint):
        self._constraints.append(constraint)

        for var in constraint.getScope():
            if var not in self._constraintsOfVariable:
                self._constraintsOfVariable[var] = []
            self._constraintsOfVariable[var].append(constraint)

    def addVariable(self, variable):
        self._variables.append(variable)
        self.addVariableDomain(variable, self._domain)

    def getVariables(self):
        return self._variables

    def getDomainValues(self, var):
        return self._domainOfVariable[var]

    def getConstraints(self, var):
        if var not in self._constraintsOfVariable:
            return []
        return self._constraintsOfVariable[var]

    def getVariableDomains(self):
        return self._domainOfVariable

    def setVariableDomains(self, domainOfVariable):
        self._domainOfVariable = domainOfVariable

    def copy(self):
        variables = copy.deepcopy(self._variables)
        domains = copy.deepcopy(self._variables)
        constraints = copy.deepcopy(self._variables)
        csp = CSP(variables, domains, constraints)
        return csp

    def getNeighbour(self, variable, constraint):
        neigh = []
        for va in constraint.getScope():
            if va != variable and (va not in neigh):
                neigh.append(va)
        return neigh

    def removeValueFromDomain(self, variable, value):
        values = []
        for val in self.getDomainValues(variable):
            if val != value:
                values.append(val)
        self._domainOfVariable[variable] = values
