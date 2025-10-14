class Expense():
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = amount

class ExpenseTracker():
    def __init__(self):
        self.expenses = []

    def add_expense(self,expense):
        self.expenses.append(expense)

    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            print("Expense deleted successfully.")
        else:
            print("Invalid Expense index.")

    def view_expenses(self):
        if len(self.expenses) == 0:
            print("No available Expenses found.")
        else:
            for i, expense in enumerate(self.expenses, start=1):
                print(f"{i}. Date:{expense.date}, Description:{expense.description}, Amount:{expense.amount}")

    def total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total Expenses = #{total}")

