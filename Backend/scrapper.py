from bs4 import BeautifulSoup
import requests

from product_scrapper import amazon_data_scrapper, flipkart_data_scrapper, reliance_data_scrapper

import re
import time
import datetime
import smtplib


product_name = "iphone 12"

def amazon(product):
    print("In amazon function 1")
    URL = amazon_data_scrapper(product)
    print("In amazon function 2")
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    page = requests.get(URL, headers=headers)

    # getting the html content for the website
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    # extracting the details for the html content
    title = soup2.find(id='productTitle').get_text()
#     src = soup2.find("img", id='imgTagWrapperId')
#     src2 = soup.find_all("img", class_ = "imgTagWrapperId")
    src = soup2.find("div", {"id": "imgTagWrapperId"}).img['src']
    price = soup2.find("span",{"class":"a-price-whole"}).get_text()
    rating = soup2.find("span",{"class":"a-icon-alt"}).get_text()

    price = price.strip().replace(',', '')
    price = float(re.findall(r'\d+', price)[0])
    title = title.strip()
    rating = float(rating.strip()[:3])
    
    print(title)
    print(src)
    print(price)
    print(rating)

    return {
        "SiteName": "Amazon Data",
        "ProductLink": URL,
        "ProductTitle": title,
        "ProductPrice": price,
        "ProductRating": rating,
        "ProductSRC": src
    }

# amazon("iphone 12")

def flipkart(product):
    URL = flipkart_data_scrapper(product)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title =  soup2.find("span",{"class":"B_NuCI"}).get_text()
#     images = soup2.findAll('img') 
#     for image in images: 
#         print(image['src'])
    src = soup2.find("div", {"class": "CXW8mj _3nMexc"}).img['src']
    price = soup2.find("div",{"class":"_30jeq3 _16Jk6d"}).get_text()
    rating = soup2.find("div",{"class":"_3LWZlK"}).get_text()
#     delivery = soup2.find("span", {"class": "a-text-bold"}).get_text()

    price = price.strip().replace(',', '')
    price = float(re.findall(r'\d+', price)[0])
    title = title.strip()
    rating = float(rating.strip()[:3])
    src = src.strip()
#     delivery = delivery.strip()
    
    print(title)
    print(src)
    print(price)
    print(rating)
#     print(delivery)

    return {
        "SiteName": "Flipkart Data",
        "ProductLink": URL,
        "ProductTitle": title,
        "ProductPrice": price,
        "ProductRating": rating,
        "ProductSRC": src
    }

# flipkart("iphone 12")

# can be ignored
# def reliance(product):
#     URL = reliance_data_scrapper(product)
#     print(URL)
#     headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
#     page = requests.get(URL, headers=headers)

#     soup1 = BeautifulSoup(page.content, "html.parser")
# #     print(soup1)

#     title =  soup1.find("h1",{"class":"pdp__title"}).get_text()
#     src = soup1.find_all("img", class_ = "img-center pdp__mainHeroImgContainer imgCenter")[0]
#     src = src.get('data-srcset')
#     src = "https://www.reliancedigital.in" +src
#     price = soup1.find("span",{"class":"TextWeb__Text-sc-1cyx778-0 bNdnUu"}).get_text()
#     rating = soup1.find("span",{"class":"TextWeb__Text-sc-1cyx778-0 juAZux"}).get_text()
#     # stars = soup1.find_all("span", class_ = "TextWeb__Text-sc-1cyx778-0 StarRating__StarRatingOuter-sc-1mfqajc-0 bpqZol eOeJGd")[0]
#     # stars = soup1.find_all("span", class_ = "TextWeb__Text-sc-1cyx778-0 StarRating__StarRatingOuter-sc-1mfqajc-0 hEqsYK kTkmZO")[0]
#     # # print(stars)
#     # stars = stars.find_all("i", class_ = "fa fa-star")
# #     delivery = soup2.find("span", {"class": "a-text-bold"}).get_text()

#     price = price.strip()
#     title = title.strip()
#     # rating = rating.strip()
#     src = src.strip()
# #     delivery = delivery.strip()

#     return {
#         "ProductLink": URL,
#         "ProductTitle": title,
#         "ProductPrice": price,
#         "ProductRating": rating,
#         "ProductSRC": src
#     }
    
#     # print(title)
#     # print(src)
#     # print(price)
#     # print(rating)
#     # print(len(stars))
# #     print(delivery)

def reliance(product):
    URL = reliance_data_scrapper(product)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")
#     print(soup1)

    title =  soup1.find("h1",{"class":"pdp__title"}).get_text()
    src = soup1.find_all("img", class_ = "img-center pdp__mainHeroImgContainer imgCenter")[0]
    src = src.get('data-srcset')
    src = "https://www.reliancedigital.in" +src
    price = soup1.find_all("span", class_ = "TextWeb__Text-sc-1cyx778-0")[4].get_text()
    rating = soup1.find_all("span", class_ = "TextWeb__Text-sc-1cyx778-0")[1].get_text()
#     stars = soup1.find("span", class_ = "TextWeb_Text-sc-1cyx778-0 StarRating_StarRatingOuter-sc-1mfqajc-0")
    stars = soup1.find("span", {"class": "StarRating__StarRatingOuter-sc-1mfqajc-0"})
    stars = stars.find_all("i", class_ = "fa fa-star")
#     delivery = soup2.find("span", {"class": "a-text-bold"}).get_text()

    price = price.strip().replace(',', '')
    price = float(re.findall(r"\d+", price)[0])
    title = title.strip()
    rating = rating.strip()
    src = src.strip()
#     delivery = delivery.strip()

    return {
        "SiteName": "Reliance Data",
        "ProductLink": URL,
        "ProductTitle": title,
        "ProductPrice": price,
        "ProductRating": len(stars),
        "ProductSRC": src
    }
    
    # print(title)
    # print(src)
    # print(price)
    # print(rating)
    # print(len(stars))
#     print(delivery)

# reliance(product_name)
