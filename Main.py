from tracker import FinanceTracker
from expense import Expense

tracker = FinanceTracker()
tracker.load()


def show_menu():
    print("\n===== Personal Finance Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Search by Category")
    print("5. Delete Expense")
    print("6. Exit")


while True:

    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Name: ").strip()

        if not name:
            print("Expense name cannot be empty.")
            continue

        try:
            amount = float(input("Amount: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        category = input("Category: ").strip()
        date = input("Date (YYYY-MM-DD): ").strip()

        expense = Expense(
            name,
            amount,
            category,
            date
        )

        tracker.add(expense)
        tracker.save()

        print("Expense added successfully!")

    elif choice == "2":

        if not tracker.expenses:
            print("No expenses found.")
        else:
            tracker.show()

    elif choice == "3":

        total = tracker.calculate_total()

        print(f"\nTotal Spending: ${total:.2f}")

    elif choice == "4":

        category = input("Enter category: ")

        results = tracker.search(category)

        if results:

            print("\nMatching Expenses:\n")

            for expense in results:
                print(
                    f"{expense.name} | "
                    f"${expense.amount:.2f} | "
                    f"{expense.category} | "
                    f"{expense.date}"
                )

        else:
            print("No matching expenses found.")

    elif choice == "5":

        tracker.show()

        try:
            number = int(input("Expense number to delete: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        tracker.delete(number)
        tracker.save()

        print("Expense deleted successfully.")

    elif choice == "6":

        print("Goodbye!")

        break

    else:

        print("Invalid option. Please choose between 1 and 6.")
