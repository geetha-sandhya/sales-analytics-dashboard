import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Superstore Sales Dataset.csv")

print(data.head())
# Group by Category and sum sales
category_sales = data.groupby("Category")["Sales"].sum()
# Find top category
top_category = category_sales.idxmax()
region_sales = data.groupby("Region")["Sales"].sum()
# Find best region
top_region = region_sales.idxmax()
# Category sales chart
category_sales.plot(kind='bar')

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.show()
# AI-style insight for top category
print("Top Category is:", top_category, "with highest sales.")

# AI-style insight for top region
print("Top Region is:", top_region, "with highest sales.")

# Compare categories
for category, value in category_sales.items():
    print(category, "has total sales of", round(value, 2))