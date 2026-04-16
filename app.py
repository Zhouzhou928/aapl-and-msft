import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Financial Analysis", layout="wide")

st.title("📊 WRDS Financial Analysis Tool")
st.subheader("ACC102 Track4 | AAPL vs MSFT Comparison")

df_aapl = pd.read_csv("data_aapl.csv")
df_msft = pd.read_csv("data_msft.csv")

st.sidebar.header("Settings")
company_mode = st.sidebar.selectbox("View Mode", ["AAPL", "MSFT", "Comparison"])
metric = st.sidebar.selectbox("Metric", [
    "net_profit_margin", "debt_asset_ratio", "asset_turnover", "roe", "current_ratio"
])

if company_mode == "AAPL":
    st.subheader("Apple Inc. Analysis")
    fig, ax = plt.subplots()
    ax.plot(df_aapl['year'], df_aapl[metric], marker='o', color='blue')
    ax.set_title(metric)
    ax.grid(True)
    st.pyplot(fig)
    st.dataframe(df_aapl.round(2))

elif company_mode == "MSFT":
    st.subheader("Microsoft Corp. Analysis")
    fig, ax = plt.subplots()
    ax.plot(df_msft['year'], df_msft[metric], marker='s', color='orange')
    ax.set_title(metric)
    ax.grid(True)
    st.pyplot(fig)
    st.dataframe(df_msft.round(2))

else:
    st.subheader("AAPL vs MSFT Comparison")
    fig, ax = plt.subplots()
    ax.plot(df_aapl['year'], df_aapl[metric], marker='o', label='AAPL')
    ax.plot(df_msft['year'], df_msft[metric], marker='s', label='MSFT')
    ax.set_title(f"Comparison: {metric}")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("AAPL Data")
        st.dataframe(df_aapl.round(2))
    with col2:
        st.subheader("MSFT Data")
        st.dataframe(df_msft.round(2))

st.subheader("Asset Turnover vs Net Profit Margin")
fig2, ax2 = plt.subplots()
ax2.scatter(df_aapl['asset_turnover'], df_aapl['net_profit_margin'], label='AAPL')
ax2.scatter(df_msft['asset_turnover'], df_msft['net_profit_margin'], label='MSFT')
ax2.set_xlabel("Asset Turnover")
ax2.set_ylabel("Net Profit Margin")
ax2.legend()
st.pyplot(fig2)