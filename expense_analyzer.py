import csv

def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (Food/Travel/Shopping/Other): ")
    amount = float(input("Enter amount: "))

    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

    print("Expense added successfully!\n")


def view_summary():
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            total = 0
            max_expense = 0
            categories = {}

            for row in reader:
                amount = float(row[2])
                total += amount

                if amount > max_expense:
                    max_expense = amount

                category = row[1]
                categories[category] = categories.get(category, 0) + amount

        print("\n------- Expense Summary -------")
        print(f"Total Spending: ₹{total}")
        print(f"Highest Single Expense: ₹{max_expense}")
        print("Category-wise Spending:")
        for c, a in categories.items():
            print(f"  {c}: ₹{a}")
        print("--------------------------------\n")

    except FileNotFoundError:
        print("No expenses found. Add some first!\n")


def main():
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


from tabulate import tabulate
import csv

def view_expenses():
    rows = []
    
    with open("expenses.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        
        for row in reader: 
            rows.append(row)
        
        if not rows:
            print("No expenses found!")
        else:
            print(tabulate(rows, header, tablefmt= "grid"))
def add_expenses():
    category = input("Enter category: ")
    amount = input("Enter amount: ")
    
    with open("expenses.csv", "a", newline= " ") as file:
        writer = csv.writer(file)
        writer.writerow([category, amount])
        print("Expenses added successfully!")
        
def main():
    while True:
        print("\n---- Expense Analyzer ----")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            break
        else:
            print("Invalid choice!")
            
main()