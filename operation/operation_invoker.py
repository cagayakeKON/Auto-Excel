class OperationInvoker():
    def __init__(self) -> None:
        self._preparing_for_operation = []
        self._operation = []
    
    def add_preparing_for_operation(self, cmd):
        self._preparing_for_operation.append(cmd)

    def remove_preparing_for_operation(self, cmd):
        self._preparing_for_operation.remove(cmd)
        
    def ada_operation(self, cmd):
        self._operation.append(cmd)

    def remove_operation(self, cmd):
        self._operation.remove(cmd)
  
    def run_command(self):
        for cmd in self._operation:
            cmd.execute()
        for cmd in self._preparing_for_operation:
            cmd.execute()