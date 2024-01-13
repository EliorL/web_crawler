## Multi-Threaded Website Crawler in Python
This utility is designed with the goal of efficiently gathering all links from the main HTML website URL 
and its sub-pages, saving them neatly into organized files.

#### Purpose
The primary objective of this tool is to streamline the process of web crawling, providing a robust solution 
for collecting comprehensive link data from websites. By utilizing multiple threads, 
the crawler enhances performance, making it a valuable asset for tasks that demand efficiency and speed.

#### File Structure
Upon execution, the crawler generates files within the program folder to store the collected data:

- "./crawled_site_{site_name}/crawled.txt": A file containing the links crawled from the website.
- "./crawled_site_{site_name}/queue.txt": This file keeps track of links waiting to be crawled 
(empty upon completion).

#### Getting Started
To use the crawler, follow these simple steps:

- Clone the repository to your local machine.
- Run main.py

* Note: the site crawled in the program cause errors intentionally.
