class FileLooper():
    def __init__(self,path,invoker) -> None:        
        self.path = path
        self.invoker = invoker

    def run(self):
        self.invoker.execute()
    