from bs4 import BeautifulSoup
import urllib
import json
import re

def process_string(strng):
    name = strng[:]
    # Remove text inside parentheses
    re.sub("(.*?)", "", strng)

    # Remove all dashes
    name = name.replace("-", "")

    # Remove all dots
    name = name.replace(".", "")

    # Remove "and" and break the string up into a list of drug names
    lst = name.split("and")

    # Remove commas and break the string up into a longer list
    res = []
    for l in lst:
        res.extend(l.split(","))

    for i in range(len(res)):
        res[i] = res[i].title()
        res[i] = res[i].replace(" ", "")

    return res

def parse_indexes(soup):
    indexes = soup.find("ul", {"id" : "index"})
    res = {}
    for i in indexes:
        if i.name == "li":
            link = i.find("a")
            if link != None:
                name = link.get_text()
                lst = process_string(name)
                for l in lst:
                    res[l] = link["href"]


            key = i.find("span")
            if key != None:
                alias = ""
                for child in key.children:
                    if child.name == None:
                        alias += child.string

                lst = process_string(alias)
                for l in lst:
                    res[l] = link["href"]
    return res

''' Example usage:

url = "https://medlineplus.gov/druginfo/drug_Aa.html"
r = urllib.urlopen(url).read()
soup = BeautifulSoup(r, "html.parser")
print parse_indexes(soup)

'''
