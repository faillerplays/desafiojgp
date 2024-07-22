'''Using Plotly in Python, develop a chart displaying the All items, less food and
energy, seasonally adjusted price series with year-over-year percentage
variation using the monthly data from 2019 to the present. Keep the frequency
monthly in the chart.'''
import plotly.express as px
import pandas as pd

# Load the data (assuming it's stored in a CSV file named "cpi_data.csv")
df = pd.read_csv("cpi_data.csv")

# Filter the data to only include the "CPI All items, less food and energy, seasonally adjusted" price series
df_filtered = df[['date', 'CPI All items, less food and energy, seasonally adjusted']].copy()
#YoY change on CPI ALL items less food and energy
df_filtered.loc[: ,'YoY Change'] = df_filtered['CPI All items, less food and energy, seasonally adjusted'].pct_change(12) * 100

# Create a line chart showing the year-over-year percentage change in the "CPI All items, less food and energy, seasonally adjusted" price series. Keep the frequency monthly.
fig = px.line(df_filtered, x='date', y='YoY Change', title='Year-over-Year Percentage Change in CPI All Items Less Food and Energy', labels={'date': 'Date', 'YoY Change': 'Year-over-Year Percentage Change (%)'})
# Add a horizontal line at y=0 to indicate zero growth
fig.add_shape(type='line', x0=df_filtered['date'].min(), y0=0, x1=df_filtered['date'].max(), y1=0, line=dict(color='red', dash='dash'))
fig.write_html('cpilfeyoy.html')
fig.show()


'''3. Describe in words how you would automate the process of extracting the data.
R:
To automate the process of extracting the data, I would use a task scheduler to run the script at the start of every month.'''