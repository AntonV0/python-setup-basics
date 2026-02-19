"""Tests for the web_scrapers module in the my_library package."""

from my_library.web_scrapers import scrape_website, extract_links


def test_scrape_website():
    # Assert that the scrape_website function returns a string containing the URL
    url = "http://example.com"
    content = scrape_website(url)
    assert isinstance(content, str)
    assert url in content


def test_extract_links():
    # Assert that the extract_links function returns a list of URLs
    html = "<html><body><a href='http://example.com/page1'>Page 1</a><a href='http://example.com/page2'>Page 2</a><a href='http://example.com/page3'>Page 3</a></body></html>"
    links = extract_links(html)
    assert isinstance(links, list)
    assert len(links) == 3
    assert all(link.startswith("http://example.com/") for link in links)


# Run the tests
if __name__ == "__main__":
    test_scrape_website()
    test_extract_links()
    print("All tests passed!")
