import os
import textwrap
import datetime
from directory_tree_generator import DirectoryTreeGenerator  # 导入DirectoryTreeGenerator类

class OutputManager:
    def __init__(self, base_output_filename):
        self.base_output_filename = base_output_filename
    
    def create_output_file(self, directory):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"{self.base_output_filename}_{timestamp}.txt"
        return output_filename

    def write_directory_tree(self, directory):
        output_filename = self.create_output_file(directory)
        with open(output_filename, 'w', encoding='utf-8') as file_output:
            print(directory, file=file_output)  # 打印根目录名称
            DirectoryTreeGenerator(directory).generate(file_output)  # 使用DirectoryTreeGenerator类生成目录树
        return output_filename