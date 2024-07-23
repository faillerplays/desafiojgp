# US Inflation Analysis (JGP Challenge)

This repository contains the solution for the data scientist internship recruitment challenge by JGP . The goal of the challenge is to analyze US inflation data (CPI) obtained from the Bureau of Labor Statistics (BLS).

## Repository Structure

* **question1.py:** Script to fetch inflation data from the BLS API, process it, and save it to a CSV file.
* **question2&3.py:** Script to generate an interactive plot showing the evolution of the CPI "All items less food and energy" (seasonally adjusted) and its annual percentage change.
* **question4.py:** Script to generate `cpiallvscpigasoline.html` - analyzing the relationship between the CPI "All items" and the "Gasoline" CPI.
* **question5.py:** Bonus question - Script to create a FastAPI application that allows queries to the CPI data.
* **cpi_data.csv:** CSV file containing the inflation data obtained from the BLS API.
* **cpiallvscpigasoline.html:** HTML file containing the charts of the percentage change in general CPI and gasoline.
* **cpilfeyoy.html:** HTML file containing the chart of the year-over-year percentage change of CPI All items less food and energy.
* **requirements.txt:** List of Python dependencies required to run the project.
## How to run the project

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/faillerplays/desafiojgp.git](https://github.com/faillerplays/desafiojgp.git)
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run scripts:**
    ```bash
    python question1.py
    python question2&3.py
    python question4.py
    python question5.py
    ```
4. **Start FastAPI server from question5.py**
   ```bash
     uvicorn questao5:app --reload
   ```
## Interactive Visualization

You can view the interactive visualization of the CPI All Items and Gasoline data by clicking the link below:

[View CPI and Gasoline Data Visualization](https://faillerplays.github.io/desafiojgp/cpiallvscpigasoline.html)
[View CPI All Items Less Food and Energy YoY % Change](https://faillerplays.github.io/desafiojgp/cpilfeyoy.html)
## Autor

*   [Miguel Dargains] - [miguel.dargains@gmail.com]

## License

This project is licensed under the MIT License. See the LICENSE file for details.
