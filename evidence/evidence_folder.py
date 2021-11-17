import re,os
from evidence.operation import Operation

class EvidenceFolder(Operation):
    def __init__(self,root_path,folder_name,regex):
        self.root_path = root_path
        self.folder_name = folder_name
        self.regex = regex
        self._preparation = []
        self._opration = []
        
    def execute(self):
        for task in self._preparation:
            task.execute()
        for task in self._opration:
            task.execute()
    
    @property
    def full_path(self):
        return os.path.join(self.root_path,self.folder_name)

    @property
    def check_number(self):
        check_number_list = re.compile(self.regex).findall(self.folder_name)
        if(len(check_number_list)>0):
            return re.compile(self.regex).findall(self.folder_name)[0]
        else :
            return ""

