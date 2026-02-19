"""Tests for the file_helpers module in the my_library package."""

from my_library.file_helpers import read_file, write_file


def test_read_file():
    # Create a temporary file for testing
    test_file_path = 'test_file.txt'
    with open(test_file_path, 'w', encoding='utf-8') as file:
        file.write('Hello, World!')

    # Assert that the read_file function returns the correct content
    assert read_file(test_file_path) == 'Hello, World!'


def test_write_file():
    # Create a temporary file path for testing
    test_file_path = 'write_file.txt'

    # Use the write_file function to write content to the file
    write_file(test_file_path, 'Testing write function.')

    # Assert that the content was written correctly by reading it back
    with open(test_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        assert content == 'Testing write function.'


# Run the tests
if __name__ == "__main__":
    test_read_file()
    test_write_file()
    print("All tests passed!")
