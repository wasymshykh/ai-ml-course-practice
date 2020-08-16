'''
Created on Mar 6, 2019

@author: dr.aarij
'''
from abc import abstractmethod

class Constraint(object):
    '''
    classdocs
    '''


    def __init__(self): pass
    
    @abstractmethod
    def isConsistentWith(self,assignment): pass
    
    @abstractmethod
    def getScope(self): pass