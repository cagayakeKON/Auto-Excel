from abc import ABCMeta,abstractclassmethod

class ExcelOparate(metaclass = ABCMeta):
    
    @abstractclassmethod
    def excute():
        pass
    
    
class Task(ExcelOparate):
    pass


class Agent:
    def __init__(self) -> None:
        self._task_queue =[]
    
    def executeTask(self,task):
        self._task_queue.append(task)
        task.excute
        
