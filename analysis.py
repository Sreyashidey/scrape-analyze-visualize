# -*- coding: utf-8 -*-
"""analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1O_4fv3pUP9YhJ4GgJTUERboHT8CgByf0

After extraction, analyse the data with your preferred python libraries and show your
understanding of the data and your skill set. (Graphs & fruitful analysis will be
appreciated)
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("output.csv")

df.head()

print(df.dtypes)

df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
df['Sales Price'] = pd.to_numeric(df['Sales Price'], errors='coerce')

print(f"NaN values in 'Price': {df['Price'].isnull().sum()}")
print(f"NaN values in 'Sales Price': {df['Sales Price'].isnull().sum()}")

df_cleaned = df.dropna(subset=['Price', 'Sales Price'])

print(df.dtypes)

df.describe()

"""# a. Most expensive product"""

most_expensive_product = df_cleaned.loc[df_cleaned['Sales Price'].idxmax()]

product_name = most_expensive_product['Name']
sales_price = most_expensive_product['Sales Price']

print(f"The most expensive product is: {product_name}")
print(f"Sales Price: {sales_price}")

"""#b. Cheapest Product"""

cheapest_product = df_cleaned.loc[df_cleaned['Sales Price'].idxmin()]
cheapest_product_name = cheapest_product['Name']
cheapest_product_price = cheapest_product['Sales Price']
print(f"The cheapest product is: {cheapest_product_name}")
print(f"Sales Price: {cheapest_product_price}")

"""# c. Number of Products from Each brand

"""

brand_counts = df_cleaned['Brand'].value_counts()
print("\nNumber of Products from Each Brand:")
print(brand_counts)

"""#d. Number of Products by Each seller
considering sku as the seller ids
"""

seller_counts = df_cleaned['SKU'].value_counts()
print("\nNumber of Products by Each Seller:")
print(seller_counts)

plt.figure(figsize=(30,10))
brand_counts.plot(kind='bar', color='skyblue')
plt.title("Number of Products from Each Brand")
plt.xlabel("Brand")
plt.ylabel("Number of Products")
plt.xticks(rotation=45)
plt.show()

"""We find that the brand generic has the highest number of products."""

df['Average Rating'] = pd.to_numeric(df['Average Rating'], errors='coerce')
df['Rating Count'] = pd.to_numeric(df['Rating Count'], errors='coerce')
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
df['Sales Price'] = pd.to_numeric(df['Sales Price'], errors='coerce')
df_cleaned = df.dropna(subset=['Average Rating', 'Rating Count'])
most_popular_products = df_cleaned[['Name', 'Rating Count']].sort_values(by='Rating Count', ascending=False).head(10)
top_rated_products = df_cleaned[['Name', 'Average Rating']].sort_values(by='Average Rating', ascending=False).head(10)

expensive_top_rated = df_cleaned[['Name', 'Price', 'Average Rating']].sort_values(by=['Average Rating', 'Price'], ascending=[False, False]).head(10)

high_rating_low_price = df_cleaned[['Name', 'Average Rating', 'Sales Price']].sort_values(by=['Average Rating', 'Sales Price'], ascending=[False, True]).head(10)

# Correlation between Rating Count and Price
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df_cleaned, x='Rating Count', y='Price')
plt.title('Correlation Between Rating Count and Price')
plt.xlabel('Number of Ratings')
plt.ylabel('Price')
plt.show()

# Rating Distribution
plt.figure(figsize=(8, 6))
sns.histplot(df_cleaned['Average Rating'], bins=10, kde=True)
plt.title('Distribution of Product Ratings')
plt.xlabel('Average Rating')
plt.ylabel('Frequency')
plt.show()

print("Most Popular Products Based on Rating Count:")
print(most_popular_products)
print("\nTop Rated Products:")
print(top_rated_products)
print("\nMost Expensive Top Rated Products:")
print(expensive_top_rated)
print("\nHigh Rated Products with Low Sales Price:")
print(high_rating_low_price)

# Sponsored vs Non-Sponsored Products
sponsored_counts = df_cleaned['Sponsored'].value_counts()

# Plotting Sponsored vs Non-Sponsored Products
plt.figure(figsize=(6, 4))
sponsored_counts.plot(kind='pie', autopct='%1.1f%%', colors=['lightcoral', 'lightgreen'])
plt.title("Sponsored vs Non-Sponsored Products")
plt.ylabel('')
plt.show()

"""This analysis will gives a comprehensive view of the data, helping us to understand the price distribution, most popular and best-rated products, and the proportion of sponsored listings."""