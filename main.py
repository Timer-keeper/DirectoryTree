from directory_tree_generator import DirectoryTreeGenerator
from output_manager import OutputManager

if __name__ == "__main__":
    directory = input("请输入要列出的目录路径: ")
    base_output_filename = "directory_tree_with_content"
    output_manager = OutputManager(base_output_filename)
    output_filename = output_manager.write_directory_tree(directory)
    print(f"目录树及文件内容已保存至 {output_filename}")