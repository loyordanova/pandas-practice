# Step 1. Import the necessary libraries

import pandas as pd
import numpy as np
import ssl

# ------------------------------------------------------------------------------------------------

# Step 2. Import the dataset from this address.
# Step 3. Assign it to a variable called euro12

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv'

euro12 = pd.read_csv(url, sep=',')
# print(euro12)
print(euro12.columns)

# ------------------------------------------------------------------------------------------------

# Step 4. Select only the Goal column.
# print(euro12['Goals'])  # print(euro12.Goals) -> same

# ------------------------------------------------------------------------------------------------

# Step 5. How many team participated in the Euro2012?
# teams = euro12.Team.count()
# print(teams)
# or
# euro12.shape[0]

# ------------------------------------------------------------------------------------------------

# Step 6. What is the number of columns in the dataset?
# print(euro12.shape[1])

# ------------------------------------------------------------------------------------------------

# Step 7. View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline
discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]
# print(discipline)

# ------------------------------------------------------------------------------------------------

# Step 8. Sort the teams by Red Cards, then to Yellow Cards
sorted_teams = discipline.sort_values(['Red Cards', 'Yellow Cards'], ascending=False)
# print(sorted_teams)

# ------------------------------------------------------------------------------------------------

# Step 9. Calculate the mean Yellow Cards given per Team
mean_yellow_cards = round(discipline['Yellow Cards'].mean())
# print(mean_yellow_cards)

# ------------------------------------------------------------------------------------------------

# Step 10. Filter teams that scored more than 6 goals
filtered_teams = euro12[euro12['Goals'] > 6]
# print(filtered_teams)

# ------------------------------------------------------------------------------------------------

# Step 11. Select the teams that start with G
teams = euro12[euro12['Team'].str.startswith('G')]
# print(teams)

# ------------------------------------------------------------------------------------------------

# Step 12. Select the first 7 columns
# print(euro12.iloc[:, 0: 7])

# ------------------------------------------------------------------------------------------------

# Step 13. Select all columns except the last 3
# print(euro12.iloc[:, 0: -3])

# ------------------------------------------------------------------------------------------------

# Step 14. Present only the Shooting Accuracy from England, Italy and Russia
filtered_accuracy = euro12.loc[euro12.Team.isin(['England', 'Italy', 'Russia']), ['Team', 'Shooting Accuracy']]
print(filtered_accuracy)