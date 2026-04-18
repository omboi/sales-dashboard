import streamlit as st
import pandas as pd
import plotly.express as px

# Page title
st.title("Interactive Sales Dashboard")

# Load data
df = pd.read_csv("sales.csv")
df["date"] = pd.to_datetime(df["date"])

# Sidebar filters
st.sidebar.header("Filters")

region = st.sidebar.multiselect(
    "Select Region",
    options=df["region"].unique(),
    default=df["region"].unique()
)

date_range = st.sidebar.date_input(
    "Select Date Range",
    [df["date"].min(), df["date"].max()]
)

# Filter data
filtered_df = df[
    (df["region"].isin(region)) &
    (df["date"] >= pd.to_datetime(date_range[0])) &
    (df["date"] <= pd.to_datetime(date_range[1]))
]

# KPI
total_sales = filtered_df["sales"].sum()
st.metric("Total Sales", total_sales)

# Charts
st.subheader("Sales Over Time")
fig1 = px.line(filtered_df, x="date", y="sales", title="Daily Sales")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Sales by Product")
fig2 = px.bar(filtered_df, x="product", y="sales", color="product")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Sales by Region")
fig3 = px.pie(filtered_df, names="region", values="sales")
st.plotly_chart(fig3, use_container_width=True)
