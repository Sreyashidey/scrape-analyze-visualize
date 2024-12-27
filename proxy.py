import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException


proxy_url = "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt"


def get_proxies(url):
    r = requests.get(url)
    proxies = r.text.splitlines() 
    return proxies


def test_proxy(proxy):
    url = "https://www.google.com"  
    proxies = {
        "http": proxy,
        "https": proxy,
    }
    try:
        response = requests.get(url, proxies=proxies, timeout=5)
        if response.status_code == 200:
            return True
    except RequestException:
        return False

def get_working_proxies(proxy_url):
    proxies = get_proxies(proxy_url)
    working_proxies = []

    for proxy in proxies:
        if test_proxy(proxy):
            print(f"Working proxy: {proxy}")
            working_proxies.append(proxy)

    return working_proxies

# Run the function and get working proxies
working_proxies = get_working_proxies(proxy_url)

# Print out all working proxies
print(f"Total working proxies: {len(working_proxies)}")
for proxy in working_proxies:
    print(proxy)
