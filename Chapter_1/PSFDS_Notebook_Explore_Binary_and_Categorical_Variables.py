
# coding: utf-8

# # Practical Statistics for Data Scientists
# ## Exploratory Data Analysis

# This Notebook is the python equivalent of the R code for Chapter-1, from the book <a href="http://shop.oreilly.com/product/0636920048992.do">Practical Statistics for Data Scientists</a> by Peter Bruce and Andrew Bruce. This <a href="https://github.com/andrewgbruce/statistics-for-data-scientists">GitHub</a> repository has the complete R code for the book.
# 
# The authors note that the aim of the book is to be a "Desk Reference" for key Statistical concepts that are relevant to Data Science, explaining their importance and the reason behind that choice.
# 
# Data that is used in the book, has been curated by the authors and made available on <a href="https://drive.google.com/drive/folders/0B98qpkK5EJemYnJ1ajA1ZVJwMzg">Google Drive</a> and <a href="https://www.dropbox.com/sh/clb5aiswr7ar0ci/AABBNwTcTNey2ipoSw_kH5gra?dl=0">Dropbox</a>
# 

# In[2]:

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


from scipy.stats import trim_mean


# In[3]:

# Read the data from a .csv file
airlineDelaysDF = pd.read_csv("../data/dfw_airline.csv")


# A variable is considered to be categorical, if each observation belongs to one of a set of distinct categories. Weather forecast describing cloud cover (with categories cloudy, partly cloudy, sunny) or a person's birth continent (with categories Africa, America, Antartica, Asia, Australia, Europe) are a couple of examples.
# 
# However, in certain applications, each observation is binary - that is having one of two possible outcomes.
# 
# Example:
# A person may
# <ul style="margin-left:15px;">
#             <li>accept or decline, an offer from a bank for a credit card</li>
#             <li>opt-in or opt-out, of health insurance</li>
#             <li>vote yes or no in a bond-election, to provide additional funds for city development</li>
# </ul>

# ### BarPlot - Categorical Variables

# In[4]:

airlineDelaysDF.head(10)


# In[5]:

headerList = []
headerList = list(airlineDelaysDF)


# In[6]:

flightDelays =[]
flightDelays = airlineDelaysDF.values.tolist()[0]


# In[7]:

myScale = 6 #change the scale of the flight delays
scaledFlightDelay = [i/myScale for i in flightDelays]


# In[10]:

y_pos = np.arange(len(headerList))

plt.figure(figsize=(10, 8))

plt.bar(y_pos, scaledFlightDelay, align='center', alpha=0.5)
plt.xticks(y_pos,headerList )
plt.xlabel('Delay Causes', fontsize=14)
plt.ylabel('Delays scaled down 1/6th', fontsize=14)
plt.title('Bar Plot: Cause of Airline Delays at DFW, since 2010', fontsize=18)
 
plt.show()


# ### NOTE

# The Authors have briefly touched on <b>Mode</b> and <b>Expected Value</b> in the book.
# 
# If the distribution has a single mound or peak, the distribution is called unimodal, and the value that occurs most often is called the mode.

# Expected value is the sum of values times their probability of occurrence, often used to sum up factor variable levels.
