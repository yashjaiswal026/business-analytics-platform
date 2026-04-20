#File Name: analysis.py

import pandas as pd

#Product Analysis
def product_analysis(df):
    if df is None:
        print("Sorry! Data not Found, Load data first.")
        return

    print("\nTop Selling Products")
    top_products = df['product'].value_counts().sort_values(ascending=False).head()
    print(top_products)

    print("\nLeast Selling Products")
    least_products = df['product'].value_counts().sort_values(ascending=True).head()
    print(least_products)

    print("\nCategory-wise Sales")
    print(df.groupby('category')['amount'].sum())

#Customer Analysis
def customer_analysis(df):
    if df is None:
        print("Sorry! Data not Found, Load data first.")
        return

    print("\nTotal Unique Customers:", df['customer'].nunique())

    print("\nMost Active Customers")
    print(df['customer'].value_counts().head())

#Sales Trends
def sales_trends(df):
    if df is None:
        print("Sorry! Data not Found, Load data first.")
        return

    df['date'] = pd.to_datetime(df['date'])
    daily = df.groupby(df['date'].dt.date)['amount'].sum()
    monthly = df.groupby(df['date'].dt.to_period('M'))['amount'].sum()

    print("\nDaily Sales Trend")
    print(daily.head())
    print("\nMonthly Sales Trend")
    print(monthly.head())
