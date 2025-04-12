import os
import textwrap
import datetime
from directory_tree_generator import DirectoryTreeGenerator


class OutputManager:
    def __init__(self, base_output_filename):
        self.base_output_filename = base_output_filename

    def create_output_file(self, directory):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"{self.base_output_filename}_{timestamp}.md"
        return output_filename

    def write_directory_tree(self, directory):
        output_filename = self.create_output_file(directory)
        with open(output_filename, "w", encoding="utf-8") as file_output:
            print(f"# 项目目录结构\n\n```\n{directory}\n", file=file_output)
            DirectoryTreeGenerator(directory).generate(file_output)
            print("```\n", file=file_output)
        return output_filename
