from assignment import Assignment

class ForwardCheckingInference:

    def __init__(self):
        pass
    
    def doInference(self,inferenceInfo,csp,variable,value):
        assignment = Assignment()
        assignment.add_variable(variable, value)
        for con in csp.getConstraints(variable):
            otherVariables = csp.getNeighbour(variable, con)
            for ov in otherVariables:
                someValues = []
                changed = False
                domVals = inferenceInfo.getDomainsOfAffectedVariables(ov)
                if domVals is None:
                    domVals = csp.getDomainValues(ov)
                    
                for domVal in domVals:
                    assignment.add_variable(ov, domVal)
                    if not con.is_consistent(assignment):
                        changed = True
                    else:
                        someValues.append(domVal)
                
                if changed:
                    inferenceInfo.addToAffectedVariables(ov,someValues)
                    
                assignment.remove_variable(ov)
        return []        
    