'''
Created on Mar 6, 2019

@author: dr.aarij
'''

class Variable(object):
    '''
    classdocs
    '''


    def __init__(self, name):
        '''
        Constructor
        '''
        
        self._name = name
    
    def getName(self):
        return self._name
    
    def __eq__(self, other):
        return self.getName() == other.getName()
    
    def __hash__(self):
        return hash(self._name)
    
    def __str__(self):
        return self._name