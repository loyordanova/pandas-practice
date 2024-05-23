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
print(chipo.columns)

# ------------------------------------------------------------------------------------------------

# Step 8. How is the dataset indexed?
# print(chipo.index)

# ------------------------------------------------------------------------------------------------

# Step 9. Which was the most-ordered item?
# grouped = chipo.groupby('item_name').sum()['quantity']
# max_item = grouped.idxmax()
# max_qty = grouped.max()
# print(max_item, max_qty)

# c = chipo.groupby('item_name')
# c = c.sum()
# c = c.sort_values(['quantity'], ascending=False)
# print(c.head(1))

# ------------------------------------------------------------------------------------------------

# Step 10. For the most-ordered item, how many items were ordered?
#
# print(chipo.groupby('item_name').sum()['quantity'].max())

# c = chipo.groupby('item_name')
# c = c.sum()
# c = c.sort_values(['quantity'], ascending=False)
# c.head(1)

# ------------------------------------------------------------------------------------------------

# Step 11. What was the most ordered item in the choice_description column?
# c = chipo.groupby('choice_description').sum()
# c = c.sort_values(['quantity'], ascending=False)
# print(c.head(1))
#
# print(chipo.groupby('choice_description').sum())

# ------------------------------------------------------------------------------------------------

# Step 12. How many items were orderd in total?
# print(chipo.quantity.sum())

# ------------------------------------------------------------------------------------------------

# Step 13. Turn the item price into a float
# removing the dollar sign and converting the rest to a float $2.39 -> 2.39
# dollarizer = lambda x: float(x[1:])
# applying the function to each item
# chipo.item_price = chipo.item_price.apply(dollarizer)

# ------------------------------------------------------------------------------------------------

# Step 14. How much was the revenue for the period in the dataset?
# Calculate the total revenue by multiplying quantity and item_price for each order, then summing up
# total_revenue = (chipo['quantity'] * chipo['item_price']).sum()
# np.round is a NumPy function that rounds the number to the specified number of decimal places.
# print(np.round(total_revenue, 2))

# ------------------------------------------------------------------------------------------------

# Step 15. How many orders were made in the period?
# orders_made = chipo.order_id.value_counts().count()
# print(orders_made)

# ------------------------------------------------------------------------------------------------

# Step 16. What is the average revenue amount per order?
# chipo['total_revenue'] = (chipo['quantity'] * chipo['item_price']).sum()
# order_totals = chipo.groupby(by=['order_id']).sum()
# avg_revenue_per_order = chipo['total_revenue'].mean()
# print(avg_revenue_per_order)

# ------------------------------------------------------------------------------------------------

# Step 17. How many different items are sold?
# diff_items_sold = chipo.item_name.nunique()
# another way
# chipo.item_name.value.counts().count()
# print(diff_items_sold)

# ------------------------------------------------------------------------------------------------

# Step 18. How many times were a Veggie Salad Bowl ordered?
# veggie_salad_bowl = chipo.groupby('item_name')['quantity'].sum()
# print(veggie_salad_bowl['Veggie Salad Bowl'])
# or
# veggie_salad_bowl = chipo[chipo.item_name == 'Veggie Salad Bowl']
# print(len(veggie_salad_bowl))

# ------------------------------------------------------------------------------------------------

# Step 19. How many products cost more than $10.00?
# chipo['item_price'] = chipo['item_price'].str.replace('$', '') .astype(float)
# product_cost_more_than_10 = chipo[chipo['item_price'] > 10]['item_name'].nunique()
# print(product_cost_more_than_10)

# ------------------------------------------------------------------------------------------------

# Step 20. What is the price of each item?
# print(chipo[['item_name', 'item_price']].drop_duplicates().to_string(index=False))

# ------------------------------------------------------------------------------------------------

# Step 21. Sort by the name of the item
# sorted_by_name = chipo.item_name.sort_values()
# print(sorted_by_name)

# ------------------------------------------------------------------------------------------------

# Step 22. What was the quantity of the most expensive item ordered?
# chipo['item_price'] = chipo['item_price'].str.replace('$', '') .astype(float)
# sorted_items = chipo.sort_values(by='item_price', ascending=False).head(1)
# print(sorted_items)
# print(f"Most expensive item is: {sorted_items['item_name'].to_string(index=False)} ->\n"
#       f"price: {sorted_items['item_price'].to_string(index=False)}\n"
#       f"quantity: {sorted_items['quantity'].to_string(index=False)}")

# ------------------------------------------------------------------------------------------------

# Step 23. How many times did someone order more than one Canned Soda?
canned_soda = chipo[chipo.item_name == 'Canned Soda']
canned_soda_more_than_one = len(canned_soda[canned_soda.quantity > 1])
print(canned_soda_more_than_one)
# or
# canned_soda_more_than_one = chipo[(chipo.item_name == 'Canned Soda') & (chipo.quantity > 1)]
# print(len(canned_soda_more_than_one))