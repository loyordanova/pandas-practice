import pandas as pd
import random

# Define lists of possible values for each attribute

names = ["Arthas", "Sylvanas", "Thrall", "Jaina", "Illidan", "Varian", "Garrosh", "Tyrande", "Malfurion", "Gul'dan",
         "Anduin", "Vol'jin", "Saurfang", "Velen", "Grommash", "Khadgar", "Maiev", "Alleria", "Sargeras", "Turalyon",
         "Kael'thas", "Baine", "Magni", "Uther", "Ner'zhul", "Kel'Thuzad", "Sylvos", "Azshara", "Cairne", "Durotan",
         "Genn", "Kil'jaeden", "Medivh", "Muradin", "Tichondrius", "Ysera", "Anduin", "Vashj", "Mannoroth", "Kargath",
         "Drek'Thar", "Cairne", "Anub'arak", "Vashj", "Muradin", "Saurfang", "Tirion", "Darion", "Taelan", "Ysera"]
races = ["Human", "Undead", "Orc", "Night Elf", "Blood Elf", "Tauren", "Dwarf", "Gnome", "Troll"]
classes = ["Paladin", "Hunter", "Shaman", "Mage", "Warlock", "Warrior", "Druid", "Priest", "Rogue"]
levels = [random.randint(1, 100) for _ in range(50)]  # Generate random levels
genders = ["Male", "Female"]
guilds = ["Knights", "Dark Rangers", "Horde", "Kirin Tor", "Illidari", "Alliance", "Scourge", "Dragonflight"]

# ------------------------------------------------------------------------------------------------

# Generate random data for each character

data = {
    "Name": [random.choice(names) for _ in range(50)],
    "Race": [random.choice(races) for _ in range(50)],
    "Class": [random.choice(classes) for _ in range(50)],
    "Level": [random.choice(levels) for _ in range(50)],
    "Gender": [random.choice(genders) for _ in range(50)],
    "Guild": [random.choice(guilds) for _ in range(50)]
}

# ------------------------------------------------------------------------------------------------
# CREATE DATAFRAME

"""
Data sets in Pandas are usually multi-dimensional tables, called DataFrames.

Series is like a column, a DataFrame is the whole table.
"""

# Create a DataFrame from the generated data
wow_df = pd.DataFrame(data)

# ------------------------------------------------------------------------------------------------

# PLAYING WITH ROWS

# Display the first few rows of the DataFrame
# print(wow_df.head(7))

# Return one row
# print(wow_df.loc[0])

"""
LOC VS ILOC

loc (Label-based indexing)
Usage: loc is used for label-based indexing and selection by the actual labels of the rows and columns.
Syntax: df.loc[row_labels, column_labels]

iloc (Integer-based indexing)
Usage: iloc is used for integer-based indexing and selection by the position of the rows and columns.
Syntax: df.iloc[row_indices, column_indices]
"""

# Return one specific value of the DataFrame
# print(wow_df.loc[1, 'Level'])

# Select a single column and show only the first 3
# print(wow_df['Class'].head(3))

# Select a multiple columns
# print(wow_df[['Class', 'Level']])

# Select rows where column value > 50 (returns boolean)
# print(wow_df['Level'] > 50)

# Returns the whole DataFrame with all rows where 'Level' value > 50
# print(wow_df[wow_df['Level'] > 50])

# Returns data about all rows that have 'Level' value > 50 (real values not bools)
# print(wow_df['Level'][wow_df['Level'] > 50])

# ------------------------------------------------------------------------------------------------

# DATA TYPE

# Check the data types of each column
# print(wow_df.dtypes)


"""
int64: 
This data type represents 64-bit integers. 
It's commonly used for columns containing whole numbers without decimal points, 
such as IDs, counts, or levels.

float64: 
This data type represents 64-bit floating-point numbers. 
It's used for columns containing numerical data with decimal points, 
such as measurements or percentages.

object: 
This data type represents strings or mixed data types. 
It's often used for columns containing text or categorical variables. 
However, it can also include other types of data, 
so it's essential to check the contents of these columns.

datetime64: 
This data type represents date and time values. 
It's used for columns containing date or timestamp information.

bool: 
This data type represents boolean values (True or False). 
It's used for columns containing binary or boolean data.
"""

# ------------------------------------------------------------------------------------------------

# DESCRIBE() method


"""
The describe() function in Pandas provides summary statistics of the numerical columns in a DataFrame. 
It calculates several common statistics for each numerical column, including:

count: The number of non-null values in the column.
mean: The average value of the column.
std: The standard deviation, which measures the spread or dispersion of the values in the column.
min: The minimum value in the column.
25% (Q1): The first quartile, which represents the value below which 25% of the data falls.
50% (median): The median, which represents the middle value of the data. 50% of the data falls below this value.
75% (Q3): The third quartile, which represents the value below which 75% of the data falls.
max: The maximum value in the column.
"""

# Display summary statistics of the numerical columns
# print(wow_df.describe())

# Customize describe() function
# custom_stats = wow_df.describe(percentiles=[0.1, 0.25, 0.5, 0.75, 0.9])
# custom_stats = custom_stats.drop(['count', 'std'])
# print(custom_stats)


# ------------------------------------------------------------------------------------------------

# GROUP BY

"""
The groupby() function in Pandas is used to group rows in a DataFrame based on a specific column or set of columns. 
It allows you to perform operations on the grouped data, such as aggregation, filtering, or transformation.

The syntax for groupby() is:

df.groupby(by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True, squeeze=False, observed=False, dropna=True)
"""

# Group by column
grouped_by_race = wow_df.groupby('Race')
# for name, group in grouped_by_race:  # name is the name of the group and group is all the members(rows)
#     print(name)
#     print(group)

# Sum level by Race
summed_level = grouped_by_race['Level'].sum()
# print(summed_level)

# same thing here
# print(wow_df.groupby('Race')['Level'].sum())

# Average Level by Race
avg_level_by_race = wow_df.groupby('Race')['Level'].mean()
# print("Average Level by Race:")
# print(avg_level_by_race)

# Average Level by Class
avg_level_by_class = wow_df.groupby('Class')['Level'].mean()
# print("\nAverage Level by Class:")
# print(avg_level_by_class)

# ------------------------------------------------------------------------------------------------

# COUNTING

"""
The value_counts() function in Pandas is used to count the occurrences of each unique value in a column. 
It returns a Series containing the unique values and their corresponding counts.

The syntax for value_counts() is:

Series.value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True)
"""

# Distribution of Genders
gender_distribution = wow_df['Gender'].value_counts()
# print("\nDistribution of Genders:")
# print(gender_distribution)

# Most Common Guilds
most_common_guilds = wow_df['Guild'].value_counts().head(5)
# print("\nMost Common Guilds:")
# print(most_common_guilds)
