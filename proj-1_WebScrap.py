#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from bs4 import BeautifulSoup
import requests
import datetime
import csv


# In[ ]:


base_url = 'https://www.*aft.ie/property-for-sale/ireland?from='
add_url = '&pageSize=20'
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"
}
current_date = datetime.date.today()
csv_file_path = 'Daft101.csv'

header = ['Address', 'Price', 'Bedrooms', 'Bathrooms', 'Property_type', 'Floor_area','Date']
file = open('Daft_101.csv', 'w', newline='', encoding='UTF8')
writer = csv.writer(file)
writer.writerow(['Address', 'Price', 'Bedrooms', 'Bathrooms', 'Property_type', 'Floor_area','Date'])

for i in range(0, 13361, 20):
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
        floor_areas = soup2.find_all('p', {'data-testid': 'floor-area'})


        csv_file_path = 'Daft101.csv'

        file = open('Daft101.csv', 'a+', newline='')
        writer = csv.writer(file)

        for address, price, bedroom, bathroom, property_type, floor_area in zip(addresses, prices, bedrooms, bathrooms, property_types, floor_areas):
            writer.writerow([address.text, price.text, bedroom.text, bathroom.text, property_type.text, floor_area.text, current_date])
        
        print(f"Processed {i} items")
    else:
        print(f"Failed to retrieve data from {url}")

