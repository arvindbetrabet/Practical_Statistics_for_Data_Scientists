
# coding: utf-8

# # Practical Statistics for Data Scientists
# ## Exploratory Data Analysis

# This Notebook is the python equivalent of the R code for Chapter-1, from the book <a href="http://shop.oreilly.com/product/0636920048992.do">Practical Statistics for Data Scientists</a> by Peter Bruce and Andrew Bruce. This <a href="https://github.com/andrewgbruce/statistics-for-data-scientists">GitHub</a> repository has the complete R code for the book.
# 
# The authors note that the aim of the book is to be a "Desk Reference" for key Statistical concepts that are relevant to Data Science, explaining their importance and the reason behind that choice.
# 
# Data that is used in the book, has been curated by the authors and made available on <a href="https://drive.google.com/drive/folders/0B98qpkK5EJemYnJ1ajA1ZVJwMzg">Google Drive</a> and <a href="https://www.dropbox.com/sh/clb5aiswr7ar0ci/AABBNwTcTNey2ipoSw_kH5gra?dl=0">Dropbox</a>
# 
# <b>NOTE:</b>
# The data for creating the Contingency Table has been downloaded from the Lending Club <a href=" https://www.lendingclub.com/info/download-data.action">website</a> for the year 2007-2011. Please see the screenshot
# 
# <img src="../img/lending_club.png" style="width:400px; height: 400px;"></img>
# 

# In[2]:

import numpy as np
import pandas as pd


# In[3]:

# Read the data from a .csv file
# This file is a modified version of the original
# CSV file from the Lending Club website. It just has
# grade, sub_grade and loan_status columns

loanDataDF = pd.read_csv("../data/lc_Stats_2007_2011.csv")



# In[4]:

# Check the type of data structure, holding the data
type(loanDataDF)


# In[5]:

# Top 10 rows/records of the data
loanDataDF.head(10)


# In[6]:

# Bottom 10 rows/records of the data
loanDataDF.tail(10)


# In[7]:

# Get the data types of feature/attributes in the data
loanDataDF.dtypes


# <br>

# ## Two Variables - Both Categorical

# ### Contingency Table

# In[8]:

loanDataCrossTab = pd.crosstab(loanDataDF['grade'], loanDataDF['loan_status'], margins=True)


# In[9]:

print(loanDataCrossTab)


# <b>NOTE:</b><br>
# The column in the Contingency Table that has the “Does not meet the credit policy” wording, represent loans that were funded by investors and issued by Lending Club, prior to 2010, but that would not qualify for listing today.<br>
# 
# The grade categories range from A to G, A being the "lowest risk", with F & G being the "high risk", in terms of paying off the loan.  A loan becomes “charged off” when there is no longer a reasonable expectation of further payments. Charge off typically occurs when a loan is no later than 150 days past due.
# 

# <br>
