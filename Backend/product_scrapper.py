import requests
from bs4 import BeautifulSoup

product_name = "iphone 12"  # replace with the actual product name

# all the functions take product name and returns the corresponding url for it from which html content can be 
# extracted

# other comments can be ignored

def amazon_data_scrapper(product_name):
	'''print("--------------------AMAZON-----------------------------------")
	# perform a search on Amazon using the product name as the query
	search_url = f"https://www.amazon.in/s?k={product_name}"
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
	page = requests.get(search_url, headers=headers)

	# parse the search results page using BeautifulSoup
	soup = BeautifulSoup(page.content, "html.parser")

	# extract the URL of the first search result
	# results = soup.find_all("a", class_="a-link-normal")
	# results = soup.findAll('a', {'class': 'a-link-normal s-no-outline'})
	# results = soup.findAll('a', {'class': '_1fQZEK'})
	# results = soup.findAll('a', {'class': 'a-link-normal s-no-outline'})[0]['href']
	# results = soup.findAll('a', {'class': '_1fQZEK'})[0]['href']
	print("Hello Results")
	print(results)
	results = soup.findAll('a', {'class': 'a-link-normal s-no-outline'})[0]['href']
	# results = soup.findAll('a', {'class': '_1fQZEK'})[0]['href']
	
	print(results)
	product_url = "https://www.amazon.in" + results
	return product_url'''
	print("--------------------AMAZON-----------------------------------")
	print(f"Finding for {product_name}")
	search_url = f"https://www.amazon.in/s?k={product_name}"
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
	page = requests.get(search_url, headers=headers)
	print("page Content done")
	# parse the search results page using BeautifulSoup
	soup = BeautifulSoup(page.content, "html.parser")
	# print(soup)
	print("Parsing done")
	# extract the URL of the first search result
	# results = soup.find_all("a", class_="a-link-normal")
	results = soup.findAll('a', {'class': 'a-link-normal s-no-outline'})[0]['href']
	print("results done")
	print(results)
	product_url = "https://www.amazon.in" + results
	return product_url

# amazon_data_scrapper(product_name)


def flipkart_data_scrapper(product_name):
	print("------------------------FLIPKART-----------------------------")
	# perform a search on Amazon using the product name as the query
	search_url = "https://www.flipkart.com/search?q=" + product_name
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
	page = requests.get(search_url, headers=headers)

	# parse the search results page using BeautifulSoup
	soup = BeautifulSoup(page.content, "html.parser")

	# extract the URL of the first search result
	# results = soup.find_all("a", class_="a-link-normal")
	product_url = soup.findAll('a', {'class': '_1fQZEK'})[0]['href']
	print(product_url)
	product_url = "https://www.flipkart.com" + product_url
	return product_url

def reliance_data_scrapper(product_name):
	print("----------------------------Reliance------------------------")
	search_url = f"https://www.reliancedigital.in/search?q={product_name}"
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
	page = requests.get(search_url, headers=headers)
	print(search_url)

	# parse the search results page using BeautifulSoup
	soup = BeautifulSoup(page.content, "html.parser")

	# extract the URL of the first search result
	my_div = soup.find_all('div', class_='sp grid')
	# my_div = my_div.find_all('a')
	href = my_div[0].find_all('a')[0].get("href")
	print(href)
	product_url = "https://www.reliancedigital.in" + href
	return product_url

# reliance_data_scrapper(product_name)
