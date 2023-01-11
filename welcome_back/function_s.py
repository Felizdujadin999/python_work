from pathlib import Path


def write_into_a_file(file_name: str):
    list_one = []
    source = Path.home() / "desktop" / "file_created"
    source.mkdir(exist_ok=True)
    new_file = source / file_name
    new_file.touch(exist_ok=True)
    new_file.write_text("Hello precious, HAPPY NEW YEAR!!!......")
    string_format_text = new_file.read_text()
    lists = string_format_text.split(" ")
    return lists


print(write_into_a_file("fileOne.txt"))
