
# coding: utf-8

# # Practical Statistics for Data Scientists
# ## Exploratory Data Analysis

# This Notebook is the python equivalent of the R code for Chapter-1, from the book <a href="http://shop.oreilly.com/product/0636920048992.do">Practical Statistics for Data Scientists</a> by Peter Bruce and Andrew Bruce. This <a href="https://github.com/andrewgbruce/statistics-for-data-scientists">GitHub</a> repository has the complete R code for the book.
# 
# The authors note that the aim of the book is to be a "Desk Reference" for key Statistical concepts that are relevant to Data Science, explaining their importance and the reason behind that choice.
# 
# Data that is used in the book, has been curated by the authors and made available on <a href="https://drive.google.com/drive/folders/0B98qpkK5EJemYnJ1ajA1ZVJwMzg">Google Drive</a> and <a href="https://www.dropbox.com/sh/clb5aiswr7ar0ci/AABBNwTcTNey2ipoSw_kH5gra?dl=0">Dropbox</a>
# 

# In[69]:

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


from scipy.stats import trim_mean


# In[70]:

# Read the data from a .csv file
stateDataDF = pd.read_csv("../data/state.csv")


# In[71]:

# Check the type of data structure, holding the data
type(stateDataDF)


# In[72]:

# Top 10 rows/records of the data
stateDataDF.head(10)


# In[73]:

# Bottom 10 rows/records of the data
stateDataDF.tail(10)


# In[74]:

# Adding a new column with derived data 
stateDataDF['PopulationInMillions'] = stateDataDF['Population']/1000000


# In[75]:

# Get the data types of feature/attributes in the data
stateDataDF.dtypes


# In[76]:

# Checking the data, ensure column is added
stateDataDF.head(10)


# In[77]:

# Get the summary of numerical data type
# columns in the data
stateDataDF.describe()


# In[78]:

# Rename column heading
stateDataDF.rename(columns={'Murder.Rate': 'MurderRate'}, inplace=True)


# In[79]:

# Get the column headings
list(stateDataDF)


# <br>

# ### Percentile

# In[80]:

# Explore percentiles of Murder Rate,
# 5%, 10%, 25%, 50%, 75% and 95%
murderRatePercentile = stateDataDF.MurderRate.quantile([0.05, 0.1, 0.25, 0.5, 0.75, 0.95])


# In[81]:

print(murderRatePercentile)


# <br>

# ### BoxPlot

# In[82]:

# BoxPlot Population In Millions
fig, ax1 = plt.subplots()
fig.set_size_inches(9,  15)

ax1 = sns.boxplot(x=stateDataDF.PopulationInMillions, orient="v")
ax1.set_ylabel("Population by State in Millions", fontsize=15)
ax1.set_title("Population - BoxPlot", fontsize=20)


# In[83]:

sns.plt.show()


# <br>

# ### Histogram

# In[84]:

# Histogram Population In Millions
fig, ax2 = plt.subplots()
fig.set_size_inches(9,  15)

ax2 = sns.distplot(stateDataDF.PopulationInMillions, kde=False)
ax2.set_ylabel("Frequency", fontsize=15)
ax2.set_xlabel("Population by State in Millions", fontsize=15)
ax2.set_title("Population - Histogram", fontsize=20)


# In[85]:

sns.plt.show()


# <br>

# ### Frequency Table

# Python has a few ways to illustrate a Frequency Table, I have chosen crosstab and groupby. To accomplish this, I added another column to the dataframe that specified bins, to enable me to perform the groupby and crosstab functionality.

# In[86]:

# Perform the binning action, the bins have been
# chosen to accentuate the output for the Frequency Table
stateDataDF['PopulationInMillionsBins'] = pd.cut(stateDataDF.PopulationInMillions, bins=[0, 1, 2, 5, 8, 12, 15, 20, 50])


# In[87]:

stateDataDF


# In[88]:

# One type of Frequency Table
pd.crosstab(stateDataDF.PopulationInMillionsBins, stateDataDF.Abbreviation, margins=True)


# In[89]:

stateDataDF.groupby(stateDataDF.PopulationInMillionsBins)['Abbreviation'].apply(','.join)


# <br>

# ### Density Plot

# In[92]:

# Density Plot - Murder Rate
fig, ax3 = plt.subplots()
fig.set_size_inches(7,  9)

ax3 = sns.distplot(stateDataDF.MurderRate, kde=True)
ax3.set_ylabel("Density", fontsize=15)
ax3.set_xlabel("Murder Rate per Million", fontsize=15)
ax3.set_title("Desnsity Plot - Murder Rate", fontsize=20)


# In[93]:

sns.plt.show()


# In[ ]:



