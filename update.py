#Imports
import time
from bs4 import BeautifulSoup
import requests

def check():
    testfile = open("website.txt", "r")
    checkupdate = ''.join(testfile.readlines())
    #set URL and request page
    URL = 'https://secure.runescape.com/m=news/archive?oldschool=1'
    page = requests.get(URL, headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11.0; rv:84.0) Gecko/20100101 Firefox/84.0'})
    #Parse page content
    content = BeautifulSoup(page.content, 'html.parser')
    #print(soup.prettify())
    content.prettify()
    print (content)
    updatepage = str(content.find_all("h4")[2])
    if checkupdate == updatepage:
        testfile.close()
        print(updatepage)
        print ("No update was done")
    else:
        testfile.close()
        print(checkupdate)
        print(updatepage)
        print ("Update was done")
        testfile2 = open("website.txt", "w")
        testfile2.write(updatepage)
        print("Update was written")

#check()

while True:
    check()
    time.sleep(15)