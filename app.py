import streamlit as st
import pandas as pd

st.title("📊 Sales Analytics Dashboard")

# Load data
data = pd.read_csv("Superstore Sales Dataset.csv")

# KPI Section
total_sales = data["Sales"].sum()
top_category = data.groupby("Category")["Sales"].sum().idxmax()
low_category = data.groupby("Category")["Sales"].sum().idxmin()

st.metric("Total Sales", f"{total_sales:.0f}")
st.metric("Top Category", top_category)
st.metric("Lowest Category", low_category)

# Sales by Category
st.subheader("Sales by Category")
category_sales = data.groupby("Category")["Sales"].sum()
st.bar_chart(category_sales)

# Sales by Region
st.subheader("Sales by Region")
region_sales = data.groupby("Region")["Sales"].sum()
st.bar_chart(region_sales)