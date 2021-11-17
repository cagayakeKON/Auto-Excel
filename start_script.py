
from builder.file_looper import FileLooper
from builder.operation_builder import OperationBuilder
from operation.replace_str_operationl import ReplaceStrOperation
import re

file_looper = (OperationBuilder().set_folder_path("C:/Users/001496-liteng/Desktop/Bridgestone/STEF/1116")
            #    .add_operation(ReplaceStrOperation("a", "b"))
               .add_operation(ReplaceStrOperation("b","",lambda path:path,1))
               .build())
               
file_looper.run()

