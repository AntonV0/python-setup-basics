"""File helpers module for my_library package."""


def read_file(file_path):
    """Read the contents of a file and return it as a string."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def write_file(file_path, content):
    """Write a string to a file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
