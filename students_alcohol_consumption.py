# Step 1. Import the necessary libraries

import pandas as pd
import numpy as np
import ssl

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

# ------------------------------------------------------------------------------------------------

# Step 2. Import the dataset from this address.
# Step 3. Assign it to a variable called df

url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv'
df = pd.read_csv(url)
# print(df.head())

# ------------------------------------------------------------------------------------------------

# Step 4. For the purpose of this exercise slice the dataframe from 'school' until the 'guardian' column
# sliced = df.loc[:, "school":"guardian"]
# print(sliced)

# ------------------------------------------------------------------------------------------------

# Step 5. Create a lambda function that will capitalize strings.
capitalizer = lambda x: x.capitalize()

# ------------------------------------------------------------------------------------------------

# Step 6. Capitalize both Mjob and Fjob
# cap_mjoc = df['Mjob'].apply(capitalizer)
# cap_fjob = df['Fjob'].apply(capitalizer)
# print(cap_mjoc)
# print(cap_fjob)

# ------------------------------------------------------------------------------------------------

# Step 7. Print the last elements of the data set.
# print(df.tail())

# ------------------------------------------------------------------------------------------------

# Step 8. Did you notice the original dataframe is still lowercase? Why is that? Fix it and capitalize Mjob and Fjob.
# df['Mjob'] = df['Mjob'].apply(capitalizer)
# df['Fjob'] = df['Fjob'].apply(capitalizer)

# ------------------------------------------------------------------------------------------------

# Step 9. Create a function called majority that returns a boolean value to a new column called legal_drinker (Consider majority as older than 17 years old)


