from expense_tracker import Expense, ExpenseTracker
tracker = ExpenseTracker()
print("This is your Expense Tracker App.")
while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. Remove Expense")
    print("3. View Expenses")
    print("4. Total Expenses")
    print("5. Exit")

    choice = int(input("What will you like to do today? Choose a number from the above options: "))

    if choice == 1:
        date = input("Enter the date (YYYY-MM-DD): ")
        descrption = input("Enter the expense description: ")
        amount = int(input("Enter the amount: "))
        expense = Expense(date,descrption,amount)
        tracker.add_expense(expense)
        print("Expense added Successfully")

    elif choice == 2:
        view_first = input("Do you want to view your expenses to know which one you would like to remove? Yes/No ").lower()
        if view_first == "yes":
            tracker.view_expenses()
            user_index = int(input("Enter the Expense Index or number to remove: "))
            zero_index = user_index - 1
            tracker.remove_expense(zero_index)
        else:
            user_index = int(input("Enter the Expense Index or number to remove: "))
            zero_index = user_index - 1
            tracker.remove_expense(zero_index)

    elif choice == 3:
        tracker.view_expenses()

    elif choice == 4:
        tracker.total_expenses()

    elif choice == 5:
        print("Goodbye")
        break

    else:
        print("Invalid Choice, please try again")
