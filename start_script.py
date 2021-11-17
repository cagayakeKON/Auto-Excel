
from builder.file_looper import FileLooper
from builder.operation_builder import OperationBuilder
from operation.replace_str_operationl import ReplaceStrOperation

file_looper = (OperationBuilder().set_folder_path("C:/Users/001496-liteng/Desktop/Bridgestone/STEF/1116")
               .add_operation(ReplaceStrOperation("a","b"))
               .build())
file_looper.run()