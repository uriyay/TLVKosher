#!/usr/bin/python3
'''
This script will download all of Kosher places names in Tel Aviv and save it to a TXT file
'''
import sys
import os
import urllib.request
from bs4 import BeautifulSoup

URL = 'https://rabanut.co.il/%d7%97%d7%99%d7%a4%d7%95%d7%a9-%d7%a2%d7%a1%d7%a7%d7%99%d7%9d-%d7%9b%d7%a9%d7%a8%d7%99%d7%9d/'
TARGET_PATH = 'resturants_names.txt'

def download_url(url):
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}

    req = urllib.request.Request(url, headers=hdr)
    page = urllib.request.urlopen(req)
    html = page.read().decode()
    return html

def get_rests_names(html):
    soup = BeautifulSoup(html)
    options = soup.find_all(attrs=dict(name='business_id'))
    assert len(options) == 1, 'should be one result!'
    options = options[0]
    result = [x.text for x in options.children if hasattr(x, 'text')]
    return result

def main(path=TARGET_PATH):
    html = download_url(URL)
    #parse it
    names = get_rests_names(html)
    with open(path, 'w') as fp:
        fp.write('\n'.join(names))

if __name__ == '__main__':
    main(*sys.argv[1:])
