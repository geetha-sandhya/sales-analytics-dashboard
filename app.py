import streamlit as st
import pandas as pd

st.title("📊 Sales Analytics Dashboard")

data = pd.read_csv("Superstore Sales Dataset.csv")

total_sales = data["Sales"].sum()
top_category = data.groupby("Category")["Sales"].sum().idxmax()
low_category = data.groupby("Category")["Sales"].sum().idxmin()

st.metric("Total Sales", f"{total_sales:.0f}")
st.metric("Top Category", top_category)
st.metric("Lowest Category", low_category)

st.subheader("Sales by Category")
st.bar_chart(data.groupby("Category")["Sales"].sum())

st.subheader("Sales by Region")
st.bar_chart(data.groupby("Region")["Sales"].sum())