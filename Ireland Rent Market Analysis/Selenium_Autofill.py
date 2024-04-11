#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import re


# In[ ]:


# Data to sing in
password_daft = "*******************"
username_daft = "*******************"

# Connect
browser_driver = Service('/usr/local/bin/chromedriver')
page_to_fill = webdriver.Chrome(service=browser_driver)
page_to_fill.get("https://www.**ft.ie/for-rent/studio-apartment-flat-3-55-richmond-street-south-dublin-2/5527162")

time.sleep(2)

# Agree cookies
page_to_fill.find_element(By.ID, "didomi-notice-agree-button").click()

# Get address
address = page_to_fill.find_element(By.CSS_SELECTOR, 'h1[data-testid="address"]')
address = address.text

time.sleep(2)
# Click email
page_to_fill.find_element(By.XPATH, "//button[@data-testid='message-btn']").click()

time.sleep(2)

# Fill sign in form
username = page_to_fill.find_element(By.ID, "username")
password = page_to_fill.find_element(By.ID, "password")
username.send_keys(username_daft)
password.send_keys(password_daft)

page_to_fill.find_element(By.ID, "login").click()

time.sleep(2)

# Locate elements for second form
form_input_fname_xpath = "//input[@name='firstName']"
form_input_lname_xpath = "//input[@name='lastName']"
form_input_email_xpath = "//input[@name='email']"
form_input_phone_xpath = "//input[@name='phone']"
form_input_message_xpath = "//textarea[@name='message']"
form_select_adults_xpath = "//button[@data-testid='adultTenants-increment-button']"
form_select_pets_xpath = "//input[@data-testid='hasPets-item-1']"
form_input_date_xpath = "//input[@data-testid='datetime-picker-input']"
form_submit_button_xpath = "//button[@aria-label='Send']"
form_close_button_xpath = "//button[@class='styles__CloseContainer-qea560-6 jqmvRi']"

# Wait for form elements to be present
page_to_fill.implicitly_wait(10)

# Data for the form
fname = "****"
lname = "**********"
email = "*************93@gmail.com"
phone = "+35385264****"
text = "Dear Sir/Madam, I hope this message finds you well. My name is ****, and I am writing to express my sincere interest in renting the apartment you have available at {}."
message = text.format(address)
date = "02/01/2024"

# Fill in the form
page_to_fill.find_element(By.XPATH, form_input_fname_xpath).send_keys(fname)
page_to_fill.find_element(By.XPATH, form_input_lname_xpath).send_keys(lname)
page_to_fill.find_element(By.XPATH, form_input_email_xpath).send_keys(email)
page_to_fill.find_element(By.XPATH, form_input_phone_xpath).send_keys(phone)
page_to_fill.find_element(By.XPATH, form_input_message_xpath).send_keys(message)
page_to_fill.find_element(By.XPATH, form_input_date_xpath).send_keys(date)

adults_button = page_to_fill.find_element(By.XPATH, form_select_adults_xpath)
adults_button.click()

pets_button = page_to_fill.find_element(By.XPATH, form_select_pets_xpath)
pets_button.click()

# Submit the form
submit_button = page_to_fill.find_element(By.XPATH, form_submit_button_xpath)
submit_button.click()

close_button = page_to_fill.find_element(By.XPATH, form_close_button_xpath)
close_button.click()

