import re,os

class EvidenceFolder():
    def __init__(self,mode,root_path,regex,folder_name):
        self.root_path = root_path
        self.regex = regex
        self.check_number = re.compile(regex)
        self.folder_name = folder_name

    def __init__(self,mode,src):
        pass

    def change_self_folder_name(self,new_folder_name):
        self.folder_name = new_folder_name
        os.rename(os.path.join(self.root_path,self.folder_name),os.path.join(self.root_path,new_folder_name))

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

    def __list_all_file():
        pass
