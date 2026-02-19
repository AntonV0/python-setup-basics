"""Individual Lab: Testing a Personal Library"""

from tests.test_data_analysers import test_calculate_total, test_calculate_mean
from tests.test_web_scrapers import test_scrape_website, test_extract_links
from tests.test_file_helpers import test_read_file, test_write_file


def run_all_tests():
    tests = [
        test_calculate_total,
        test_calculate_mean,
        test_scrape_website,
        test_extract_links,
        test_read_file,
        test_write_file,
    ]

    for test in tests:
        test()  # will raise AssertionError if it fails

    print("✅ All tests passed!")


if __name__ == "__main__":
    run_all_tests()
