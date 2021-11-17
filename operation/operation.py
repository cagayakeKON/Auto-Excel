from abc import ABCMeta, abstractmethod

class Operation(object):
    
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def execute(self):
        pass
