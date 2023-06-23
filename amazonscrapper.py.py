#!/usr/bin/env python
# coding: utf-8

# In[7]:


import requests
from bs4 import BeautifulSoup

def scrape_amazon(keyword):
    url = f'https://www.amazon.in/s?k={keyword}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    products = soup.find_all('div', {'data-component-type': 's-search-result'})

    results = []
    for product in products:
        name_elem = product.find('span', {'class': 'a-size-medium'})
        price_elem = product.find('span', {'class': 'a-offscreen'})

        if name_elem and price_elem:
            name = name_elem.text.strip()
            price = price_elem.text.strip()
            results.append({'name': name, 'price': price})

    return results

def scrape_walmart(keyword):
    url = f'https://www.walmart.com/search/?query={keyword}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    products = soup.find_all('div', {'class': 'search-result-product-title'})

    results = []
    for product in products:
        name_elem = product.find('a')
        price_elem = product.find_next('span', {'class': 'price-group'})

        if name_elem and price_elem:
            name = name_elem.text.strip()
            price = price_elem.text.strip()
            results.append({'name': name, 'price': price})

    return results

# Example usage
keyword = 'laptop'
amazon_results = scrape_amazon(keyword)
walmart_results = scrape_walmart(keyword)

if not amazon_results:
    print('No results found on Amazon.')
else:
    print('Amazon Results:')
    for result in amazon_results:
        print(result['name'], result['price'])

if not walmart_results:
    print('No results found on Walmart.')
else:
    print('\nWalmart Results:')
    for result in walmart_results:
        print(result['name'], result['price'])


# In[ ]:




