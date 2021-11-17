from builder.file_looper import FileLooper
from operation.operation_invoker import OperationInvoker


class OperationBuilder():

    def __init__(self):
        self.invoker = OperationInvoker()

    def set_folder_path(self, path):
        self.path = path
        return self

    def add_operation(self, operation):
        self.invoker.ada_operation(operation)
        return self

    def add_preparing_for_operation(self, operation):
        self.invoker.add_preparing_for_operation(operation)
        return self

    def build(self) -> FileLooper:
        return FileLooper(self.path, self.invoker)
