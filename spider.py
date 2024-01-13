from urllib.request import urlopen
from link_finder import LinkFinder
from general import *


class Spider:
    """Add links to waiting list according to pages and move to file."""
    # Shared among all instances.
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name):
        # Shared information
        Spider.domain_name = domain_name
        Spider.base_url = base_url
        Spider.project_name = project_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        self.boot()
        # Will be ignored after created once
        self.crawl_page('First spider', Spider.base_url)

    @staticmethod
    def boot():
        """Create folder and add files."""
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        """Insure page not crawled and then start crawling."""
        if page_url not in Spider.crawled:
            print(f'{thread_name} now crawling {page_url}')
            print(f'Queue {len(Spider.queue)} | Crawled {len(Spider.crawled)}')
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            # Move from waiting list to crawled list.
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            # Convert sets to files.
            Spider.update_files()

    @staticmethod
    def gather_links(page_url):
        """Crawl page and return set of links or empty set."""
        html_string = ''
        try:
            response = urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                # Covert to html string.
                html_string = html_bytes.decode('utf-8')

            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except Exception as e:
            print(f'Error: can not crawl page {page_url}. Error name = {e}')
            return set()
        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        """Take set of links and add to existing waiting list."""
        for url in links:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            # Insure not crawl to other websites even if there are links for them.
            if Spider.domain_name not in url:
                continue

            Spider.queue.add(url)

    @staticmethod
    def update_files():
        """Update created files to save data."""
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)
