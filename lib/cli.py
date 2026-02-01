#!/usr/bin/env python3

import click

from models.user import User
from models.category import Category
from models.expense import Expense
from models.budget import Budget

click.command()
def menu():
    """main menu"""

    while True:
        click.echo("\n" + "="*60)
        click.echo(click.style("  💰 FINANCE TRACKER - MAIN MENU 💰", fg="cyan", bold=True))
        click.echo("="*60)
        click.echo("1. Manage Users")
        click.echo("2. Manage Expenses")
        click.echo("3. Manage Budgets")
        click.echo("4. View Reports")
        click.echo("5. Exit")
        click.echo("="*60)

        choice = click.prompt( "Select an option", type=click.Choice(["1", "2", "3", "4", "5"]))

        if choice == "1":
            user_menu()
        elif choice == "2":
            expense_menu()
        elif choice == "3":
            budget_menu()
        elif choice == "4":
            reports_menu()
        elif choice == "5":
            click.echo(click.style("\n Thank you for using Finance Tracker. Goodbye! 👋🏾"))
        break

def user_menu():
    while True:
        """user menu"""

        click.echo("\n" + "="*60)
        click.echo(click.style("  USER MANAGEMENT", fg="blue", bold=True))
        click.echo("="*60)
        click.echo("1. Create a user")
        click.echo("2. View all users")
        click.echo("3. Find user by name")
        click.echo("4. Find user by ID")
        click.echo("5. Update user")
        click.echo("6. Delete user")
        click.echo("7. Manage categories")
        click.echo("8. Back to main menu")
        click.echo("="*60)

        choice = click.prompt("Select an option",
            type=click.Choice(["1", "2", "3", "4", "5", "6", "7", "8"]))
        
        if choice == "1":
            # create user
            name = click.prompt("Enter user name")
            try:
                user = User.create(name)
                click.echo(click.style(f"Success: User {name} has been created", fg="green"))
            except Exception as exc:
                click.echo(click.style(f"Error: {exc}", fg="red"))

        elif choice == "2":
            # show users
            users = User.get_all()
            if not users:
                click.echo(click.style("No user found", fg="red"))
            else:
                click.echo(click.style("\n === ALL USERS ==="))
                for user in users:
                    click.echo(user)

        elif choice == "3":
            # find user by name
            name = click.prompt("Enter the user's name")
            user = User.find_by_name(name)
            if user:
                click.echo(click.style(f"{user}"))
            else:
                click.echo(click.style(f"User {user} not found", fg="red"))

        elif choice == "4":
            # find user by id
            user_id = click.prompt("Enter the user's ID", type=int)
            user = User.find_by_id(user_id)
            if user:
                click.echo(click.style(f"{user}", fg="green"))
            else:
                click.echo(click.style(f"User {user_id} not found", fg="red"))

        elif choice == "5":
            # update user information
            user_id = click.prompt("Enter the user's ID", type=int)
            user = User.find_by_id(user_id)
            if not user:
                 click.echo(click.style(f"User {user_id} not found", fg="red"))
            else:
                try:
                    name = click.prompt("Enter the user's new name")
                    user.update(name)
                    click.echo(click.style(f" Success, user has been updated to {user} ", fg="green"))
                except Exception as exc:
                    click.echo(click.style(f"Error {exc} ", fg="red"))

        elif choice == "6":
            # delete user
            user_id = click.prompt("Enter the user's id", type=int)
            user = User.find_by_id(user_id)
            if user:
                if click.confirm(f"Delete user {user.name}?"):
                    user.delete()
                    click.echo(click.style(f"User {user_id} deleted", fg="green"))
                else:
                    click.echo(click.style("Deletion has been cancelled"))
            else:
                click.echo(click.style(f"User {user} not found"))

        elif choice == "7":
            category_menu()

        elif choice == "8":
            break


def category_menu():
    user_id = click.prompt("Enter user ID", type=int)
    user = User.find_by_id(user_id)
    if not user:
        click.echo(click.style(f"User {user_id} not found"))
        return
    
    while True:
        click.echo("\n" + "="*60)
        click.echo(click.style(f"  CATEGORY MENU - {user.name}", fg="blue", bold=True))
        click.echo("="*60)
        click.echo("1. Create a category")
        click.echo("2. View all categories")
        click.echo("3. Back to main menu")
        click.echo("="*60)

        choice = click.prompt(
            "Select an option",
            type=click.Choice(["1", "2", "3"])
        )

        if choice == "1":
            # create a category
            name = click.prompt("Enter category name")
            try:
                category = Category.create(name, user.id)
                click.echo(click.style(f"Success: {category} has been created", fg="green"))
            except Exception as exc:
                click.echo(click.style(f"Error: {exc}"))

        elif choice == "2":
            # list all categories
            categories = Category.get_all(user.id)
            if not categories:
                click.echo("No categories found")
            else:
                click.echo(f"\nCATEGORES FOR {user.name}")
                for cat in categories:
                    click.echo(cat)

        elif choice == "3":
            break

def expense_menu():
    user_id = click.prompt("Enter user ID", type=int)
    user = User.find_by_id(user_id)
    if not user:
        click.echo(click.style(f"❌ User {user_id} not found", fg="red"))
        return
    
    while True:
        click.echo("\n" + "="*60)
        click.echo(click.style(f"  EXPENSE MANAGEMENT - {user.name}", fg="green", bold=True))
        click.echo("="*60)
        click.echo("1. Add an expense")
        click.echo("2. View all expenses")
        click.echo("3. View expenses by category")
        click.echo("4. Delete an expense")
        click.echo("5. Back to main menu")
        click.echo("="*60)
        
        choice = click.prompt(
            "Select an option",
            type=click.Choice(["1", "2", "3", "4", "5"])
        )

        if choice == "1":
            # add an expense
            categories = Category.get_all(user.id)
            if not categories:
                click.echo(click.style("❌ No categories found. Create one first!", fg="red"))
                continue

            click.echo("\nAvailable categories")
            for i, cat in enumerate(categories, 1):
                click.echo(f"{i}. {cat.name}")

            try:
                cat_choice = click.prompt("Select category number", type=int)
                if cat_choice < 1 or cat_choice > len(categories):
                    click.echo(click.style("Invalid category selected, please try again", fg="red"))
                    continue
                
                category = categories[cat_choice - 1]
                description = click.prompt("Enter expense descritpion")
                amount = click.promp("Enter amount", type=float)

                expense = Expense.create(description, amount, category.id, user.id)
                click.echo(click.style(f"Success: {expense} added", fg="green"))
            except Exception as exc:
                click.echo(click.style(f"Error: {exc}"))

        elif choice == "2":
            # list all expenses
            expenses = Expense.get_all(user.id)
            if not expenses:
                click.echo(click.style("No expenses found"))
            else:
                click.echo(click.style(f"ALL EXPENSES FOR {user.name}"))
                total = 0
                for exp in expenses:
                    click.echo(f"ID: {exp.id} | {exp.description} | ${exp.amount:.2f} | Category: {exp.category.name}")
                    total += exp.amount
                click.echo(click.style(f"TOTAL: {total:.2f} KSH", fg="green", bold=True))

        elif choice == "3":
            # view all expenses by category
            categories = Category.get_all(user.id)
            if not categories:
                click.echo("No categories found")
                continue

            click.echo("\nAvailable categories:")
            for i, cat in enumerate(categories, 1):
                click.echo(f"{i}. {cat.name}")

            try:
                cat_choice = click.prompt("Select category number", type=int)
                if cat_choice < 1 or cat_choice > len(categories):
                    click.echo(click.style("Invalid category selected. Please try again."))
                    continue

                category = categories[cat_choice - 1]
                expenses = Expense.get_by_category(category.id, user.id)

                if not expenses:
                    click.echo(click.style(f"No expenses found in {category.name}"))
                else:
                    click.echo(click.style(f"\nEXPENSES IN {category.name}"))
                    total = 0
                    for exp in expenses:
                        click.echo((f"ID: {exp.id} | {exp.description} | {exp.amount:.2f} KSH"))
                        total += exp.amount
                    click.echo(click.style(f"TOTAL: {total:.2f} KSH", fg="green", bold=True))
            except Exception as exc:
                click.echo(click.style(f"Error: {exc}"))

        elif choice == "4":
            # delete expense
            expenses = Expense.get_all(user.id):
            if not expenses:
                click.echo(click.style("No expenses to delete"))
                continue

            click.echo("\nYour expenses")
            for i, exp in enumerate(expense, 1):
                click.echo(f"{i}. {exp.description} - ${exp.amount:.2f}")

            try:
                exp_choice = click.prompt("Select expense number to delete", type=int)
                if exp_choice < 1 or exp_choice > len(expenses):
                    click.echo(click.style("Invalid selection"))
                    continue

                expenses = expenses[exp_choice - 1]
                if click.confirm(f"Delete '{expense.description}'?"):
                    expense.delete()
                    click.echo(click.style("Expense deleted successfully", fg="green"))
                else:
                    click.echo("Deletion cancelled")

            except Exception as exc:
                click.echo(f"Error: {exc}")

        elif choice == "5":
            break
        




if __name__ == "__main__":
    menu()
