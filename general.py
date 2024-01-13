import os


def create_project_dir(directory):
    """Each website crawled created as a separate folder."""
    if not os.path.exists(directory):
        print(f'Creating directory {directory}')
        os.makedirs(directory)


def create_data_files(project_name, base_url):
    """Create queue for waiting list and crawled files (if not created)."""
    # Use files to prevent data loss
    queue = os.path.join(project_name, 'queue.txt')
    crawled = os.path.join(project_name, 'crawled.txt')

    if not os.path.isfile(queue):
        write_file(queue, base_url)

    # after completing crawl, create:
    if not os.path.isfile(crawled):
        write_file(crawled, '')


def write_file(path, data):
    """Create new file."""
    with open(path, 'w', encoding="utf-8") as f:
        f.write(data)


def file_to_set(file_name):
    """Read a file and convert each line to set items for faster reading."""
    results = set()

    with open(file_name, 'rt', encoding="utf-8") as f:
        for line in f:
            results.add(line.replace('\n', ''))

    return results


def set_to_file(links, file_name):
    """Iterate through a set, each item will be a new line in a file."""

    with open(file_name, "w", encoding="utf-8") as f:
        for link in sorted(links):
            try:
                f.write(link + "\n")
            except Exception as e:
                print(f'Error: Can not encode this link: {link}. Error name: {e}')
