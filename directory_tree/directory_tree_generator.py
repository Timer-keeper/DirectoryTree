import os
import textwrap
from file_handler import FileHandler
from concurrent.futures import ThreadPoolExecutor, as_completed
import fnmatch


class DirectoryTreeGenerator:
    def __init__(self, rootdir):
        self.rootdir = rootdir
        self.ignore_patterns = self._load_gitignore(rootdir)

    def _load_gitignore(self, directory):
        gitignore_path = os.path.join(directory, ".gitignore")
        patterns = []
        if os.path.isfile(gitignore_path):
            try:
                with open(gitignore_path, "r", encoding="utf-8") as f:
                    patterns = [
                        line.strip()
                        for line in f
                        if line.strip() and not line.startswith("#")
                    ]
            except UnicodeDecodeError as e:
                print(f"无法读取.gitignore文件: {e}")
        return patterns

    def _is_ignored(self, path):
        for pattern in self.ignore_patterns:
            if fnmatch.fnmatch(path, pattern) or fnmatch.fnmatch(
                os.path.basename(path), pattern
            ):
                return True
        return False

    def generate(self, file_output, prefix=""):
        entries = sorted(os.listdir(self.rootdir))

        with ThreadPoolExecutor() as executor:
            futures = []
            for index, entry in enumerate(entries):
                path = os.path.join(self.rootdir, entry)
                if self._is_ignored(path):
                    continue
                is_last = index == len(entries) - 1
                futures.append(
                    executor.submit(
                        self._process_entry, path, file_output, prefix, is_last
                    )
                )
            for future in as_completed(futures):
                future.result()

    def _process_entry(self, path, file_output, prefix, is_last):
        if os.path.isdir(path):
            print(
                textwrap.indent(
                    f"**{os.path.basename(path)}/**",
                    prefix + ("└── " if is_last else "├── "),
                ),
                file=file_output,
            )
            DirectoryTreeGenerator(path).generate(
                file_output, prefix + ("    " if is_last else "│   ")
            )
        else:
            print(
                textwrap.indent(
                    f"**{os.path.basename(path)}**",
                    prefix + ("└── " if is_last else "├── "),
                ),
                file=file_output,
            )
            FileHandler.handle(
                path, file_output, prefix + ("    " if is_last else "│   ")
            )
