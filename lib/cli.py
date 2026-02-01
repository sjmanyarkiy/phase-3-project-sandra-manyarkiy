#!/usr/bin/env python3

import click

from models.user import User
from models.category import Category
from models.expense import Expense
from models.budget import Budget

click.command()
def menu():
    """==== FINANCE TRACKER ===="""

    while True:
        click.echo("\n" + "=*60")
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
            click.echo(click.style("\n👋 Thank you for using Finance Tracker. Goodbye!", fg="yellow"))
        break

    