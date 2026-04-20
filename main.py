#File Name: main.py

from data_loader import preview_data, load_data
from core_logic import show_menu, revenue_analysis
from analysis import product_analysis, customer_analysis, sales_trends
from visualization import visualize_data, generate_report

df = None

while True:
    show_menu()
    choice = input("\nEnter choice: ")

    if choice == "1":
        file = input("Enter CSV filename: ")
        df = load_data(file)

    elif choice == "2":
        preview_data(df)

    elif choice == "3":
        revenue_analysis(df)

    elif choice == "4":
        product_analysis(df)

    elif choice == "5":
        customer_analysis(df)

    elif choice == "6":
        sales_trends(df)

    elif choice == "7":
        visualize_data(df)

    elif choice == "8":
        generate_report(df)

    elif choice == "9":
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")
