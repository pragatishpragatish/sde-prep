import json

def load_expenses():
    global expenses

    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)

    except FileNotFoundError:
        expenses = []

def add_expenses():
    category = input("Enter Spend Category: ")
    amount = float(input("Enter Amount Spent: "))
    description = input("Description(Optional): ")

    expense = {"category": category, "amount": amount, "description": description}

    expenses.append(expense)
    print("Expense Added!")


def view_expense():
    if not expenses:
        print("No Expenses to Show")
    for expense in expenses:
        print("------------------")
        print("Category: ", expense["category"])
        print("Amount: ", expense["amount"])
        print("Description: ", expense["description"])
    print("------------------")

def calculate_total():
    total = 0
    
    for expense in expenses:
        total += expense["amount"]
    print("------------------")
    print("Total Amount Spent:", total)
    print("------------------")

def save_data():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)

    print("File Saved!")

load_expenses()

while True:
    print("Expense Tracker")
    print("1. Enter Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Exit")
    option = int(input("Enter an Option: "))
    match option:
        case 1:
            add_expenses()
        case 2:
            view_expense()
        case 3:
            calculate_total()
        case 4:
            print("Goodbye!")
            save_data()
            break
        case _:
            print("Invalid Option")
