import os
import textwrap
from PIL import Image


class FileHandler:
    TEXT_EXTENSIONS = [
        ".txt",
        ".csv",
        ".json",
        ".md",
        ".html",
        ".xml",
        ".log",
        ".py",
        ".pyc",
    ]
    IMAGE_EXTENSIONS = [".jpg", ".jpeg", ".png", ".gif"]

    @staticmethod
    def handle(filepath, file_output, prefix):
        extension = os.path.splitext(filepath)[1].lower()

        if extension in FileHandler.TEXT_EXTENSIONS:
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                    if content.strip():
                        snippet = (
                            content if len(content) < 500 else content[:500] + "\n..."
                        )
                        print(
                            textwrap.indent(
                                f"\n```{extension[1:]}\n{snippet}\n```\n", prefix
                            ),
                            file=file_output,
                        )
            except Exception as e:
                print(
                    textwrap.indent(f"(无法读取文件内容: {e})", prefix),
                    file=file_output,
                )
        elif extension in FileHandler.IMAGE_EXTENSIONS:
            try:
                img = Image.open(filepath)
                print(
                    textwrap.indent(f"(图像文件大小: {img.size})", prefix),
                    file=file_output,
                )
            except Exception as e:
                print(
                    textwrap.indent(f"(无法读取图像文件: {e})", prefix),
                    file=file_output,
                )
        else:
            print(textwrap.indent("(非文本文件)", prefix), file=file_output)
