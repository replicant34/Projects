#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime


# In[2]:


url = 'https://www.daft.ie/for-rent/house-86-waterloo-lane-ballsbridge-dublin-4/5516615'
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"}
page = requests.get(url, headers = headers)
soup1 = BeautifulSoup(page.content, "html.parser")
soup2 = BeautifulSoup(soup1.prettify())
address = soup2.find('h1', {'data-testid': 'address', 'class': 'TitleBlock__Address-sc-1avkvav-8 dzihxK'}).get_text()
price = soup2.find('h2', {'class' : "TitleBlock__StyledCustomHeading-sc-1avkvav-5 blbeVq"}).get_text()
bedroom = soup2.find('p', {'data-testid' : 'beds', 'class': "TitleBlock__CardInfoItem-sc-1avkvav-9 fgXVWJ"}).get_text()
bathroom = soup2.find('p', {'data-testid' : 'baths', 'class': "TitleBlock__CardInfoItem-sc-1avkvav-9 fgXVWJ"}).get_text()
property_type = soup2.find('p', {'data-testid' : 'property-type', 'class': "TitleBlock__CardInfoItem-sc-1avkvav-9 cKZYAr"}).get_text()

print(address)
print(price)
print(bedroom)
print(bathroom)
print(property_type)


# In[3]:


address = address.strip()
price = price.strip()[1:7]
bedroom = bedroom.strip()
bathroom = bathroom.strip()
property_type = property_type.strip()

print(address)
print(price)
print(bedroom)
print(bathroom)
print(property_type)


# In[4]:


import datetime
current_date = datetime.date.today()
print(current_date)


# In[5]:


import csv
header = ['Address', 'Price', 'Bedrooms', 'Bathrooms', 'Type', 'Date']
data = [address, price, bedroom, bathroom, property_type, current_date]
with open('Daft_Dataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


# In[6]:


import pandas as pd
df = pd.read_csv(r'/Users/iliagrishkin/Daft_dataset.csv')
print(df)


# In[7]:


with open('Daft_Dataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[26]:


def track_price():
    url = 'https://www.daft.ie/for-rent/house-86-waterloo-lane-ballsbridge-dublin-4/5516615'
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"}
    page = requests.get(url, headers = headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify())
    address = soup2.find('h1', {'data-testid': 'address', 'class': 'TitleBlock__Address-sc-1avkvav-8 dzihxK'}).get_text()
    price = soup2.find('h2', {'class' : "TitleBlock__StyledCustomHeading-sc-1avkvav-5 blbeVq"}).get_text()
    bedroom = soup2.find('p', {'data-testid' : 'beds', 'class': "TitleBlock__CardInfoItem-sc-1avkvav-9 fgXVWJ"}).get_text()
    bathroom = soup2.find('p', {'data-testid' : 'baths', 'class': "TitleBlock__CardInfoItem-sc-1avkvav-9 fgXVWJ"}).get_text()
    property_type = soup2.find('p', {'data-testid' : 'property-type', 'class': "TitleBlock__CardInfoItem-sc-1avkvav-9 cKZYAr"}).get_text()
    address = address.strip()
    price = price.strip()[1:7]
    bedroom = bedroom.strip()
    bathroom = bathroom.strip()
    property_type = property_type.strip()
    import datetime
    current_date = datetime.date.today()
    import csv
    header = ['Address', 'Price', 'Bedrooms', 'Bathrooms', 'Type', 'Date']
    data = [address, price, bedroom, bathroom, property_type, current_date]
    with open('Daft_Dataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    if (price < 3600):
        send_email()


# In[ ]:


while(True):
    track_price()
    time.sleep(86400)


# In[ ]:


import pandas as pd
df = pd.read_csv(r'/Users/iliagrishkin/Daft_dataset.csv')
print(df)


# In[11]:


def send_email():
    from email.message import EmailMessage
    import ssl
    import smtplib

    email_sender = 'replicant0034@gmail.com'
    email_password = 'xxxxxxxxxxxxxxxxxxx'
    email_reciever = 'replicant0034@gmail.com'

    subject = "The price" address "has changed"
    body = """
    Check on 
     """
    url

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_reciever
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciever, em.as_string() )

