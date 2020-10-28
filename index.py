from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import os.path

print("Unesi url stranice kako bi srejpali podatke")


def getUrl(my_url):
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    return page_html


def scrapping_data(location, pageSoup):
    print('Unesi lokaciju')
    x = location
    inputPath = os.path.join(os.path.expanduser("~"), x)
    if os.path.exists(inputPath):
        directory = os.path.join(os.path.expanduser('~'), x)
        page_soup = soup(pageSoup, "html.parser")

        siteData1 = open(os.path.join(directory, "index.html"), "w+")
        siteData2 = open(os.path.join(directory, "index.css"), "w+")

        siteData1.write(str(page_soup.body))
        siteData2.write((str(page_soup.style)))

    else:
        print("progresna lokacije debilu")
