import urllib.request
from bs4 import BeautifulSoup as bs
import re
import pandas as pd

#Parse all functions from the random py library

#load html code from a url
url = "https://docs.python.org/3/library/random.html"
page = urllib.request.urlopen(url)

soup = bs(page)
#print(soup)

#get names of function
names = soup.body.findAll('dt')
#print(names)

function_names = re.findall('id="random.\w+', str(names))
function_names = [item[4:] for item in function_names]
#print(function_names)

#get description
description = soup.body.findAll('dd')
#print(description)

function_usage = []

for item in description:
    #get rid of html tags
    item = item.text
    #get rid next line operator
    item = item.replace('\n' , ' ')
    function_usage.append(item)

#print(function_names)
#print(function_usage)

print(len(function_names))
print(len(function_usage))

#create a dataFrame with pandas
data = pd.DataFrame({'function name': function_names, 'function usage': function_usage})
print (data)

#write to csv
data.to_csv('data.csv')