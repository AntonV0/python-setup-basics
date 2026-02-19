"""Data analysers module for my_library package."""


def calculate_total(numbers):
    """Calculate the total of a list of numbers."""
    return sum(numbers)


def calculate_mean(numbers):
    """Calculate the mean of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
