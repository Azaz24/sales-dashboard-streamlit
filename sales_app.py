import streamlit as st
import pandas as pd

st.title("📊 Sales Dashboard")

data = {
    "Product": ["Laptop", "Phone", "Tablet", "Headphones", "Shoes"],
    "Category": ["Electronics", "Electronics", "Electronics", "Accessories", "Fashion"],
    "Sales": [50000, 30000, 20000, 10000, 15000]
}

df = pd.DataFrame(data)

st.sidebar.header("Filter")
category = st.sidebar.selectbox("Select Category", df["Category"].unique())

filtered_df = df[df["Category"] == category]

st.dataframe(filtered_df)
st.line_chart(filtered_df["Sales"])