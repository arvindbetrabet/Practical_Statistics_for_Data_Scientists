
# coding: utf-8

# # Practical Statistics for Data Scientists
# ## Exploratory Data Analysis

# This Notebook is the python equivalent of the R code for Chapter-1, from the book <a href="http://shop.oreilly.com/product/0636920048992.do">Practical Statistics for Data Scientists</a> by Peter Bruce and Andrew Bruce. This <a href="https://github.com/andrewgbruce/statistics-for-data-scientists">GitHub</a> repository has the complete R code for the book.
# 
# The authors note that the aim of the book is to be a "Desk Reference" for key Statistical concepts that are relevant to Data Science, explaining their importance and the reason behind that choice.
# 
# Data that is used in the book, has been curated by the authors and made available on <a href="https://drive.google.com/drive/folders/0B98qpkK5EJemYnJ1ajA1ZVJwMzg">Google Drive</a> and <a href="https://www.dropbox.com/sh/clb5aiswr7ar0ci/AABBNwTcTNey2ipoSw_kH5gra?dl=0">Dropbox</a>
# 

# In[19]:

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from scipy.stats import kendalltau


# In[20]:

# Read the data from a .csv file
kingCountyTaxDF = pd.read_csv("../data/kc_tax.csv")


# ### Two Numerical Variables - Hexabin Plot

# In[21]:

kingCountyTaxDF.head(10)


# In[22]:

kingCountyTaxDF.describe(include = 'all')


# In[23]:

# Take a subset of the King County, Washington
# Tax data, for Assessed Value for Tax purposes
# < $750,000 and Total Living Sq. Feet > 100 &
# < 3500

kingCountyTaxSubsetDF = kingCountyTaxDF.loc[(kingCountyTaxDF['TaxAssessedValue'] < 600000) & 
                                            (kingCountyTaxDF['SqFtTotLiving'] > 100) & 
                                            (kingCountyTaxDF['SqFtTotLiving'] < 2000)]


# In[24]:

kingCountyTaxSubsetDF.head(10)


# In[25]:

kingCountyTaxSubsetDF.describe(include = 'all')


# In[26]:

# The ZipCode column in the Data Frame
# has a few Null values
kingCountyTaxSubsetDF.info()


# In[27]:

kingCountyTaxSubsetDF['TaxAssessedValue'].isnull().values.any()


# In[28]:


sns.set(style="ticks")



x = kingCountyTaxSubsetDF['SqFtTotLiving']
y = kingCountyTaxSubsetDF['TaxAssessedValue']

fig = sns.jointplot(x, y, kind="hex", stat_func=kendalltau, 
                    color="#4CB391")

fig.set_axis_labels('Total Sq.Ft of Living Space', 'Assessed Value for Tax Purposes')


# In[29]:


plt.subplots_adjust(top=0.85)

plt.suptitle('Tax Assessed vs. Total Living Space', size=18)
plt.show()


# <br>

# ### Contour Plot

# In[35]:

fig2 = sns.kdeplot(x, y, legend=True)


# In[36]:

plt.subplots_adjust(top=0.85)

plt.suptitle('Tax Assessed vs. Total Living Space', size=18)

plt.xlabel('Total Sq.Ft of Living Space')
plt.ylabel('Assessed Value for Tax Purposes')

plt.show()


# NOTE: The Contour Plot takes a bit longer to be generated (on a laptop). The lighter greens are the peaks.
