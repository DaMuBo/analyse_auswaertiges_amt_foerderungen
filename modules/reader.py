import requests
from bs4 import BeautifulSoup
import sys
from random import choice

# Nehme einen zufälligen HTML Reader um die Daten abzurufen.
def randomheader():
    desktop_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0']
    return {'User-Agent': choice(desktop_agents), 
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
        'Accept-Language' : 'en-US,en;q=0.5',
        'Accept-Encoding' : 'gzip', 
        'DNT' : '1', # Do Not Track Request Header 
        'Connection' : 'close'
        }
#Lese die HTML Daten mit einer Funktion ein die prüft ob die Daten richtig zurück gegeben werden
def htmlreader(url,header, proxys=None):
    session = requests.session()
    session.headers = header
    if proxys == None:
        response = session.get(url)
    else:
        try:
            response = session.get(url, proxies=proxys)
        except:
            return -2
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        return soup
    else:
        return -1
    
# Definiere eine Funktion die den HTML Text nach bestimmten Werten durchsucht und diese zurückgibt, wenn er welche findet.
def finder(values,otype,definer=None):
    if definer == None:
        if values.find(otype):
            return values.find(otype).get_text().strip()
        else:
            return -1
    else:
        if values.find(otype,definer):
            return values.find(otype,definer).get_text().strip()
        else:
            return -1
        
# Wähle einen zufälligen Proxy aus über den die Daten abgerufen werden
def proxysampler(url,header):
    session = requests.session()
    session.headers = header
    response = session.get(url)
    soup = BeautifulSoup(response.content, 'html5lib')
    liste = list(zip(map(lambda x:x.text, soup.findAll('td')[::8]), map(lambda x:x.text,
                                                                          soup.findAll('td')[1::8])))
    liste = list(map(lambda x:x[0]+':'+x[1], liste))
    proxy = {'https':choice(liste)}
    return proxy

def reader_one()