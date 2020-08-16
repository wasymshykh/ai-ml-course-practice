'''
Created on Mar 6, 2019

@author: dr.aarij
'''
import copy
class Assignment(object):
    '''
    classdocs
    '''


    def __init__(self):
        self._variables = []
        self._valueOfVariable = {}
    
    def addVariableToAssignment(self,var,value):
        if var not in self._valueOfVariable:
            self._variables.append(var)
        self._valueOfVariable[var] = value
    
    def removeVariableFromAssignment(self,var):
        if var in self._valueOfVariable:
            self._variables.remove(var)
            del self._valueOfVariable[var]
    
    def getAssignmentOfVariable(self,var):
        if var not in self._valueOfVariable:
            return None
        return self._valueOfVariable[var]
    
    
    def isConsistent(self,constraints):
        for con in constraints:
            if not con.isConsistentWith(self):
                return False
        
        return True
        
    
    def hasAssignmentFor(self,var):
        return var in self._valueOfVariable
    
    def isComplete(self,variables):
        for var in variables:
            if not self.hasAssignmentFor(var):
                return False        
        return True
    
    def returnCopy(self):
        variables = copy.deepcopy(self._variables)
        values = copy.deepcopy(self._valueOfVariable)
        
        assignment = Assignment()
        
        assignment._variables = variables
        assignment._valueOfVariable = values
        
        return assignment

    def isSolution(self,csp):
        return self.isComplete(csp.getVariables()) and self.isConsistent(csp.getListOfConstraints())
    
    def __str__(self):
        result = []
        
        for var in self._variables:
            result.append(("%s = %s")%(var,self._valueOfVariable[var]))
        
        return str(result)