'''
Created on Mar 6, 2019

@author: dr.aarij
'''
from abc import abstractmethod

class SearchStrategy(object):
    '''
    classdocs
    '''


    def __init__(self, listeners = []):
        self._listeners = listeners
    
    def addListeners(self,listener):
        self._listeners.append(listener)
    
    def removeListeners(self,listener):
        if listener in self._listeners:
            self._listeners.remove(listener)
    
    def fireListeners(self):
        for listener in self._listeners:
            listener.fireChange()
    
    @abstractmethod
    def solve(self,csp):pass