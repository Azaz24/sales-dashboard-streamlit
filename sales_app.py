import streamlit as st
import pandas as pd

# ----------------------------
# Title & Subheader
# ----------------------------
st.title("📊 Sales Dashboard App")
st.subheader("A simple app to analyze product sales by category")

# ----------------------------
# Hardcoded Data
# ----------------------------
data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Phone"],
    "Category": ["Electronics", "Electronics", "Electronics", "Electronics", "Electronics"],
    "Sales": [50000, 1500, 3000, 12000, 25000]
}

df = pd.DataFrame(data)

# ----------------------------
# Sidebar Filter
# ----------------------------
st.sidebar.header("🔍 Filter Data")
category = st.sidebar.selectbox("Select Category", df["Category"].unique())

# Filter data
filtered_df = df[df["Category"] == category]

# ----------------------------
# Main Section
# ----------------------------
st.write("### 📋 Filtered Sales Data")
st.dataframe(filtered_df)

# ----------------------------
# Line Chart
# ----------------------------
st.write("### 📈 Sales Trend")
st.line_chart(filtered_df.set_index("Product")["Sales"])