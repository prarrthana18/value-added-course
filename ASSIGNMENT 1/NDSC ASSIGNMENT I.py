#!/usr/bin/env python
# coding: utf-8

# In[8]:


pip install bs4


# In[9]:


pip install requests


# In[10]:


from bs4 import BeautifulSoup


# In[11]:


import requests


# In[12]:


url="https://www.flipkart.com/laptops/pr?sid=6bo,b5g&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_fc219fa9-9236-432f-8a9e-c6021a4454cb_1_372UD5BXDFYS_MC.34WHNYFH5V2Y&otracker=hp_rich_navigation_8_1.navigationCard.RICH_NAVIGATION_Electronics~Laptop%2Band%2BDesktop_34WHNYFH5V2Y&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_8_L1_view-all&cid=34WHNYFH5V2Y"


# In[13]:


url


# In[14]:


Website_Allow=requests.get(url)


# In[15]:


Website_Allow


# In[16]:


soup=BeautifulSoup(Website_Allow.text)


# In[17]:


soup


# In[19]:


lap=soup.select("._4rR01T")


# In[20]:


lap


# In[21]:


lap_list=[]


# In[22]:


import time


# In[23]:


for i in lap:
    lap_name=i.text
    lap_list.append(i.text)
    print(lap_list)
    time.sleep(2)


# In[24]:


lap_list


# In[25]:


rating=soup.select("._1lRcqv ._3LWZlK")


# In[26]:


rating


# In[27]:


rate=[]


# In[28]:


for j in rating:
    rate.append(j.text)


# In[29]:


rate


# In[30]:


price=soup.select("._1_WHN1")


# In[31]:


price


# In[32]:


prices=[]


# In[33]:


for k in price:
    prices.append(k.text)


# In[34]:


prices


# In[35]:


rev=soup.select("._13vcmD+ span")


# In[36]:


rev


# In[37]:


reviews=[]


# In[38]:


for l in rev:
    reviews.append(l.text)


# In[39]:


reviews


# In[40]:


import pandas as pd


# In[41]:


dataset=pd.DataFrame(lap,columns=['Prod_name'])


# In[42]:


dataset


# In[43]:


dataset['Price']= prices


# In[44]:


dataset


# In[45]:


dataset['Prod_Rate']=rate


# In[46]:


dataset


# In[47]:


dataset['Reviews']=reviews


# In[48]:


dataset


# In[ ]:





# In[49]:


import pandas as pd


# In[50]:


dataset.to_csv("NDSC ASSIGNMENT I.csv")


# In[51]:


dataset1=dataset


# In[52]:


if '__name__'=='__main__':
    dataset1=pd.read_csv("NDCS ASSIGNMENT I.csv")
    print(dataset1)
    print(type( dataset1))
  
dataset1[' Reviews']= dataset1['Reviews'].str.replace(r'\W',"")      
print(dataset1)


# In[53]:


dataset1[' Prod_name']= dataset1['Prod_name'].str.replace(r'\W',"")      
print(dataset1)


# In[ ]:





# In[54]:


dataset1['Price']= dataset1['Price'].str.replace(r'\W',"")      
print(dataset1)


# In[55]:


dataset1['Prod_Rate']= dataset1['Prod_Rate'].str.replace(r'\W',"")      
print(dataset1)


# In[56]:


dataset1['Prod_name']=dataset1['Prod_name'].str.replace("Windows1... ","")
print(dataset1)


# In[57]:


dataset1['Prod_name']=dataset1['Prod_name'].str.replace("Windows1... ","")
print(dataset1)


# In[58]:


dataset1['Reviews']=dataset1['Reviews'].str.replace("Reviews","")
print(dataset1)


# In[60]:


dataset1['Prod_name']= dataset1['Prod_name'].str.replace("8 GB/256 GB SSD/Windows...","")      
print(dataset1)


# In[61]:


dataset1['Prod_name']= dataset1['Prod_name'].str.replace(" (Home) 14s- dy2506TU Th...","")      
print(dataset1)


# In[1]:


import pandas as pd
import numpy as np


# In[2]:


dataset=pd.read_csv("NDSC ASSIGNMENT I.csv")


# In[3]:


dataset


# In[4]:


x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,:-1].values


# In[5]:


x


# In[6]:


y


# ## Finding null values

# In[7]:


dataset.isnull().sum()


# In[9]:


import pandas as pd


# In[19]:


dataset1=pd.read_csv("NDSC ASSIGNMENT I.csv")


# In[20]:


dataset1


# In[21]:


dataset1.Prod_Rate.unique()


# In[22]:


order=[4.4, 4.3, 3.8, 4.5, 4.2, 4. , 4.1]


# In[23]:


order


# In[ ]:





# In[35]:


import pandas as pd


# In[36]:


from sklearn.preprocessing import LabelEncoder


# In[29]:


dataset1=pd.DataFrame(dataset1)


# In[30]:


dataset1


# In[37]:


lab_encode=LabelEncoder()


# In[38]:


dataset1['Prod_Rate']=lab_encode.fit_transform(dataset1['Prod_Rate'])


# In[39]:


dataset1


# In[40]:


dataset1['Reviews']=lab_encode.fit_transform(dataset1['Reviews'])


# In[41]:


dataset1


# ## Scaling

# In[42]:


dataset1.plot.kde()

