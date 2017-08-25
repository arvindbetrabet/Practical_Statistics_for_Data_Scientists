
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


# <br>

# ### Correlation

# When the data points follow a roughly straight-line trend, the variables are said to have an approximately linear relationship. In some cases, the data points fall close to a straight line, but more often there is quite a bit of variability of the points around the straight-line trend. A summary measure called the correlation describes the strength of the linear association.
# 
# Correlation summarizes the strength and direction of the linear (straight-line) association between two quantitative variables. Denoted by r, it takes values between -1 and +1.
# <ul>
# <li>A positive value for r indicates a positive association, and a negative value for r indicates a negative association.</li>
# <li>The <b>closer r is to 1</b> the closer the data points fall to a straight line, thus the linear association is <b>stronger.</b> The <b>closer r is to 0</b>, making the linear association <b>weaker</b>.</li>
# </ul>

# In[2]:

# Read the S&P 500 data from a .csv file
sp500DailyReturns = pd.read_csv("../data/sp500_px.csv") # S&P 500 Daily Returns
sp500Symbols = pd.read_csv("../data/sp500_sym.csv")# Selected S&P Symbols


# In[3]:

sp500ETFSymbols = pd.DataFrame()


# In[4]:

sp500ETFSymbols = sp500Symbols.loc[sp500Symbols['sector'] == 'etf', ['symbol']]


# In[5]:

print(sp500ETFSymbols)


# In[6]:

sp500DailyReturns.head(10)


# In[7]:

newSP500DF = sp500DailyReturns.loc[sp500DailyReturns['Unnamed: 0'] > '2012-07-01', sp500ETFSymbols["symbol"].values]


# In[8]:

newSP500DF.head(10)


# In[9]:

corrSP500 = newSP500DF.corr()


# ### Correlation Matrix

# In[10]:

print(corrSP500)


# <br>

# ### Correlation Plot

# In[11]:

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

ax.set_label("Correlation Coefficient")
ax.set_title("Correlation between ETF returns")

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)


# In[12]:

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corrSP500, cmap=cmap, vmax= 1, vmin=-1, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5, "label": 'Correlation Coefficient'})


# In[13]:

plt.show()


# <br>

# ### Scatter Plot

# A Scatter Plot is a common and easy way to display the relation between two numeric-variables x and y.
# 
# A scatter plot indicates the <b>direction of a relationship</b> between the variables. Articulation of direction develops when there is either:
# <ul>
# <li>High values of one variable occurring with high values of the other variable or low values of one variable occurring
# with low values of the other variable.</li>
# 
# <li>High values of one variable occurring with low values of the other variable.</li>
# </ul>
# 
# The <b>strength of the relationship</b> can be gauged by looking at the scatter plot and seeing how close the points are to a line.
# 
# A scatterplot can reveal, the <b>overall pattern</b> and any <b>deviations</b> from the pattern, when observed correctly.

# In[14]:


area = np.pi*10

plt.figure(figsize=(10, 8))

# Plot
plt.scatter(sp500DailyReturns.RTN, sp500DailyReturns.GD, s=area, alpha=0.5)
plt.title('Scatterplot between returns for Raytheon Company \nand General Dynamics Corporation', fontsize=16)
plt.xlabel('RTN - Raytheon Company', fontsize=14)
plt.ylabel('GD - General Dynamics Corporation', fontsize=14)

plt.show()


# In[ ]:



