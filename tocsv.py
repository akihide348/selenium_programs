#!/usr/bin/env python
# coding: utf-8

# In[174]:


from bs4 import BeautifulSoup
import urllib.request as req
import pandas as pd


# In[175]:


url = "https://b.hatena.ne.jp/hotentry/it"
res = req.urlopen(url)
sp = BeautifulSoup(res, 'html.parser')


# In[176]:


list =[]
url_list = []
oo=sp.find_all('a', class_='js-keyboard-openable',rel='noopener')
for i in oo:
    list.append(i.string)
    url_list.append(i.attrs['href'])
list


# In[177]:


df_title_url = pd.DataFrame({'Title':list, 'URL':url_list})
df_title_url


# In[178]:


df_notnull = df_title_url.dropna(how='any')
df_notnull


# In[179]:


df_notnull.to_csv('hateburo2.csv', encoding='utf-8')


# In[ ]:


# path_w = 'https://docs.google.com/spreadsheets/d/15RXZuUHH79lnzJ_F_W-b9Kyyh2EJqgkzTLE8gspSdVs/edit#gid=1211397768'
# s = '/Users/mac/Dev/selenium_py.hateburo2.csv'

# with open('path_w', 'w') as f:
#     f.write(s)

