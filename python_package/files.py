import pathlib
from pathlib import Path

path1 = pathlib.Path.cwd()
folder_a = path1 / "folder_a"
folder_a.mkdir(exist_ok=True)

file_paths = [
    folder_a / "private.img",
    folder_a / "lyrics.txt",
    folder_a / "alone.vid",
    folder_a / "inside.csv",
    folder_a / "bible.txt",
    folder_a / "looks.jpg"
]
# for path in file_paths:
#     path.touch()

# for files in path1.rglob("*.py"):
  #  print(files.name)

source = path1 / "test.py"
print(source)
destination = pathlib.Path(r"C:\Users\PC\PycharmProjects\dujadin_projects\chapter_four\test.py")
source.replace(destination)
destination = path1 / "chapter_four" / "test.py"
source.replace(destination)

# for file in folder_a.iterdir():
#     print(file.name)
#
# print(list(folder_a.iterdir()))
# print(path1)

# fake_path = Path("C:/kelloges/private.img")
# cwd_path = Path.cwd() / "chapter_five"
# print(cwd_path)
# print("Parent -", fake_path.parent)
# print(list(fake_path.parents))
# print("Anchor -", fake_path.anchor)
# print("Name -", fake_path.name)
# print("Suffix -", fake_path.suffix)
# print("Stem -", fake_path.stem)
#
# cwd_path.mkdir(exist_ok=True)
# new_file_path = cwd_path / "Assignment_two"
# new_file_path.touch()
#
# print("Exists -", fake_path.exists())
# print("Exists? -", cwd_path.exists())
# print("isDir -", cwd_path.is_file())
# print("isDir -", cwd_path.is_dir())
#
# # creating a file with the command function "x"
# f = open("assignment.py", "x")
# creating a file with the command function "w"
# f = open("assignment.py", "w")
