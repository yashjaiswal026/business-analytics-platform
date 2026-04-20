#File Name: data_loader.py

import pandas as pd

#Preview Data
def preview_data(df):
    if df is None:
        print("Sorry! Data not Found, Load data first.")
        return

    print("\nDataset Preview")
    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])
    print("Column Names:", list(df.columns))
    print(df.head())

#Load Data
def load_data(filename):
    
    try:
        # Load CSV file
        df = pd.read_csv(filename)

        # Check if dataset is empty
        if df.empty:
            print("Dataset is empty.")
            return None

        # amount column (string value to numbric)
        df['amount'] = pd.to_numeric(df['amount'], errors='coerce')

        # Clean data (remove missing values)
        df = df.dropna()

        # Reset index after cleaning
        df.reset_index(drop=True, inplace=True)

        print("!!!! File loaded and data cleaned successfully. !!!!")
        return df

    except FileNotFoundError:
        print("Error: File not found.")
    except pd.errors.EmptyDataError:
        print("Error: File is empty.")
    except pd.errors.ParserError:
        print("Error: Invalid CSV format.")
    except Exception as e:
        print("Unexpected error:", e)
    return None
