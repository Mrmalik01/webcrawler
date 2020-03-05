from urllib.request import urlopen
from link_finder import LinkFinder
from tool import *

###
# Description : Spider is basically a web crawler, that will move to various websites and collect all urls
### Variables
# project_name - base url of the code directory
# base_url - base url of a website
# domain_name - domain of a website. It is used to make sure our spider doesnt move to another domain name.
# All these variables will be shared between different spiders - (concurreny)
###
class Spider:
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_files = ''
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + "/queue.txt"
        Spider.crawled_files = Spider.project_name + "/crawled.txt"

        # It will create project directory that will contain queue and crawled file
        self.boot()

        self.crawl_page('First spider', Spider.base_url)

    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled_files = file_to_set(Spider.crawled_files)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled_files:
            print(thread_name+": crawling - "+page_url)
            print("\tQueue list - " + str(len(Spider.queue))+" | Crawled list - "+str(len(Spider.crawled_files)))
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled_files.add(page_url)
            Spider.update_files()

    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if 'text.html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except Exception as e:
            print(str(e))
            return set()
        return finder.page_links()
