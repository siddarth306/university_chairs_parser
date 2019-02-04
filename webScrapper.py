import requests
from bs4 import BeautifulSoup
import csv


"""def strategy1():
    a

def strategy2():


def strategy3():"""


URL = "https://en.wikipedia.org/wiki/List_of_engineering_schools#United_States"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

table = soup.findAll("table")[7:8]

count1 = 0
count2 = 0
for row in table[0].findAll("tr"):
    univ_link = row.findAll("td")
    if len(univ_link) >= 3:
        engg_link = univ_link[2].find("a")
        if engg_link is not None:
            #print(engg_link['href'])
            WIKI_URL = "https://en.wikipedia.org" + engg_link['href']
            wiki_r = requests.get(WIKI_URL)
            wiki_soup = BeautifulSoup(wiki_r.content, 'html5lib')
            wiki_table = wiki_soup.findAll("table", {"class" ,"infobox"})
            if wiki_table is not None:
                if len(wiki_table) >=1:
                    department_url = wiki_table[0].findAll("span",{"class","url"})
                count1 += (len(wiki_table) == 1)

                if len(wiki_table) > 1:
                    print(WIKI_URL)


