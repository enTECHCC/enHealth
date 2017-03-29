from bs4 import BeautifulSoup
import urllib
import json

# r = urllib.urlopen("https://medlineplus.gov/druginfo/meds/a682683.html").read()
# r = urllib.urlopen("https://medlineplus.gov/druginfo/meds/a681006.html").read()
# soup = BeautifulSoup(r, "html.parser")

def getSourceAddr(url):
	return url

def getGenericName(soup):
	res = soup.find("h1", {"class":"with-also"})
	return res.string

def getUsage(soup):
	usage_parags = soup.find("div", {"id":"how"}).find_all("p")
	res = ""
	for p in usage_parags:
		res += p.string
	return res

def getGeneralDescriptions(soup):
	descriptions = soup.find("div", {"id":"why"}).find_all("p")
	res = ""
	for des in descriptions:
		res += des.string
	return res

def getBrandNames(soup):
	res = []
	name_lists = soup.find("div", {"id":"brand-name-1"}).find_all("ul")
	for lst in name_lists:
		for item in lst:
			# Discard the list items that are discontinued
			link = item.find("a")
			
			if ((not link == None) and (link["href"] == "\#discontinued")) or (link == None):
				contents = item.contents
				for c in contents:
					if c.name == None:
						res.append(c)
						break
	return res

def getSideEffects(soup):
	effect_lists = soup.find("div", {"id":"side-effects"}).find_all("ul")
	
	res = []
	
	for lst in effect_lists:
		for item in lst:
			res.append(item.get_text())
	
	return res

def getWarnings(soup):
	warning_lists = soup.find("div", {"id":"section-precautions"}).find_all("ul")
	res = ""
	for lst in warning_lists:
		for item in lst:
			res += item.string
	return res

# Function that takes a soup object and returns a json object
def jsonify(soup):
	data = {}
	data["GenericName"] = getGenericName(soup)
	data["GeneralDescriptions"] = getGeneralDescriptions(soup)
	data["Usage"] = getUsage(soup)
	data["BrandName"] = getBrandNames(soup)
	data["SideEffectsParag"] = getSideEffects(soup)
	data["Warnings"] = getWarnings(soup)
	data["Source"] = "https://medlineplus.gov/"
	data["RecommendedDosage"] = None
	data["OverTheCounter"] = None
	data["Interactions"] = None
	data["ActiveIngredients"] = None
	data["SideEffectsParag"] = None
	return json.dumps(data, indent = 4, sort_keys = True)
	
# print jsonify(soup)
