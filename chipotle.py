# Step 1. Import the necessary libraries
import pandas as pd
import numpy as np
import requests
import ssl

# ------------------------------------------------------------------------------------------------

# Step 2. Import the dataset from this address.
# Step 3. Assign it to a variable called chipo

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'

chipo = pd.read_csv(url, sep='\t')


# ------------------------------------------------------------------------------------------------

# Step 4. See the first 10 entries
# print(chipo.head(10))

# ------------------------------------------------------------------------------------------------

# Step 5. What is the number of observations in the dataset?
# print(chipo.shape[0])

# ------------------------------------------------------------------------------------------------

# Step 6. What is the number of columns in the dataset?
# print(chipo.shape[1])

# ------------------------------------------------------------------------------------------------

# Step 7. Print the name of all the columns.
# print(chipo.columns)

# ------------------------------------------------------------------------------------------------

# Step 8. How is the dataset indexed?
# print(chipo.index)