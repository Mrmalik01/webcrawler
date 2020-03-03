from urllib.request import urlopen
from pprint import PrettyPrinter
from bs4 import BeautifulSoup
import os

URL = "http://www.columbia.edu/~fdc/sample.html"

data =  urlopen(url=URL)


# Beautiful Soup is a third party library used to parse HTML documents
bs_object = BeautifulSoup(data.read(), "html.parser")

# To get all the anchor tags from the html source code
print(bs_object.a)

# To get the title of the page
print(bs_object.title)

# To get the head tag of the page
print(bs_object.head)


def create_project_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)