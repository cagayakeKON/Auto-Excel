
from builder.file_looper import FileLooper
from builder.operation_builder import OperationBuilder
from operation.replace_str_operationl import ReplaceStrOperation

processing_file = ""

file_looper = (OperationBuilder().set_folder_path("C:/Users/001496-liteng/Desktop/Bridgestone/STEF/1116")
               .add_operation(ReplaceStrOperation("a","b",FileLooper.processing_file_name_path))
               .build())
file_looper.run()