import os


class Operation():
    def __init__(self,root_path,file_type):
        pass

    

    def __get_all_folder(self):
        file_list = []
        for root, dirs , fs in os.walk(self.root_path,False):
            return dirs 