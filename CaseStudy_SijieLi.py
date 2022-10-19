#!/usr/bin/env python
# coding: utf-8

# # Case Study
# # Sijie Li

# ## 1. Initial Data Preparation

# In[ ]:


get_ipython().system('pip install yfinance')


# In[2]:


import yfinance as yf


# In[1]:


stock_list = ['SPY', 'AGG', 'F', 'GM', 'UBER','TSLA','GOOG',
'SNAP',
'VOW3.DE',
'EXSA.DE',
'EURUSD=X',
'EURUSD=F',
'GD=F',
'DB',
'ABB']
print('stock_list:', stock_list)


# In[3]:


data = yf.download(stock_list, start="2015-12-31", end="2021-12-31",interval = "1wk")
print('data fields downloaded:', set(data.columns.get_level_values(0)))
data


# ### Prompt 2: Data wrangling

# In[4]:


import pandas as pd
import os
import csv


# In[5]:


data['Adj Close'].head()


# In[7]:


data2 = pd.DataFrame(data['Adj Close'])
data2.dropna(how='all', axis=1, inplace=True)


# In[8]:


data2.head()


# In[9]:


data2.to_csv(r'C:\Users\sijie.li\stocklist3.csv', sep='\t', index=True,header=True)


# In[ ]:




