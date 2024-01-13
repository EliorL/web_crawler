import threading
import time
from queue import Queue
from spider import Spider
from domain import *
from general import *

HOMEPAGE = "https://crawler-test.com/"
DOMAIN_NAME = get_domain_name(HOMEPAGE)
PROJECT_NAME = 'crawled_site_' + DOMAIN_NAME
QUEUE_FILE = os.path.join(PROJECT_NAME, 'queue.txt')
CRAWLED_FILE = os.path.join(PROJECT_NAME, 'crawled.txt')
# Number of threads the system can handle.
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


def create_workers():
    """Create worker threads (will stop when main exits)."""
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


def work():
    """Do the next job in queue."""
    end_time = time.time() + 600
    while True:
        if time.time() > end_time:
            print("Timeout: process stopped due to timeout of 10 minutes.")
            break
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        # Report system that job done.
        queue.task_done()


def create_jobs():
    """Each queued link is a new job."""
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    # Wait for other threads.
    queue.join()
    crawl()


def crawl():
    """Check if there are items in queue, if so crawl them."""
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(f'{len(queued_links)} links in the queue')
        create_jobs()


create_workers()
crawl()
print("Finished.")
