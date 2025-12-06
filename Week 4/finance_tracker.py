import csv
import os

FILE_NAME = "expenses.csv"


# Load the CSV file into a list of dictionaries
def load_expenses():
    expenses = []

    # If file doesn't exist, create it
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "category", "description", "amount"])
        return expenses

    # Read existing data
    with open(FILE_NAME, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            expenses.append(row)

    return expenses


# Save the entire list back to the CSV file
def save_expenses(expenses):
    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "category", "description", "amount"])
        for e in expenses:
            writer.writerow([e["date"], e["category"], e["description"], e["amount"]])


# Add a new expense
def add_expense(expenses):
    print("\n=== Add New Expense ===")
    date = input("Date (YYYY-MM-DD): ")
    category = input("Category: ")
    description = input("Description: ")
    amount = input("Amount: ")

    expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }

    expenses.append(expense)
    save_expenses(expenses)  # update file immediately

    print("Expense added and saved!\n")


# Display all expenses
def display_expenses(expenses):
    if not expenses:
        print("No expenses saved.\n")
        return

    print("\n=== All Expenses ===")
    for e in expenses:
        print("Date       :", e["date"])
        print("Category   :", e["category"])
        print("Description:", e["description"])
        print("Amount     :", e["amount"])
        print("--------------------")
    print()


# Main program
def main():
    expenses = load_expenses()

    while True:
        print("=== Personal Finance Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            display_expenses(expenses)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


main()
