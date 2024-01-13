from html.parser import HTMLParser
from urllib import parse


class LinkFinder(HTMLParser):
    """Return all links in page."""

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        """Find where html tag begin."""
        # Upon use of HTMLParser feed() this function is called when it encounters an opening tag <a>
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    # If relative url add base url
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)

    def page_links(self):
        """Return set of page links."""
        return self.links

    def error(self, message):
        """Html parser method to handle errors."""
        pass
