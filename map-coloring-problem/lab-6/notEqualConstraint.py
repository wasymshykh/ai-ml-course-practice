'''
Created on Mar 6, 2019

@author: dr.aarij
'''
import constraint

class NotEqualConstraint(constraint.Constraint):
    '''
    classdocs
    '''


    def __init__(self, var1, var2):
        '''
        Constructor
        '''
        self._scope = [var1,var2]
    
    def getScope(self):
        return self._scope
    
    def isConsistentWith(self,assignment):
        val1 = assignment.getAssignmentOfVariable(self._scope[0])
        val2 = assignment.getAssignmentOfVariable(self._scope[1])
        return val1 == None or val2 == None or val1 != val2
        