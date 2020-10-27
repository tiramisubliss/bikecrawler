from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from pprint import pprint
from urllib.request import Request, urlopen
import uuid
import re
from requests.utils import requote_uri
 
 
def advance_get(url):
    site= url
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(site,headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page, 'html.parser')
    return soup
 
def olxCrawling(keyword):
    newKeyword = keyword.replace(" ","-")
    url = "https://www.olx.co.id/items/q-"+newKeyword
    raw_html = advance_get(url)
    #print (raw_html)
    # html = BeautifulSoup(raw_html, 'html.parser')

    listing = raw_html
    for listedProd in listing:
        product= {
            # "product_name":listedProd.select("._2tW1I")[0].text,
            # "product_name":listedProd.select("title.text",
            # "url":"https://www.olx.co.id/"+listedProd.find_all('a', href=True)[0]['href'],
            # "description":"",
            # "price":int(re.sub("\D", "",listedProd.select("._89yzn")[0].text.strip()))
        }

    print (listing)
 
def bukalapakCrawling(keyword):
    url = 'https://www.bukalapak.com/products?search%5Bkeywords%5D='+keyword+'&search%5Bsort_by%5D=last_relist_at%3Adesc&search%5Bused%5D=1';
    url = requote_uri(url)
    raw_html = advance_get(url)
    listProd = raw_html.select('.bl-flex-item.mb-8');
    #print(len(listProd))
    for prod in listProd:
        product = {}
        links = prod.select('.bl-link')
        if(len(links)>0):
            href =links[0]['href'] 
            price = prod.select('.bl-text.bl-text--subheading-2.bl-text--semi-bold.bl-text--ellipsis__1')
            product['product_name']=links[0].text.strip()
            product['price']= prod.select('.bl-text.bl-text--subheading-2.bl-text--semi-bold.bl-text--ellipsis__1')[0].text.strip()
            product['url']=href
            product['keyword']=keyword
            product['description']=''
            product['marketplace']='bukalapak'
            product['price'] = int(re.sub("\D", "",product['price']))
            print(product)

if __name__ == "__main__":
    #  bukalapakCrawling("strattos s4")
    olxCrawling("strattos s4")
