#File Name: core_logic.py

import pandas as pd

#Show Menu
def show_menu():
    print("\n===== ELECTRONICS SALES MENU =====")
    print("1. Load Data")
    print("2. Preview Data")
    print("3. Revenue Analysis")
    print("4. Product Analysis")
    print("5. Customer Analysis")
    print("6. Sales Trends")
    print("7. Visualize Data")
    print("8. Generate Report")
    print("9. Exit")

# Revenue Analysis
def revenue_analysis(df):
    if df is None:
        print("Sorry! Data not Found, Load data first.")
        return

    total_revenue = df['amount'].sum()
    avg_order = df['amount'].mean()
    total_transactions = len(df)

    print("\nRevenue Analysis")
    print("Total Revenue:", total_revenue)
    print("Average Order Value:", avg_order)
    print("Total Transactions:", total_transactions)
