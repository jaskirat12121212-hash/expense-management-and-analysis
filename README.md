💰 Expense Intelligence

A Python-based expense management application that helps users track transactions and analyze spending patterns through interactive dashboards.

Features

- Add and view expense transactions
- Category-wise expense analysis
- Interactive bar charts for spending comparison
- Transaction history using Pandas
- CSV-based data storage

Tech Stack

Python · Streamlit · Pandas · Matplotlib · FastAPI

Analysis

- Total spending by category
- Comparison of expenses across categories
- Historical transaction review
- New expense comparison with previous transactions (if enabled)

Run Locally

pip install -r requirements.txt
streamlit run expense_manage_frontent.py

If FastAPI is required, start the backend separately:

uvicorn main:app --reload

