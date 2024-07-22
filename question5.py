from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd

app = FastAPI()

# Load CPI data (from previous question)
df_cpi = pd.read_csv('cpi_data.csv', index_col='date', parse_dates=True)


@app.get("/cpi")
async def get_cpi_data(start_date: str = None, end_date: str = None):
    """

        start_date: (optional) Start date in YYYY-MM-DD format.
        end_date: (optional) End date in YYYY-MM-DD format.
        http://127.0.0.1:8000/cpi?start_date=2024-01-01&end_date=2024-05-01
    """

    if start_date and end_date:
        # Filter by date range
        filtered_df = df_cpi[(df_cpi.index >= start_date) & (df_cpi.index <= end_date)]
    elif start_date:
        # Filter from start date
        filtered_df = df_cpi[df_cpi.index >= start_date]
    elif end_date:
        # Filter until end date
        filtered_df = df_cpi[df_cpi.index <= end_date]
    else:
        # Return all data if no dates are provided
        filtered_df = df_cpi

    return JSONResponse(filtered_df.to_json(orient="index", date_format='iso'))
