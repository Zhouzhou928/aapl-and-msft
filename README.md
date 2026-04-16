# aapl-and-msft
This project compares Apple (AAPL) and Microsoft (MSFT)’s 2015–2023 financial performance via WRDS data, analyzing profitability, solvency, and efficiency. Apple leads in margins from premium hardware; Microsoft grows steadily via cloud. An interactive Streamlit dashboard visualizes trends, turning raw data into clear insights for investors.
# ACC102 Track4: Interactive Financial Analysis Dashboard – AAPL vs MSFT
Student Name: XIAOXU.ZHOU
Student ID: 2471738

## 1. Project Purpose
This project develops an interactive and visually intuitive financial analysis dashboard to compare the financial performance of Apple Inc. (AAPL) and Microsoft Corporation (MSFT) over the period 2015–2023. The goal is to transform raw historical financial data into clear, dynamic, and interpretable insights using Python programming and the Streamlit visualization framework.

## 2. Data Source
All financial data is retrieved from the WRDS Compustat database, which provides reliable and standardized corporate financial information. The dataset includes key items such as revenue, net income, total assets, total liabilities, current assets, current liabilities, total equity, and operating cash flow. The analysis covers nine full fiscal years from 2015 to 2023.

## 3. Financial Metrics Calculated
The project focuses on five critical financial dimensions to evaluate corporate performance:
- Net Profit Margin: Measures the profitability of each dollar of sales.
- Return on Equity (ROE): Reflects the return generated for shareholders’ investments.
- Debt-to-Asset Ratio: Assesses the long-term solvency and financial leverage.
- Current Ratio: Evaluates short-term liquidity and the ability to cover current obligations.
- Asset Turnover: Indicates how efficiently a company uses its assets to generate sales.

## 4. Dashboard Functions and Features
The interactive dashboard supports advanced user controls and real-time updates:
- Adjustable weight slider to simulate a combined portfolio of AAPL and MSFT.
- Multi-select tool to choose and compare multiple financial ratios simultaneously.
- Real-time calculation of weighted average financial indicators.
- Time-series line charts for long-term trend comparison.
- Scatter plot to analyze the relationship between operational efficiency and profitability.
- Annual bar charts for revenue comparison across selected years.
- Synchronized data tables for transparent value checking.

## 5. Online Access Link
The interactive application has been deployed online and is publicly accessible at:
https://aapl-and-msft-jxjduvdzrgzqpkzspiwis4.streamlit.app/

Users can directly open the link in a browser to explore all functions without local installation or configuration.

## 6. How to Run Locally
1. Install required libraries:
pip install -r requirements.txt
2. Launch the dashboard locally:
streamlit run app.py
3. Access the interactive interface via a web browser at:
http://localhost:8001

## 7. Key Observations and Analysis Results
Apple maintains a consistently high net profit margin due to its strong brand pricing power and product premium strategy. Microsoft shows steady and sustainable growth in profitability driven by its cloud services and enterprise software segments. Both companies maintain healthy liquidity and moderate leverage, ensuring financial stability. Apple demonstrates relatively higher asset turnover, while Microsoft focuses on high-margin recurring revenue.

## 8. Conclusion
This project integrates data extraction, ratio computation, statistical analysis, and interactive visualization in a complete workflow. The dashboard allows users to dynamically explore financial differences, strategic characteristics, and performance trends between two leading global technology firms. It serves as an effective tool for financial analysis, learning demonstration, and data-driven decision-making.
