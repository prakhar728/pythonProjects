import requests

URL=input("Enter the URL you wish ")
r=requests.get(URL)

from bs4 import BeautifulSoup

soup=BeautifulSoup(r.content,'html5lib')
print(soup.prettify())
print("\n \n \n")
from urllib.parse import urlparse, urljoin

domainName = urlparse(URL).netloc
print(" The DOMAIN NAME IS : \n"+domainName)

externalUrls = set()
internalUrls = set()

def url_extractor(URL):
    print("\n EXTRACTING URLS \n")
    for link in soup.find_all('a'):
        href=link.attrs.get("href")
        if href=="" or href== None:
            continue
        href=urljoin(URL,href)
        parsedHref = urlparse(href)

        href= parsedHref.scheme + "://" + parsedHref.netloc + parsedHref.path
        if href in internalUrls:
            continue
        if domainName not in href:
            if href not in externalUrls:
                print(" External Link : "+href)
                externalUrls.add(href)
            continue
        print(" Internal Link : "+ href)
        internalUrls.add(href)
    print("URLS EXTRACTED")

def MetaContentExtractor(URL):
    print("\nEXTRACTING META CONTENT\n")
    for metaTag in soup.find_all('meta'):
            print("\n")
            for i in metaTag.attrs:
                print(i," ",metaTag.attrs[i],end='||')
    print("Meta content Extracted")

internalImgs = set()
externalImgs = set()

def ImageExtractor(URL):
    print("\n EXTRACTING IMAGES \n")
    for imgTag in soup.find_all('img'):
        src=imgTag.attrs.get('src')
        if src=="" or src== None:
            continue
        src=urljoin(URL,src)
        parsedSrc = urlparse(src)

        src= parsedSrc.scheme + "://" + parsedSrc.netloc + parsedSrc.path
        if src in internalImgs:
            continue
        if domainName not in src:
            if src not in externalImgs:
                print(" External Image : "+src)
                externalImgs.add(src)
            continue
        print(" Internal Image : "+ src)
        internalImgs.add(src)
    print("Images Extracted")

url_extractor(URL)
MetaContentExtractor(URL)
ImageExtractor(URL)