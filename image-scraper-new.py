from bs4 import BeautifulSoup
import requests
import re
from urllib.request import Request, urlopen
import requests
import os
import http.cookiejar
import json

# parse/cut the html
def get_soup(url,header):
    return BeautifulSoup(urlopen(Request(url,headers=header)),'html.parser')

# change the query for the image
query = input()
query= query.split()
image_type='_'.join(query)
query='+'.join(query)
print(image_type)
print(query)
url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
# print (url)
# add the directory for new images
DIR="/Users/christinekwon/Documents/cos429/final-project/images/"
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
}
soup = get_soup(url,header)

# links for original images, type of  image
ActualImages=[]
for a in soup.find_all("div",{"class":"rg_meta"}):
    link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
    ActualImages.append((link,Type))

print  ("there are total " + str(len(ActualImages)) + " images")

if not os.path.exists(DIR):
            os.mkdir(DIR)
DIR = os.path.join(DIR, query.split()[0])

if not os.path.exists(DIR):
            os.mkdir(DIR)
# print images
for i , (img , Type) in enumerate( ActualImages):
    try:
        # req = Request(img, headers={'User-Agent' : header})
        # raw_img = urlopen(req).read()
        raw_img = urlopen(Request(img)).read()
        cntr = len([i for i in os.listdir(DIR) if image_type in i]) + 1
        print (cntr)
        if len(Type)==0:
            f = open(os.path.join(DIR , image_type + "_"+ str(cntr)+".jpg"), 'wb')
        else :
            f = open(os.path.join(DIR , image_type + "_"+ str(cntr)+"."+Type), 'wb')

        f.write(raw_img)
        f.close()

    except Exception as e:
        print ("could not load : " + str(img))
        print (e)