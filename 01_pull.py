# -----------------------------------------------
#  1. Data Acquisition:
# 
#  Objective: Download all the public course 
#  catalog data in raw HTML format from a 
#  university website.
# 
#  Tools/Resources: Extract all the course 
#  catalog data from one of the follow 
#  three universities:
#     Harvard: https://courses.my.harvard.edu
#     BU: https://www.bu.edu/academics/cas/courses
#     NE: https://catalog.northeastern.edu/course-descriptions
# -----------------------------------------------


import urllib.request
import ssl
from random import *
import time

from bs4 import BeautifulSoup



context = ssl._create_unverified_context()


def pull (url):
    data = urllib.request.urlopen(url, context=context).read()
    text = data.decode('utf-8')
    return text


def store (data, file):
    f = open('filedump/' + file, 'w')
    f.write(data)
    f.close()
    print(f'File saved as: {file}')

homepage = pull('https://catalog.northeastern.edu/course-descriptions/')
homepage = homepage.replace('\n', '').replace('\r', '')
soup = BeautifulSoup(homepage, 'html.parser')
urls = []
for letter in soup.find("div", id="atozindex").contents[1::2]:
    for item in letter.contents:
        print('https://catalog.northeastern.edu' + item.contents[0]['href'])
        urls.append('https://catalog.northeastern.edu' + item.contents[0]['href'].rstrip('/'))


for url in urls:
    ind = url.rfind('/') + 1
    data = pull(url)
    file = url[ind:] + '.html'
    print('Fetching ' + file)
    store(data, file)
    time.sleep(random() * 0.2 + 0.2)

