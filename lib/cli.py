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



if __name__ == "__main__":
    menu()
