# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 17:55:09 2019

@author: umer.chawla
"""
import variable
import copy
import notEqualConstraint
import simpleInference
import time
import backtrackingSearch
import consoleListener

class CSP():
    
    def __init__(self, variables = [], domains = [], constraints = []):
        self._variables = variables
        self._domain = domains
        self._constraints = constraints
        self._domainOfVariable = {}
        self._contraintsOfVariable = {}
        self.setUpVariableDomains()
        self.setUpConstraints()
        
    def setUpVariableDomains(self):
        for var in self._variables:
            self.addVariableDomain(var, self._domain)
        
    def setUpConstraints(self):
        for constraint in self._constraints:
            self.addConstraint(constraint)
            
    def addVariableDomain(self,var,domain):
        self._domainOfVariable[var] = copy.deepcopy(domain)
        
    def addConstraint(self,constraint):
        for var in constraint.getScope():
            if var not in self._contraintsOfVariable:
                self._contraintsOfVariable[var] = []
                self._contraintsOfVariable[var].append(constraint)
                
    def addSingleConstraint(self,constraint):
        self._constraints.append(constraint)
        for var in constraint.getScope():
            if var not in self._contraintsOfVariable:
                self._contraintsOfVariable[var] = []
                self._contraintsOfVariable[var].append(constraint)
                
    def addVariable(self,variable):
        self._variables.append(variable)
        self.addVariableDomain(variable,self._domain)
        
    def getVariables(self):
        return self._variables
    
    def getDomainValues(self,var):
        return self._domainOfVariable[var]

    def getConstraints(self,var):
        if var not in self._contraintsOfVariable:
            return []
        return self._contraintsOfVariable[var]
    
    def getVariableDomains(self):
        return self._domainOfVariable
    
    def setVariableDomains(self,domainOfVariable):
        self._domainOfVariable = domainOfVariable
        
    def copy(self):
        variables = copy.deepcopy(self._variables)
        domains = copy.deepcopy(self._variables)
        constraints = copy.deepcopy(self._variables)
        csp = CSP(variables, domains, constraints)
        return csp
    
    def getNeighbour(self,variable,constraint):
        neigh = []
        for va in constraint.getScope():
            if va != variable and (va not in neigh):
                neigh.append(va)
                return neigh
        
    def removeValueFromDomain(self,variable,value):
        values = []
        for val in self.getDomainValues(variable):
            if val != value:
                values.append(val)
                self._domainOfVariable[variable] = values
                
                
if __name__ == '__main__':
    wa = variable.Variable("WA")
    sa = variable.Variable("SA")
    nt = variable.Variable("NT")
    q = variable.Variable("Q")
    nsw = variable.Variable("NSW")
    v = variable.Variable("V")
    t = variable.Variable("T")

    variables = [wa,sa,nt,q,nsw,v,t]
    domains = ["RED", "GREEN", "BLUE"]
    constraints = [notEqualConstraint.NotEqualConstraint(wa,sa),
                   notEqualConstraint.NotEqualConstraint(wa,nt),
                   notEqualConstraint.NotEqualConstraint(nt,sa),
                   notEqualConstraint.NotEqualConstraint(q,nt),
                   notEqualConstraint.NotEqualConstraint(sa,q),
                   notEqualConstraint.NotEqualConstraint(sa,nsw),
                   notEqualConstraint.NotEqualConstraint(q,nsw),
                   notEqualConstraint.NotEqualConstraint(sa,v),
                   notEqualConstraint.NotEqualConstraint(nsw,v)]
    Csp = CSP(variables,domains,constraints)
    inPro = simpleInference.SimpleInference()
    bts = backtrackingSearch.BactrackingSearch(inPro, [consoleListener.ConsoleListener()], variableOrdering = True)
    start = time.time()
    result = bts.solve(Csp)
    end = time.time()
    print("%.2f ‐ %.2f" % (start,end))

