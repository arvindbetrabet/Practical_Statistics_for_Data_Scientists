
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


from scipy.stats import trim_mean


# In[2]:

# Read the data from a .csv file
stateDataDF = pd.read_csv("../data/state.csv")


# In[3]:

# Check the type of data structure, holding the data
type(stateDataDF)


# In[4]:

# Top 10 rows/records of the data
stateDataDF.head(10)


# In[5]:

# Bottom 10 rows/records of the data
stateDataDF.tail(10)


# In[6]:

# Adding a new column with derived data 
stateDataDF['PopulationInMillions'] = stateDataDF['Population']/1000000


# In[7]:

# Get the data types of feature/attributes in the data
stateDataDF.dtypes


# In[8]:

# Checking the data, ensure column is added
stateDataDF.head(10)


# In[9]:

# Get the summary of numerical data type
# columns in the data
stateDataDF.describe()


# In[10]:

# Rename column heading
stateDataDF.rename(columns={'Murder.Rate': 'MurderRate'}, inplace=True)


# In[11]:

# Get the column headings
list(stateDataDF)


# ### Mean, Trimmed Mean, Weighted Mean, Median and Trimmed Median

# In[12]:

populationMean = stateDataDF.Population.mean()


# In[13]:

print(populationMean)


# In[14]:

# Mean after discarding top and bottom 10% of Population numbers
# eliminating outliers
populationTrimmedMean = trim_mean(stateDataDF.Population, 0.1)


# In[15]:

print(populationTrimmedMean)


# In[16]:

# Weighted mean, in this case, the Murder Rate of a state is weighed based
# on the population of that state and then the mean is taken.
# Compared to the regular mean, where all the values are treated equally
murderRateWeightedMean = np.average(stateDataDF.MurderRate, weights=stateDataDF.Population)


# In[17]:

print(murderRateWeightedMean)


# In[18]:

populationMedian = stateDataDF.Population.median()


# In[19]:

print(populationMedian)


# In[20]:

# Sort the data frame by the Murder Rate values
stateDataDF.sort_values('MurderRate', inplace=True)

# Calculate the Cummulative Sum of the Population
cummulativeSum = stateDataDF.Population.cumsum()

# Find the midpoint of the Sum of Population
midPointCutOff = stateDataDF.Population.sum()/2.0

# The weighted Median is the 0th location index just after
# the Cummulative Sum is greater than or equal to the
# midpoint cut off
murderRateWeightedMedian = stateDataDF.MurderRate[cummulativeSum >= midPointCutOff].iloc[0]


# In[21]:

print(murderRateWeightedMedian)


# In[22]:

# Plot Population In Millions
fig, ax1 = plt.subplots()
fig.set_size_inches(15,  9)


ax1 = sns.barplot(x="State", y="PopulationInMillions", data=stateDataDF.sort_values('MurderRate'), palette="Set2")
ax1.set(xlabel='States', ylabel='Population In Millions')
ax1.set_title('Population in Millions by State', size=20)

plt.xticks(rotation=-90)


# In[23]:

# Plot Population In Millions
fig, ax2 = plt.subplots()
fig.set_size_inches(15,  9)


ax2 = sns.barplot(x="State", y="MurderRate", data=stateDataDF.sort_values('MurderRate', ascending=1), palette="husl")
ax2.set(xlabel='States', ylabel='Murder Rate per 100000')
ax2.set_title('Murder Rate by State', size=20)

plt.xticks(rotation=-90)


# In[24]:

sns.plt.show()


# Although Louisiana is ranked 17 by population (about 4.53M), it has the highest Murder rate of 10.3 per 1M people.

# ### Standard Deviation, Variance, Inter Quartile Range (IRQ), Median Absolute Deviation

# In[28]:

# Standard Deviation of Population
populationSD = stateDataDF.Population.std()


# In[29]:

print(populationSD)


# In[33]:

# Variance of Population
populationVariance = stateDataDF.Population.var()


# In[34]:

print(populationVariance)


# In[30]:

stateDataDF.Population.describe()


# In[31]:

# Inter Quartile Range of Population
populationIRQ = stateDataDF.Population.describe()['75%'] - stateDataDF.Population.describe()['25%']


# In[32]:

print(populationIRQ)


# In[35]:

# Median Absolute Deviation
populationMedianAbsoluteDeviation = stateDataDF.Population.mad()


# In[36]:

print(populationMedianAbsoluteDeviation)


# In[ ]:



