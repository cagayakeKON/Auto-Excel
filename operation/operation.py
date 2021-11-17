from abc import ABCMeta, abstractmethod

class Operation(metacalss = ABCMeta):
    
    @abstractmethod
    def execute(self):
        pass
