# expense_tracker.py

class ExpenseTracker:
    """A class to track expenses."""

    def __init__(self):
        """Initialize an empty dictionary to store expenses by category."""
        self.expenses = {}

    def add_expense(self, category, amount):
        """Add an expense to the tracker.

        Args:
            category (str): The category of the expense.
            amount (float): The amount of the expense.
        """
        if category in self.expenses:
            self.expenses[category].append(amount)
        else:
            self.expenses[category] = [amount]

    def get_total_expenses(self):
        """Calculate the total expenses.

        Returns:
            float: The total expenses.
        """
        total_expenses = sum(sum(amounts) for amounts in self.expenses.values())
        return total_expenses

    def get_expenses_by_category(self, category):
        """Get expenses by category.

        Args:
            category (str): The category to filter expenses.

        Returns:
            list: A list of expenses matching the given category.
        """
        return self.expenses.get(category, [])

    def get_categories(self):
        """Get all categories with expenses."""
        return list(self.expenses.keys())

    def get_category_total(self, category):
        """Calculate total expenses for a specific category.

        Args:
            category (str): The category to calculate total expenses.

        Returns:
            float: The total expenses for the given category.
        """
        return sum(self.expenses.get(category, []))

def main():
    """Main function to interact with the expense tracker."""
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Total Expenses")
        print("3. View Expenses by Category")
        print("4. View All Categories")
        print("5. View Total Expenses by Category")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            tracker.add_expense(category, amount)
            print("Expense added successfully!")

        elif choice == "2":
            total_expenses = tracker.get_total_expenses()
            print(f"Total Expenses: ${total_expenses:.2f}")

        elif choice == "3":
            category = input("Enter category to view expenses: ")
            expenses = tracker.get_expenses_by_category(category)
            print(f"Expenses in '{category}':")
            for expense in expenses:
                print(f" - ${expense:.2f}")

        elif choice == "4":
            categories = tracker.get_categories()
            print("Categories with expenses:")
            for category in categories:
                print(f" - {category}")

        elif choice == "5":
            category = input("Enter category to view total expenses: ")
            total_category_expenses = tracker.get_category_total(category)
            print(f"Total expenses in '{category}': ${total_category_expenses:.2f}")

        elif choice == "6":
            print("Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
