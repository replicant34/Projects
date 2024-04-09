#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

csv_file_path = 'Daft101.csv'
df = pd.read_csv(csv_file_path)

duplicate_rows = df[df.duplicated()]
num_duplicates = len(duplicate_rows)

if num_duplicates > 0:
    print(f"Found {num_duplicates} duplicate rows:")
    print(duplicate_rows)
else:
    print("No duplicate rows found.")


# In[ ]:


def empty_space(input_file, output_file):
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            cleaned_row = [cell.strip() if cell else cell for cell in row]
            writer.writerow(cleaned_row)

input_csv_file = 'Daft101.csv'
output_csv_file = 'Daft103.csv'

empty_space(input_csv_file, output_csv_file)


# In[ ]:


import re

df = pd.read_csv('Daft102.csv')

county_pattern = re.compile(r'Co\.\s\w+')

def extract_county(address):
    county_match = re.search(county_pattern, address)
    return county_match.group() if county_match else None

df['County'] = df['Address'].apply(extract_county)

df.to_csv('Daft104.csv', index=False)


# In[ ]:


df = pd.read_csv('Daft104.csv')

df['County'].fillna('Dublin', inplace=True)

df.to_csv('Daft105.csv', index=False)


# In[ ]:


df = pd.read_csv('Daft107.csv')

df['Bedrooms'] = df['Bedrooms'].str.extract('(\d+)', expand=False)
df['Bathrooms'] = df['Bathrooms'].str.extract('(\d+)', expand=False)

df['Bedrooms'] = pd.to_numeric(df['Bedrooms'], errors='coerce')
df['Bathrooms'] = pd.to_numeric(df['Bathrooms'], errors='coerce')

df.to_csv('Daft112.csv', index=False)


# In[ ]:


df = pd.read_csv('Daft106.csv')

df = df[df['Price'].str.isnumeric()]

df['Price'] = df['Price'].replace('[\$,]', '', regex=True).astype(float)

df.to_csv('Daft107.csv', index=False)


# In[ ]:


df = pd.read_csv('Daft112.csv')

zip_pattern = re.compile(r'\b([A-Z\d]+)\b')

def extract_zip(address):
    zip_match = re.search(zip_pattern, address)
    return zip_match.group(1) if zip_match else None

df['Zipcode'] = df['Address'].apply(extract_zip)

df.to_csv('Daft115.csv', index=False)


# In[ ]:




