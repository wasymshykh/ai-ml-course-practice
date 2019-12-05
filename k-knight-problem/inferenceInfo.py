'''
Created on Mar 6, 2019

@author: dr.aarij
'''
import copy

class InferenceInfo(object):
    '''
    classdocs
    '''


    def __init__(self,csp,variable,value,inferenceProcedure):
        self._variableDomains = copy.deepcopy(csp.getVariableDomains())
        self._affectedVariables = []
        self._inferenceProcedure = inferenceProcedure
        self._affectedVariablesMap = {}        

    def isFailure(self,csp,variable,value):
        for av in self._affectedVariables:
            if len(av[1]) == 0:
                return True
        return False
    
    def doInference(self,csp,variable,value):
        return self._inferenceProcedure.doInference(self,csp,variable,value)
    
    def getAffectedVariables(self):
        return self._affectedVariables
    
    def addToAffectedVariables(self,var,domainList):
        self._affectedVariablesMap[var] = domainList
    
    def getDomainsOfAffectedVariables(self,var):
        if var in self._affectedVariablesMap:
            return self._affectedVariablesMap[var]
        return None
                
    def setInferencesToAssignments(self,assignment,csp):
        for var,domains in self._affectedVariablesMap.items():          
            csp.addVariableDomain(var,domains)
    
    def restoreDomains(self,csp):
        csp.setVariableDomains(self._variableDomains)