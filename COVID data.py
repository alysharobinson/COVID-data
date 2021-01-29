#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing
import pandas as pd
import requests


# In[2]:


#Collecting Data by Parsing
url = 'https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data'
r = requests.get(url)
data_list = pd.read_html(r.text)
a_df = data_list[0]


# In[3]:


#Creating Columns 
a_df.columns = ['Col0','Country Name','Total Cases','Total Deaths','Total Recoveries','Col5']


# In[4]:


#Getting rid of unneeded columns
a_df = a_df[['Country Name','Total Cases','Total Deaths','Total Recoveries']]


# In[5]:


#Getting rid of unneeded rows
last_idx = a_df.index[-1]
a_df = a_df.drop([last_idx, last_idx-1])


# In[6]:


#Getting rid of brackets around Country names
a_df['Country Name'] = a_df['Country Name'].str.replace('\[.*\]','')


# In[7]:


#Getting rid of data in last column
a_df['Total Cases'] = a_df['Total Cases'].str.replace('No data','0')
a_df['Total Deaths'] = a_df['Total Deaths'].str.replace('No data','0')
a_df['Total Recoveries'] = a_df['Total Recoveries'].str.replace('No data','0')


# In[8]:


#Change data type to numeric (except 60+)
a_df['Total Cases'] = pd.to_numeric(a_df['Total Cases'])
a_df['Total Deaths'] = pd.to_numeric(a_df['Total Deaths'])
a_df['Total Recoveries'] = pd.to_numeric(a_df['Total Recoveries'])


# In[10]:


#Export data to Excel Sheet
a_df.to_excel(r'covid19_dataset.xlsx')


# In[ ]:




