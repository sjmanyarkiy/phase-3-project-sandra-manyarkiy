def main_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("     FINANCE TRACKER - MAIN MENU")
    print("="*50)
    print("1. Manage Users")
    print("2. Manage Expenses")
    print("3. Manage Budgets")
    print("4. View Reports")
    print("5. Exit")
    print("="*50)

def user_menu():
    """Display the user management menu"""
    print("\n" + "="*50)
    print("     USER MANAGEMENT")
    print("="*50)
    print("1. Create a new user")
    print("2. View all users")
    print("3. Find user by ID")
    print("4. Delete a user")
    print("5. Back to main menu")
    print("="*50)

def expense_menu():
    """Display the expense management menu"""
    print("\n" + "="*50)
    print("     EXPENSE MANAGEMENT")
    print("="*50)
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. View expenses by category")
    print("4. Delete an expense")
    print("5. Back to main menu")
    print("="*50)

def budget_menu():
    """Display the budget management menu"""
    print("\n" + "="*50)
    print("     BUDGET MANAGEMENT")
    print("="*50)
    print("1. Set a budget")
    print("2. View all budgets")
    print("3. View budget vs spending")
    print("4. Delete a budget")
    print("5. Back to main menu")
    print("="*50)

def handle_user_menu():
    """Handle user management menu"""
    while True:
        user_menu()
        choice = input("> ").strip()
        
        if choice == "1":
            create_user()
        elif choice == "2":
            view_all_users()
        elif choice == "3":
            find_user_by_id()
        elif choice == "4":
            user = find_user_by_id()
            if user:
                delete_user(user)
        elif choice == "5":
            break
        else:
            print("❌ Invalid choice. Please try again.")
