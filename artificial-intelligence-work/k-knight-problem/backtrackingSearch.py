'''
Created on Mar 6, 2019

@author: dr.aarij
'''
from searchStrategy import SearchStrategy
from assignment import Assignment
from inferenceInfo import InferenceInfo
import math

class BactrackingSearch(SearchStrategy):
    '''
    classdocs
    '''


    def __init__(self, inferenceProcdeure,listeners = [],variableOrdering=False,valueOrdering=False):
        '''
        Constructor
        '''
        SearchStrategy.__init__(self, listeners)
        self._inferenceProcedure = inferenceProcdeure
        self._variableOrdering = variableOrdering
        self._valueOrdering = valueOrdering
    
    def solve(self, csp):
        return self.recursiveBacktrackingSearch(csp, Assignment())
    
    def recursiveBacktrackingSearch(self, csp, assignment):
        if assignment.is_complete(csp.getVariables()):
            return assignment
        var = self.selectUnAssignedVariable(csp, assignment)
        
        for value in self.orderDomainValues(csp, var):
            assignment.add_variable(var, value)
            self.fireListeners(csp, assignment)
            if assignment.is_consistent(csp.getConstraints(var)):
                inference = InferenceInfo(csp, var, value, self._inferenceProcedure)
                inference.doInference(csp, var, value)
                if not inference.isFailure(csp, var, value):
                    inference.setInferencesToAssignments(assignment,csp)
                    result = self.recursiveBacktrackingSearch(csp,assignment)
                    if result is not None:
                        return result
                    inference.restoreDomains(csp)
            assignment.remove_variable(var)
        return None
    
    def selectUnAssignedVariable(self,csp,assignment):
        
        if not self._variableOrdering:
            for var in csp.getVariables():
                if not assignment.has_assignment(var):
                    return var
        else:
            minimum = math.inf
            resVar = None
            for var in csp.getVariables():
                if not assignment.has_assignment(var):
                    if len(csp.getDomainValues(var)) < minimum:
                        minimum = len(csp.getDomainValues(var))
                        resVar = var
            return resVar
    
    def orderDomainValues(self, csp, var):
        return csp.getDomainValues(var)
    
    def fireListeners(self,csp,assignment):
        for listener in self._listeners:
            listener.fireChange(csp,assignment)