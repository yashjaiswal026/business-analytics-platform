#File Name: visualization.py

import pandas as pd
import matplotlib.pyplot as plt

#Visualize Data
def visualize_data(df):
    if df is None:
        print("Sorry! Data not Found, Load data first.")
        return

    # Top products
    top_products = df['product'].value_counts().head()
    top_products.plot(kind='bar', title="Top Products")
    plt.show()

    # Sales trend
    df['date'] = pd.to_datetime(df['date'])
    sales_trend = df.groupby(df['date'].dt.date)['amount'].sum()
    sales_trend.plot(kind='line', title="Sales Trend")
    plt.show()

    # Category distribution
    category = df.groupby('category')['amount'].sum()
    category.plot(kind='pie', autopct='%1.1f%%')
    plt.title("Category Distribution")
    plt.show()

#Generate_report
def generate_report(df):
    if df is None:
        print("Sorry! Data not Found, Load data first.")
        return

    total_revenue = df['amount'].sum()

    with open("report.txt", "w") as f:
        f.write("ELECTRONICS SALES REPORT\n")
        f.write("=============================\n")
        f.write(f"Total Revenue: {total_revenue}\n")
        f.write(f"Total Transactions: {len(df)}\n")
        f.write(f"Unique Customers: {df['customer'].nunique()}\n")

    print("Report generated: report.txt")
