# Step 1. Import the necessary libraries
import pandas as pd
import requests
import ssl

# ------------------------------------------------------------------------------------------------

# Step 2. Import the dataset from this address.
# Step 3. Assign it to a variable called users and use the 'user_id' as index
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'
response = requests.get(url)

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

# Read the CSV data and set 'user_id' as the index
users = pd.read_csv(url, sep='|', index_col='user_id')

# ------------------------------------------------------------------------------------------------

# Step 4. See the first 25 entries
# print(users.head(25))

# ------------------------------------------------------------------------------------------------

# Step 5. See the last 10 entries
# print(users.tail(5))

# ------------------------------------------------------------------------------------------------

# Step 6. What is the number of observations in the dataset?
# print(users.shape[0])

# ------------------------------------------------------------------------------------------------

# Step 7. What is the number of columns in the dataset?
# print(users.shape[1])

# ------------------------------------------------------------------------------------------------

# Step 8. Print the name of all the columns.
# print(users.columns)

# ------------------------------------------------------------------------------------------------

# Step 9. How is the dataset indexed?
# print(users.index)

# ------------------------------------------------------------------------------------------------

# Step 10. What is the data type of each column?
# print(users.dtypes)

# ------------------------------------------------------------------------------------------------

# Step 11. Print only the occupation column
# print(users.occupation)  # or users['occupation']

# ------------------------------------------------------------------------------------------------

# Step 12. How many different occupations there are in this dataset?
# print(users.occupation.value_counts().count())  # or users.occupation.nunique()

# ------------------------------------------------------------------------------------------------

# Step 13. What is the most frequent occupation?
# print(users.occupation.value_counts().head(1).index[0])

# ------------------------------------------------------------------------------------------------

# Step 14. Summarize the DataFrame.
# print(users.describe())

# ------------------------------------------------------------------------------------------------

# Step 15. Summarize all the columns
# print(users.describe(include='all'))  # by default, only the numeric columns are returned.

# ------------------------------------------------------------------------------------------------

# Step 16. Summarize only the occupation column
# print(users['occupation'].describe())

# ------------------------------------------------------------------------------------------------

# Step 17. What is the mean age of users?
# print(round(users.age.mean()))

# ------------------------------------------------------------------------------------------------

# Step 18. What is the age with least occurrence?
print(users.age.value_counts().tail(1).index[0])