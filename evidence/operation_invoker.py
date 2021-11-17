class OperationInvoker():
    def __init__(self) -> None:
        self._commands = []
    
    def add_command(self, cmd):
            self._commands.append(cmd)

    def remove_command(self, cmd):
        self._commands.remove(cmd)

    def run_command(self):
        for cmd in self._commands:
            cmd.execute()
