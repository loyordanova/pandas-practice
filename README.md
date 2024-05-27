# Pandas 🐼

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Pandas Data Structures](#pandas-data-structures)
  - [Series](#series)
  - [DataFrame](#dataframe)
- [Reading Data](#reading-data)
- [Basic DataFrame Operations](#basic-dataframe-operations)
  - [Viewing Data](#viewing-data)
  - [Selecting Data](#selecting-data)
- [Data Cleaning](#data-cleaning)
- [Data Manipulation](#data-manipulation)
- [Grouping and Aggregating Data](#grouping-and-aggregating-data)
- [Merging and Joining DataFrames](#merging-and-joining-dataframes)
- [Saving Data](#saving-data)
- [Conclusion](#conclusion)

## Introduction
Pandas is a powerful Python library used for data manipulation and analysis. 
It is built on top of NumPy and provides data structures like Series and DataFrame, 
which are essential for data analysis tasks.

## Installation
To use pandas, you need to install it first. You can install pandas using pip:
```bash
pip install pandas
```
## Pandas Data Structures
Pandas mainly uses two data structures: Series and DataFrame.

## Series
A Series is a one-dimensional array-like object that can hold data of any type.

```ruby
import pandas as pd

# Creating a Series
data = [1, 2, 3, 4, 5]
series = pd.Series(data)

print(series)
```
## DataFrame
A DataFrame is a two-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axes (rows and columns).

```ruby
# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

print(df)
```
## Reading Data

Pandas can read data from various file formats such as CSV, Excel, SQL, and more.

Example: Reading from a CSV file
```
df = pd.read_csv('data.csv')

print(df)
```
## Basic DataFrame Operations

Viewing Data
You can view the data in a DataFrame using various methods:

head(): View the first few rows (default is 5).<br>
tail(): View the last few rows (default is 5).<br>
info(): Get a concise summary of the DataFrame.<br>
describe(): Generate descriptive statistics of the DataFrame.<br>

Example:
```
import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}

df = pd.DataFrame(data)

# View the first few rows
print("Head:\n", df.head())

# View the last few rows
print("Tail:\n", df.tail())

# Get a concise summary
print("Info:\n", df.info())

# Generate descriptive statistics
print("Describe:\n", df.describe())
```
## Viewing Data

head(): Displays the first few rows of the DataFrame. By default, it shows the first 5 rows.<br>
tail(): Displays the last few rows of the DataFrame. By default, it shows the last 5 rows.<br>
info(): Provides a concise summary of the DataFrame, including the number of non-null entries in each column.<br>
describe(): Generates descriptive statistics of the DataFrame, such as count, mean, standard deviation, min, and max values for numerical columns.<br>
shape: Returns the dimensions of the DataFrame (number of rows, number of columns).<br>
columns: Returns the column labels of the DataFrame.<br>
index: Returns the index (row labels) of the DataFrame.<br>
dtypes: Returns the data types of each column.<br>
values: Returns the underlying data as a NumPy array.<br>
sample(): Returns a random sample of rows from the DataFrame.<br>

Examples:
```
import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}

df = pd.DataFrame(data)

# View the first few rows
print("Head:\n", df.head())

# output ----------------------------

Head:
       Name  Age         City
0    Alice   25     New York
1      Bob   30  Los Angeles
2  Charlie   35      Chicago
3    David   40      Houston
4      Eve   45      Phoenix

# View the last few rows
print("Tail:\n", df.tail())

# output ----------------------------

Tail:
       Name  Age         City
0    Alice   25     New York
1      Bob   30  Los Angeles
2  Charlie   35      Chicago
3    David   40      Houston
4      Eve   45      Phoenix

# Get a concise summary of the DataFrame
print("Info:\n")
df.info()

# output ----------------------------

Info:

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   Name    5 non-null      object
 1   Age     5 non-null      int64 
 2   City    5 non-null      object
dtypes: int64(1), object(2)
memory usage: 248.0+ bytes

# Generate descriptive statistics
print("Describe:\n", df.describe())

# output ----------------------------

Describe:
             Age
count   5.000000
mean   35.000000
std     7.905694
min    25.000000
25%    30.000000
50%    35.000000
75%    40.000000
max    45.000000

# Get the shape of the DataFrame
print("Shape:", df.shape)

# output ----------------------------

Shape: (5, 3)

# Get the column labels of the DataFrame
print("Columns:", df.columns)

# output ----------------------------

Columns: Index(['Name', 'Age', 'City'], dtype='object')

# Get the index (row labels) of the DataFrame
print("Index:", df.index)

# output ----------------------------

Index: RangeIndex(start=0, stop=5, step=1)

# Get the data types of each column
print("Data Types:\n", df.dtypes)

# output ----------------------------

Data Types:
Name    object
Age      int64
City    object
dtype: object

# Get the underlying data as a NumPy array
print("Values:\n", df.values)

# output ----------------------------

Values:
 [['Alice' 25 'New York']
 ['Bob' 30 'Los Angeles']
 ['Charlie' 35 'Chicago']
 ['David' 40 'Houston']
 ['Eve' 45 'Phoenix']]


# Get a random sample of rows
print("Random Sample:\n", df.sample(2))

# output ----------------------------

Random Sample:
     Name  Age         City
1     Bob   30  Los Angeles
2  Charlie   35      Chicago
```

## Selecting Data
You can select data by columns, rows, or specific cell values:

Selecting a column: df['column_name']
Selecting multiple columns: df[['column1', 'column2']]
Selecting rows by label: df.loc[index_label]
Selecting rows by position: df.iloc[row_index]

Example:
```
# Selecting a single column
print("Select a column (Name):\n", df['Name'])

# Selecting multiple columns
print("Select multiple columns (Name, City):\n", df[['Name', 'City']])

# Selecting a row by label
print("Select a row by label (index 2):\n", df.loc[2])

# Selecting a row by position
print("Select a row by position (index 3):\n", df.iloc[3])
```
## Filtering Data
You can filter data based on conditions:

Example:
```
# Filter rows where Age is greater than 30
filtered_df = df[df['Age'] > 30]
print("Filtered DataFrame (Age > 30):\n", filtered_df)
```

## Modifying Data
You can modify data in various ways, such as adding new columns, modifying existing columns, or deleting columns:

Example:
```
# Adding a new column
df['Salary'] = [50000, 60000, 70000, 80000, 90000]
print("DataFrame with new column (Salary):\n", df)

# Modifying an existing column
df['Age'] = df['Age'] + 1
print("DataFrame with modified column (Age):\n", df)

# Deleting a column
df.drop('City', axis=1, inplace=True)
print("DataFrame after dropping column (City):\n", df)
```
## Handling Missing Values
You can handle missing values by filling them or dropping them:

Example:
```
# Sample DataFrame with missing values
data_with_nan = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, None, 35, 40, None],
    'City': ['New York', 'Los Angeles', 'Chicago', None, 'Phoenix']
}

df_with_nan = pd.DataFrame(data_with_nan)
print("DataFrame with NaN values:\n", df_with_nan)

# Filling missing values
df_filled = df_with_nan.fillna({'Age': 0, 'City': 'Unknown'})
print("DataFrame after filling NaN values:\n", df_filled)

# Dropping rows with missing values
df_dropped = df_with_nan.dropna()
print("DataFrame after dropping NaN values:\n", df_dropped)
```
## Sorting Data
You can sort data by a specific column:

Example:
```
# Sorting by Age
df_sorted = df.sort_values(by='Age')
print("DataFrame sorted by Age:\n", df_sorted)
```
## Grouping and Aggregating Data
You can group data by a specific column and perform aggregate functions:

Example:
```
# Sample DataFrame for grouping
data_for_grouping = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Department': ['HR', 'IT', 'HR', 'IT', 'HR'],
    'Salary': [50000, 60000, 70000, 80000, 90000]
}

df_grouping = pd.DataFrame(data_for_grouping)

# Grouping by Department and calculating the mean salary
grouped_df = df_grouping.groupby('Department').mean()
print("Grouped DataFrame by Department:\n", grouped_df)
```
## Merging and Joining DataFrames

1. Merging DataFrames on a Key/Column

Example:
```
import pandas as pd

# Sample DataFrames
data1 = {
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David']
}

data2 = {
    'ID': [3, 4, 5, 6],
    'Age': [25, 30, 35, 40]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Merge DataFrames on 'ID' column
merged_df = pd.merge(df1, df2, on='ID')

print("Merged DataFrame on 'ID':\n", merged_df)

# output ----------------------------------

Merged DataFrame on 'ID':
    ID     Name  Age
0   3  Charlie   35
1   4    David   40
```
2. Merging DataFrames with Different Join Types

Example:
```
# Inner Join
inner_join_df = pd.merge(df1, df2, on='ID', how='inner')
print("\nInner Join:\n", inner_join_df)

# Outer Join
outer_join_df = pd.merge(df1, df2, on='ID', how='outer')
print("\nOuter Join:\n", outer_join_df)

# Left Join
left_join_df = pd.merge(df1, df2, on='ID', how='left')
print("\nLeft Join:\n", left_join_df)

# Right Join
right_join_df = pd.merge(df1, df2, on='ID', how='right')
print("\nRight Join:\n", right_join_df)

# output ---------------------------------------

Inner Join:
    ID     Name  Age
0   3  Charlie   35
1   4    David   40

Outer Join:
    ID     Name   Age
0   1    Alice   NaN
1   2      Bob   NaN
2   3  Charlie  35.0
3   4    David  40.0
4   5      NaN  25.0
5   6      NaN  30.0

Left Join:
    ID     Name   Age
0   1    Alice   NaN
1   2      Bob   NaN
2   3  Charlie  35.0
3   4    David  40.0

Right Join:
    ID     Name   Age
0   3  Charlie  35.0
1   4    David  40.0
2   5      NaN  25.0
3   6      NaN  30.0
```
3. Joining DataFrames on Index

Example:
```
# Sample DataFrames with indices
data3 = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40]
}

data4 = {
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df3 = pd.DataFrame(data3, index=[1, 2, 3, 4])
df4 = pd.DataFrame(data4, index=[1, 2, 3, 4])

# Join DataFrames on index
joined_df = df3.join(df4)

print("\nJoined DataFrame on index:\n", joined_df)

# output ---------------------------------------

Joined DataFrame on index:
       Name  Age         City
1    Alice   25     New York
2      Bob   30  Los Angeles
3  Charlie   35      Chicago
4    David   40      Houston
```
4. Concatenating DataFrames

Example:
```
# Sample DataFrames
data5 = {
    'Name': ['Alice', 'Bob'],
    'Age': [25, 30]
}

data6 = {
    'Name': ['Charlie', 'David'],
    'Age': [35, 40]
}

df5 = pd.DataFrame(data5)
df6 = pd.DataFrame(data6)

# Concatenate DataFrames
concat_df = pd.concat([df5, df6])

print("\nConcatenated DataFrame:\n", concat_df)

# output ---------------------------------------

Concatenated DataFrame:
       Name  Age
0    Alice   25
1      Bob   30
0  Charlie   35
1    David   40
```

## Saving Data

1. Saving to CSV

Example:
```
import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}

df = pd.DataFrame(data)

# Save DataFrame to CSV
df.to_csv('data.csv', index=False)
```

2. Saving to Excel

Example:
```
# Save DataFrame to Excel
df.to_excel('data.xlsx', index=False)
```

3. Saving to JSON

Example:
```
# Save DataFrame to JSON
df.to_json('data.json', orient='records')
```

4. Saving to SQL Database

Example:
```
import sqlite3

# Create a SQLite database connection
conn = sqlite3.connect('data.db')

# Save DataFrame to SQL Database
df.to_sql('data_table', conn, if_exists='replace', index=False)

# Close the connection
conn.close()
```
## Conclusion

🐼 Pandas provides a wide range of functionalities for data manipulation and analysis, making it an essential tool for data scientists and analysts. By mastering pandas, you'll have the skills to efficiently clean, transform, analyze, and visualize data for various data-driven tasks and projects.🐼
