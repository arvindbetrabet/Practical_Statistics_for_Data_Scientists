
# coding: utf-8

# # Practical Statistics for Data Scientists
# ## Exploratory Data Analysis

# This Notebook is the python equivalent of the R code for Chapter-1, from the book <a href="http://shop.oreilly.com/product/0636920048992.do">Practical Statistics for Data Scientists</a> by Peter Bruce and Andrew Bruce. This <a href="https://github.com/andrewgbruce/statistics-for-data-scientists">GitHub</a> repository has the complete R code for the book.
# 
# The authors note that the aim of the book is to be a "Desk Reference" for key Statistical concepts that are relevant to Data Science, explaining their importance and the reason behind that choice.
# 
# Data that is used in the book, has been curated by the authors and made available on <a href="https://drive.google.com/drive/folders/0B98qpkK5EJemYnJ1ajA1ZVJwMzg">Google Drive</a> and <a href="https://www.dropbox.com/sh/clb5aiswr7ar0ci/AABBNwTcTNey2ipoSw_kH5gra?dl=0">Dropbox</a>
# 

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from scipy.stats import kendalltau


# In[2]:


# Read the data from a .csv file
kingCountyTaxDF = pd.read_csv("../data/kc_tax.csv")


# ## Two Numerical Variables
# 
# The authours' opinion is that Scatterplots are good for visualizing a small dataset, but will be too crowded for a large dataset and have suggested Hexabin and Contour plots as alternatives. 

# ### Hexabin Plot

# In[3]:


kingCountyTaxDF.head(10)


# In[4]:


kingCountyTaxDF.describe(include = 'all')


# In[5]:


# Take a subset of the King County, Washington
# Tax data, for Assessed Value for Tax purposes
# < $600,000 and Total Living Sq. Feet > 100 &
# < 2000

kingCountyTaxSubsetDF = kingCountyTaxDF.loc[(kingCountyTaxDF['TaxAssessedValue'] < 600000) & 
                                            (kingCountyTaxDF['SqFtTotLiving'] > 100) & 
                                            (kingCountyTaxDF['SqFtTotLiving'] < 2000)]


# In[6]:


kingCountyTaxSubsetDF.head(10)


# In[7]:


kingCountyTaxSubsetDF.describe(include = 'all')


# In[8]:


# The ZipCode column in the Data Frame
# has a few Null values
kingCountyTaxSubsetDF.info()


# In[9]:


kingCountyTaxSubsetDF['TaxAssessedValue'].isnull().values.any()


# In[10]:



sns.set(style="ticks")



x = kingCountyTaxSubsetDF['SqFtTotLiving']
y = kingCountyTaxSubsetDF['TaxAssessedValue']

fig = sns.jointplot(x, y, kind="hex", stat_func=kendalltau, 
                    color="#4CB391")

fig.fig.subplots_adjust(top=0.85)

fig.set_axis_labels('Total Sq.Ft of Living Space', 'Assessed Value for Tax Purposes')

fig.fig.suptitle('Tax Assessed vs. Total Living Space', size=18);


# <br>

# ### Contour Plot

# In[11]:


fig2 = sns.kdeplot(x, y, legend=True)

plt.xlabel('Total Sq.Ft of Living Space')

plt.ylabel('Assessed Value for Tax Purposes')

fig2.figure.suptitle('Tax Assessed vs. Total Living Space', size=16);


# NOTE: The Contour Plot takes a bit longer to be generated (on a laptop). The lighter greens are the peaks.

# ### Heat Maps
# 
# Heat Map, a 2-D representation of data, where values are expressed with colors and serves as a summary of the data. 

# In[12]:


# Read the data from a .csv file
sp500pxDF = pd.read_csv("../data/sp500_px.csv")


# In[13]:


sp500pxDF.head()


# In[14]:


sp500pxDF.shape


# Using a smaller subset of the larger data frame to use as an example while plotting a Heat Map.

# In[15]:


sp500pxDF_subset = sp500pxDF.iloc[0:15, 6:10]


# In[16]:


sp500pxDF_subset.shape


# In[17]:


ax = sns.heatmap(sp500pxDF_subset)


# Change color and add annotation.

# In[18]:


ax = sns.heatmap(sp500pxDF_subset, cmap='YlGnBu', annot=True)

