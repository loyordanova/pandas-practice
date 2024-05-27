# Learn Pandas from Scratch

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
