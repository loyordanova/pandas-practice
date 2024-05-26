# Step 1. Import the necessary libraries

import pandas as pd
import ssl

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

# ------------------------------------------------------------------------------------------------

# Step 2. Import the dataset from this address.
# Step 3. Assign it to a variable called drinks.
drinks = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv')

# -----------------------------------------------------------------------------------------------

print(drinks.columns)
# Step 4. Which continent drinks more beer on average?
# continent_consumption = drinks.groupby('continent')['beer_servings'].mean()
# alcohol_consumption = continent_consumption.max()
# print(continent_consumption.idxmax())

# ------------------------------------------------------------------------------------------------

# Step 5. For each continent print the statistics for wine consumption.
# continent_wine_statistics = drinks.groupby('continent')['wine_servings'].describe()
# print(continent_wine_statistics)

# ------------------------------------------------------------------------------------------------

# Step 6. Print the mean alcohol consumption per continent for every column
# mean_consumption = drinks.groupby('continent').mean(numeric_only=True)
# print(mean_consumption)

# ------------------------------------------------------------------------------------------------

# Step 7. Print the median alcohol consumption per continent for every column
# median_consumption = drinks.groupby('continent').median(numeric_only=True)
# print(median_consumption)

# ------------------------------------------------------------------------------------------------

# Step 8. Print the mean, min and max values for spirit consumption.
# mean_min_max = drinks.groupby('continent')['spirit_servings'].agg(['mean', 'min', 'max'])
# print(mean_min_max)

