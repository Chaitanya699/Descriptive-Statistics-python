#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Descriptive Statistics with python lib


# In[ ]:


#chaitanya khairnar


# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as pyplot


# In[4]:


ratings_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ST0151EN-SkillsNetwork/labs/teachingratings.csv'
ratings_df=pd.read_csv(ratings_url)


# In[5]:


#WE ARE CHECKING VALUE AND ATRIBUTES OF DATASET
ratings_df.head()


# In[6]:


#HERE WE WILL SE THE ALL DATA TYPE OF AN ATRIBUTE AND ALSO WE CAN SE THE VALUE OF DATASET
ratings_df.info()


# In[7]:


#IT WILL SHOW THE
ratings_df.shape


# In[8]:


#HERE WE ARE CHECKING THE VALUE OF ABOVE  10 LINE 
ratings_df.head(10)


# In[9]:


#WE HAD FIND THE MEAN OF STUDENTS ATTRIBUTES AND ALL BELOW
ratings_df['students'].mean()


# In[10]:


ratings_df['students'].median()


# In[11]:


ratings_df['students'].min()


# In[12]:


ratings_df['students'].max()


# In[13]:


ratings_df.describe()


# In[14]:


#IT WILL PLOT THE HIST FOT BEAUTY ATTRIBUTE
pyplot.hist(ratings_df['beauty'])


# In[15]:


#WE HAD TAKEN THE MEAN STANDARD DAVIATION AND VAR FOR GENDER ATTRIBUTE 
ratings_df.groupby('gender').agg({'beauty':['mean', 'std', 'var']}).reset_index()


# In[16]:


tenure_count = ratings_df[ratings_df.tenure == 'yes'].groupby('gender').agg({'tenure': 'count'}).reset_index()


# In[17]:


tenure_count['percentage'] = 100 * tenure_count.tenure/tenure_count.tenure.sum()
tenure_count


# In[18]:


tenure_count = ratings_df.groupby('minority').agg({'tenure': 'count'}).reset_index()
# Find the percentage
tenure_count['percentage'] = 100 * tenure_count.tenure/tenure_count.tenure.sum()
##print to see
tenure_count


# In[ ]:




