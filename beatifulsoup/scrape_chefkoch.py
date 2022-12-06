import urllib.request
from bs4 import BeautifulSoup as bs

#load html code from a url

url="https://www.chefkoch.de/rezepte/745721177147257/Lasagne.html"
page = urllib.request.urlopen(url)

soup=bs(page, "html.parser")

ingridientsRaw = soup.body.findAll("table", {"class" :"ingredients"})

ingridientsClean = []

for item in ingridientsRaw:
    #get rid of html tags
    item = item.text
    #get rid of new line operator
    item = item.replace('\n' , ' ')
    item = " ".join(item.split())
    ingridientsClean.append(item)

#print(ingridientsClean)


preparationRaw = soup.body.findAll("article" , {"class" : "ds-box ds-grid-float ds-col-12 ds-col-m-8 ds-or-3"})

for div in preparationRaw:
    preparationDivs = div.findAll("div" , {"class" : "ds-box"})
    #print(len(preparationDivs))
    preparationClean = preparationDivs[0]
    #print(preparationClean.text)


print("Zutaten:")
for ingridient in ingridientsClean:
    print(ingridient)

print("#############################################")
print("Zubereitung:")
print(preparationClean.text)
