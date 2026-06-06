import csv
import os

FILE_NAME = "expenses.csv"

# Create file with header only once
def initialize_file():
    if not os.path.isfile(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Amount", "Category", "Total"])

# Get last total
def get_last_total():
    total = 0
    try:
        with open(FILE_NAME, "r") as file:
            reader = list(csv.reader(file))
            if len(reader) > 1:
                last_row = reader[-1]
                total = float(last_row[2])
    except:
        pass
    return total

# Add Expense
def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    last_total = get_last_total()
    new_total = last_total + amount

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([amount, category, new_total])

    print(f"Expense saved! Running total: ₹{new_total}\n")

# View Expenses
def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            next(reader)  # skip header

            for i, row in enumerate(reader, start=1):
                print(f"{i}. {row[1]} - ₹{row[0]} | Total: ₹{row[2]}")
        print()
    except FileNotFoundError:
        print("No data found.\n")

# Total Expense (latest total)
def total_expense():
    total = get_last_total()
    print(f"Total spending: ₹{total}\n")

# Menu
def menu():
    initialize_file()

    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spending")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_expense()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice\n")

menu()