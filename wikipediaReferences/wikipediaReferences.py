import csv
import requests
from bs4 import BeautifulSoup


def pickReferences(page):
    try:
        print('MSG: getting references...')
        references = page.find_all(class_='references')
        references = references[len(references)-1]
        return references
    except Exception:
        raise


def getPage(url):
    try:
        print('MSG: getting page...')
        page = requests.get(url)
        pageSoup = BeautifulSoup(page.text, 'html.parser')
        return pageSoup
    except Exception:
        raise

def writeArchive(title, references):
    try:
        print('MSG: writing file...')
        archive = open(title + '.csv', 'w', newline='', encoding='utf-8')
        writer = csv.writer(archive)
        for link in references:
            cite = link.find('cite')
            if (hasattr(cite, 'a')):
                href = cite.a['href']
                name = cite.a.text
                writer.writerow([name, href])
    except Exception:
        raise
    else:
        print('MSG: done!')


while True:
    url = input('URL: ')
    try:
        page = getPage(url)
        title = page.title.text
        references = pickReferences(page)
        writeArchive(title, references)
    except Exception as e:
        print('ERROR: something went wrong!')

