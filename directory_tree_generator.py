import os
import textwrap
from file_handler import FileHandler  # 导入FileHandler类

class DirectoryTreeGenerator:
    def __init__(self, rootdir):
        self.rootdir = rootdir

    def generate(self, file_output, prefix=""):
        entries = sorted(os.listdir(self.rootdir))
        
        for index, entry in enumerate(entries):
            path = os.path.join(self.rootdir, entry)
            is_last = index == len(entries) - 1
            
            if os.path.isdir(path):
                print(textwrap.indent(f"{entry}/", prefix + ('└── ' if is_last else '├── ')), file=file_output)
                DirectoryTreeGenerator(path).generate(file_output, prefix + ('    ' if is_last else '│   '))
            else:
                print(textwrap.indent(f"{entry}", prefix + ('└── ' if is_last else '├── ')), file=file_output)
                FileHandler.handle(path, file_output, prefix + ('    ' if is_last else '│   '))