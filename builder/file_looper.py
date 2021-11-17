import tools

class FileLooper():
    
    
    def __init__(self,path,invoker) -> None:        
        self.path = path
        self.invoker = invoker
    
    def run(self):
        path_list = tools.find_all_file(self.path)
        for path in path_list:
            FileLooper.processing_file_name_path[0]=path
            self.invoker.run_command()
            

            