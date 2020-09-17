#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import time
import pandas as pd


# In[2]:


USER = "test_user"
PASS = "test_pw"


# In[3]:


browser = webdriver.Chrome()
browser.implicitly_wait(3)


# In[4]:


url_login = "https://kino-code.com/membership-login/"
browser.get(url_login)
time.sleep(3)
print('ログインページにアクセスしました')


# In[5]:


elem = browser.find_element_by_id('swpm_user_name')
elem.clear()
elem.send_keys(USER)
elem = browser.find_element_by_id('swpm_password')
elem.clear()
elem.send_keys(PASS)
print("フォームを送信")


# In[6]:


browser_form = browser.find_element_by_name('swpm-login')
time.sleep(3)
browser_form.click()
print("情報を入力してログインボタンを押しました")


# In[7]:


url = "https://kino-code.com/member-only/"
time.sleep(1)
browser.get(url)
print(url, 'アクセス完了')


# In[8]:


frm = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/main/article/div/p[2]/button')
time.sleep(1)
frm.click()
print('ダウンロードボタンをクリック')


# In[ ]:




