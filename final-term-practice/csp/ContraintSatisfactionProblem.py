import copy


class ConstraintSatisfactionProblem:
    def __init__(self, variables=[], domains=[], constraint=[]):
        self._variables = variables
        self._domains = domains
        self._constraints = constraint
        self._domain_of_var = {}
        self._constraint_of_var = {}
        self.setup_domains()
        self.setup_constraints()

    def setup_domains(self):
        for v in self._variables:
            self._domain_of_var[v] = self._domains

    def add_domain(self, variable, domain):
        self._domain_of_var[variable] = copy.deepcopy(domain)

    def setup_constraints(self):
        for c in self._constraints:
            self.add_constraint(c)

    def add_constraint(self, constraint):
        for v in constraint.get_scope():
            if v not in self._constraint_of_var:
                self._constraint_of_var[v] = []
            self._constraint_of_var[v].append(constraint)

    def add_single_constraint(self, constraint):
        self._constraints.append(constraint)
        for v in constraint.get_scope():
            if v not in self._constraint_of_var:
                self._constraint_of_var[v] = []
            self._constraint_of_var[v].append(constraint)

    def add_variable(self, variable):
        self._variables.append(variable)
        self.add_domain(variable, self._domains)

    def get_variables(self):
        return self._variables

    def get_domain_values(self, variable):
        return self._domain_of_var[variable]

    def get_constraints(self, variable):
        if variable not in self._constraint_of_var:
            return []
        return self._constraint_of_var[variable]

    def get_domains(self):
        return self._domain_of_var

    def set_variable_domains(self, domain_of_var):
        self._domain_of_var = domain_of_var

    def copy(self):
        variables = copy.deepcopy(self._variables)
        domains = copy.deepcopy(self._domains)
        constraints = copy.deepcopy(self._constraints)
        return ConstraintSatisfactionProblem(variables, domains, constraints)

    def get_neighbour(self, variable, constraint):
        n = []
        for v in constraint.get_scope():
            if v != variable and (v not in n):
                n.append(v)
        return n

    def remove_domain_value(self, variable, value):
        values = []
        for d in self._domain_of_var[variable]:
            if d != value:
                values.append(d)
        self._domain_of_var[variable] = values
