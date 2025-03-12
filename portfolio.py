import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Set page config
st.set_page_config(page_title="Portfolio Manager", layout="wide")

# Sidebar
st.sidebar.title("📊 Portfolio Manager")
st.sidebar.write("Manage and track your investments with ease!")

# Sample portfolio data
data = {
    "Stock": ["AAPL", "GOOGL", "TSLA", "AMZN", "MSFT"],
    "Shares": [10, 5, 8, 12, 7],
    "Price": [175, 2850, 700, 3450, 310],
}
df = pd.DataFrame(data)
df["Total Value"] = df["Shares"] * df["Price"]

total_portfolio_value = df["Total Value"].sum()

# Portfolio Allocation Pie Chart
fig_pie = px.pie(df, names="Stock", values="Total Value", title="Portfolio Allocation", color_discrete_sequence=px.colors.sequential.Plasma)

# Line Chart for Stock Performance (Dummy Data)
dates = pd.date_range(start="2024-01-01", periods=10)
stocks = {symbol: pd.Series([p * (1 + 0.02 * i) for i, p in enumerate([data['Price'][idx]] * 10)], index=dates) for idx, symbol in enumerate(data['Stock'])}
stock_df = pd.DataFrame(stocks)
fig_line = px.line(stock_df, title="Stock Performance", labels={"index": "Date", "value": "Price"})

# App Layout
st.title("🚀 Portfolio Management Dashboard")
st.metric("Total Portfolio Value", f"${total_portfolio_value:,.2f}")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Portfolio Allocation")
    st.plotly_chart(fig_pie, use_container_width=True)

with col2:
    st.subheader("Stock Performance Over Time")
    st.plotly_chart(fig_line, use_container_width=True)

# Show Portfolio Data
table_color = "#0E1117"
st.markdown(f"<style>.dataframe {{ background-color: {table_color}; color: white; }}</style>", unsafe_allow_html=True)
st.dataframe(df.style.set_properties(**{'background-color': table_color, 'color': 'white'}))