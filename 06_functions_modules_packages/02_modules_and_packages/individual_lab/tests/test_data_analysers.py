"""Tests for the data_analysers module in the my_library package."""

from my_library.data_analysers import calculate_total, calculate_mean


def test_calculate_total():
    # assert that the total of the list is correct
    assert calculate_total([1, 2, 3, 4]) == 10

    # assert that the total of an empty list is 0
    assert calculate_total([]) == 0

    # assert that the total of negative numbers is correct
    assert calculate_total([-1, -2, -3]) == -6


def test_calculate_mean():
    # assert that the mean of the list is correct
    assert calculate_mean([1, 2, 3, 4]) == 2.5

    # assert that the mean of an empty list is 0
    assert calculate_mean([]) == 0

    # assert that the mean of negative numbers is correct
    assert calculate_mean([-1, -2, -3]) == -2.0


# Run the tests
if __name__ == "__main__":
    test_calculate_total()
    test_calculate_mean()
    print("All tests passed!")
