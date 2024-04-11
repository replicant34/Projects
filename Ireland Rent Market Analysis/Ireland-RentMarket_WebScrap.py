#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException


# In[2]:


base_url = 'https://www.daft.ie/property-for-rent/ireland?from='
add_url = '&pageSize=20'
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"
}
current_date = datetime.date.today()
csv_file_path = 'Ireland-RentMarket10.csv'

file = open('Ireland-RentMarket10.csv', 'w', newline='')
writer = csv.writer(file)
writer.writerow(['Address', 'Price', 'Bedrooms', 'Bathrooms', 'Property_type','Date'])

for i in range(0, 1950, 20):
    url = f'{base_url}{i}{add_url}'
    
    page = requests.get(url, headers=headers)
    
    if page.status_code == 200:
        soup1 = BeautifulSoup(page.content, "html.parser")
        soup2 = BeautifulSoup(soup1.prettify())

        addresses = soup2.find_all('h2', {'data-testid': 'address', 'class': 'TitleBlock__Address-sc-1avkvav-8 dzihyY'})
        prices = soup2.find_all('h3', {'class' : "TitleBlock__StyledCustomHeading-sc-1avkvav-5 blbeVq"})
        bedrooms = soup2.find_all('p', {'data-testid' : 'beds'})
        bathrooms = soup2.find_all('p', {'data-testid' : 'baths'})
        property_types = soup2.find_all('p', {'data-testid' : 'property-type'})


        csv_file_path = 'Ireland-RentMarket10.csv'

        file = open('Ireland-RentMarket10.csv', 'a+', newline='')
        writer = csv.writer(file)

        for address, price, bedroom, bathroom, property_type, floor_area in zip(addresses, prices, bedrooms, bathrooms, property_types):
            writer.writerow([address.text, price.text, bedroom.text, bathroom.text, property_type.text, current_date])
        
        print(f"Processed {i} items")
    else:
        print(f"Failed to retrieve data from {url}")


# In[ ]:


browser_driver = Service('/usr/local/bin/chromedriver')

page_to_scrape = webdriver.Chrome(service=browser_driver)
page_to_scrape.get("http://quotes.toscrape.com")

page_to_scrape.find_element(By.LINK_TEXT, "Login").click()

time.sleep(3)


username = page_to_scrape.find_element(By.ID, "username")
password = page_to_scrape.find_element(By.ID, "password")


username.send_keys("admin")
password.send_keys("123")
page_to_scrape.find_element(By.CSS_SELECTOR, "input.btn-primary").click()


file = open("quotes_test4.csv", 'w')
writer = csv.writer(file)
writer.writerow(["Quote", "Author"])


while True:
    quotes = page_to_scrape.find_elements(By.CLASS_NAME, "text")
    authors = page_to_scrape.find_elements(By.CLASS_NAME, "author")
    for quote, author in zip(quotes, authors):
        print(quote.text + "-" + author.text)
        writer.writerow([quote.text, author.text])
    try:
        page_to_scrape.find_element(By.PARTIAL_LINK_TEXT, "Next").click()
    except NoSuchElementException:
        break
        
file.close()

