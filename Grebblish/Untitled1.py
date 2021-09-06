#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install pandas')


# In[1]:


import os
import pandas as pd 
import numpy as np 
import func as fc 


# In[2]:


current_dir=os.getcwd()
print(current_dir)


# In[3]:


full_path_file=current_dir+"/iris.data"
print(full_path_file)


# In[4]:


os.path.isfile(full_path_file)


# In[5]:


full_path=os.path.join(current_dir, "iris.data")
print(full_path)


# In[6]:


def file_exist_or_not(path) :
    
    if os.path.isfile(path) :
        return True 
    else : 
        return False 
    
    


# In[7]:


file_exist_or_not(full_path)


# In[50]:


def read_dataset(path):
    if file_exist_or_not(path)==True:
        df = pd.read_csv(path)
        df.columns=['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
    else :
        return("NON!!!!")
    return(df)


# In[51]:


read_dataset(full_path)


# In[52]:


list=os.listdir()
print(list) 


# In[53]:


results=[file for file in list if file.endswith(".ipynb")]
print(results)
     


# In[55]:


fc.print_fun(9)


# In[8]:


help(fc.print_fun)


# In[ ]:





# In[ ]:




