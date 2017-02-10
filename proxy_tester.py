# better version
# github.com/yousefissa, twitter @yousefnu

from time import time
from requests import Session

session = Session()
session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36'
                '(KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36'})

def mil_seconds():
    return int(round(time() * 1000))

# MAIN
# gets proxies and websites in a text file, rather than hard-coding them
with open('proxies.txt') as proxies_text, open('sitelist.txt') as sitelist_text:
	proxies = proxies_text.read().splitlines()
	sites = sitelist_text.read().splitlines()

# checks if list is empty
if not proxies:
    print('You did not load proxies. Check your proxies.txt file!')
    exit()
else: 
	print('Currently loaded: {}'.format(proxies))
good_proxies, bad_proxies = [], []

print('Testing on sites ', sites)

def proxyChecker(proxy):
    session.proxies.update({
        'http': 'http://' + proxy,
        'https': 'https://' + proxy
    })
    for url in sites:
        start_time = mil_seconds()
        try:
	        response = session.get(url)
	        if response.status_code != 200:
	            print('{} is not a good proxy.'.format(proxy))
	            bad_proxies.append(proxy)
	        else:
	            print('{} on site {} ---- {} ms'.format(proxy, url, mil_seconds() - start_time))
	            good_proxies.append(proxy)
        except: # broad exceptions are bad but who cares
        	print('Bad Proxy {} on site {}'.format(proxy, url))

if __name__ == '__main__':
	for p in proxies:
		proxyChecker(p)
	good_proxies_set, bad_proxies_set = set(good_proxies), set(bad_proxies)

	with open('proxy_results.txt', 'w') as proxy_results:
		proxy_results.write('Good proxies: \n')
		for proxy in good_proxies_set:
			proxy_results.write(proxy)
		proxy_results.write('Bad proxies: \n')
		for proxy in bad_proxies_set:
			proxy_results.write(proxy)
	print(good_proxies)

