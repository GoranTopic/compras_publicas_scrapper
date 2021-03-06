import requests
from lxml.html import fromstring

proxies = set()

def get_proxies(count=10):
    #'https://free-proxy-list.net/'
    #proxies.update(from_free_proxy_list(count))
    '''
    #get free proxies from website
    if(len(proxies) < count):
        #'https://advanced.name/freeproxy'
        proxies.update(advanced_free_proxy(
            count - len(proxies) 
            ))
    '''
    '''
    # get proxies form free txt file
    if(len(proxies) < count):
        proxies.update(
                read_proxi_from_file(
                    'assets/proxy_list/Free proxies.txt', 
                    count - len(proxies)))
        '''
    # get proxies from paid proxy scrape
    if(len(proxies) < count):
        proxies.update(
                read_proxi_from_file(
                    'assets/proxy_list/proxyscrape_premium_http_proxies.txt', 
                    count - len(proxies)))
    return proxies

def from_free_proxy_list(count):
    # this website provides about 21 free proxies
    url = 'https://free-proxy-list.net/'
    prev_proxy_len = -1
    proxies = set()
    while(prev_proxy_len < len(proxies)):
        response = requests.get(url)
        parser = fromstring(response.text)
        print(f"grabbing proxies: {len(proxies)} out of {count}");
        for i in parser.xpath('//tbody/tr'):
            if i.xpath('.//td[7][contains(text(),"yes")]'):
                # Grabbing IP and corresponding PORT
                proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
                proxies.add(proxy)
        prev_proxy_len = len(proxies)
    return proxies

def advanced_free_proxy(count):
    url = 'https://advanced.name/freeproxy/6255013b47ba6'
    response = requests.get(url)
    proxies = set()
    # = fromstring(response.text)
    print(type(response.text))
    for line in response.text.splitlines():
        proxies.add(line)
        if len(proxies) < count:
            break
    return proxies

def read_proxi_from_file(filename, count):
    # Using readlines()
    file = open(filename, 'r')
    lines = file.readlines();
    proxies = set()
    count = 0
    # Strips the newline character
    for line in lines:
        proxies.add(line.strip())
        if len(proxies) < count:
            break
    return proxies
