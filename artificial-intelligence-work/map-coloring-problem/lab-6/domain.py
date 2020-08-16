'''
Created on Mar 6, 2019

@author: dr.aarij
'''
import copy

class Domain(object):
    '''
    classdocs
    '''


    def __init__(self, values):
        '''
        Constructor
        '''
        
        self._values = copy.deepcopy(values)
    
    def getValues(self):
        return self._values