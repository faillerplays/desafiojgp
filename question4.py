'''Explain how you would relate the price series (All items) with the Gasoline
(Gasoline) price series.
I would plot both series on the same chart to visually compare their trends and identify any potential
correlations or patterns between them. Additionally, I could calculate the percentage change in each series and compare the
changes over time to see if there are any consistent relationships between the two series.
I would also conduct a correlation analysis to determine the strength and direction of the relationship between the two series.'''

import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
from sklearn.linear_model import LinearRegression
import numpy as np

# Load CPI data
cpi_data = pd.read_csv('cpi_data.csv')

# Convert the date column to datetime
cpi_data['date'] = pd.to_datetime(cpi_data['date'])

# Calculate percentage change
cpi_data['CPI All items, pct_change'] = cpi_data['CPI All items, seasonally adjusted'].pct_change() * 100
cpi_data['CPI Gasoline, pct_change'] = cpi_data['CPI Gasoline (all types), seasonally adjusted'].pct_change() * 100

# Drop missing values
cpi_data.dropna(inplace=True)

# Create the figure for percentage change
fig_pct_change = go.Figure()
fig_pct_change.add_trace(go.Scatter(x=cpi_data['date'], y=cpi_data['CPI All items, pct_change'], mode='lines', name='CPI All items % Change'))
fig_pct_change.add_trace(go.Scatter(x=cpi_data['date'], y=cpi_data['CPI Gasoline, pct_change'], mode='lines', name='CPI Gasoline % Change'))
fig_pct_change.update_layout(title='Percentage Change in CPI All Items and Gasoline over Time',
                             xaxis_title='Date',
                             yaxis_title='Percentage Change')

# Create the figure for prices
fig_prices = go.Figure()
fig_prices.add_trace(go.Scatter(x=cpi_data['date'], y=cpi_data['CPI All items, seasonally adjusted'], mode='lines', name='CPI All items Prices'))
fig_prices.add_trace(go.Scatter(x=cpi_data['date'], y=cpi_data['CPI Gasoline (all types), seasonally adjusted'], mode='lines', name='CPI Gasoline Prices'))
fig_prices.update_layout(title='Prices of CPI All Items and Gasoline over Time',
                         xaxis_title='Date',
                         yaxis_title='Prices')

# Calculate regression
X = cpi_data['CPI Gasoline (all types), seasonally adjusted'].values[:, np.newaxis]  # predictor variable
y = cpi_data['CPI All items, seasonally adjusted'].values  # response variable

model = LinearRegression()
model.fit(X, y)
beta = model.coef_[0]

# Create figure for regression
fig_regression = go.Figure()
fig_regression.add_trace(go.Scatter(x=cpi_data['CPI Gasoline (all types), seasonally adjusted'], y=cpi_data['CPI All items, seasonally adjusted'], mode='markers', name='Data Points'))
fig_regression.add_trace(go.Scatter(x=cpi_data['CPI Gasoline (all types), seasonally adjusted'], y=model.predict(X), mode='lines', name='Regression Line'))
fig_regression.update_layout(title=f'Regression Line (Beta = {beta:.2f})',
                             xaxis_title='CPI Gasoline Prices',
                             yaxis_title='CPI All Items Prices')

# Generate HTML for each figure
html_pct_change = pio.to_html(fig_pct_change, full_html=False, include_plotlyjs='cdn')
html_prices = pio.to_html(fig_prices, full_html=False, include_plotlyjs='cdn')
html_regression = pio.to_html(fig_regression, full_html=False, include_plotlyjs='cdn')

# Combine HTML content
full_html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>CPI Analysis</title>
</head>
<body>
    <h1>Percentage Change in CPI All Items and Gasoline over Time</h1>
    {html_pct_change}
    <h1>Prices of CPI All Items and Gasoline over Time</h1>
    {html_prices}
    <h1>Regression Line between Gasoline Prices and CPI All Items</h1>
    <p>The beta value between gasoline prices and the CPI All Items is 0.28.There's a positive link,
 but it's not super strong. Gasoline prices have a moderate effect on the overall cost of living</p>
    {html_regression}
</body>
</html>
"""

# Save to HTML file
with open('cpiallvscpigasoline.html', 'w') as f:
    f.write(full_html)

print("Plots saved as cpiallvscpigasoline.html")

print(f"The correlation between the Gasoline price series and the CPI All items series is {beta:.2f}")

