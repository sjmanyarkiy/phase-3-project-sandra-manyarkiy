#!/usr/bin/env python3

import sys
import os

from models.user import User
from models.category import Category
from models.expense import Expense
from models.budget import Budget

def seed_database():
    #create tables
    User.create_table()
    Category.create_table()
    Expense.create_table()
    Budget.create_table()

    #sample user
    user = User.create("Alex Dunphy")

    #sample categories
    rent = Category.create("Rent", user.id)
    food = Category.create("Food", user.id)
    transport = Category.create("Transport", user.id)
    entertainment = Category.create("Entertainment", user.id)

    # sample expenses
    exp1 = Expense.create("Rent", 12000, rent.id, user.id)
    exp2 = Expense.create("Groceries", 6000, food.id, user.id)
    exp3 = Expense.create("Fuel", 4500, transport.id, user.id)
    exp4 = Expense.create("Sherehe", 3000, entertainment.id, user.id)

    # sample budget
    budget = Budget.create(20000, "January 2026", food.id, user.id)


if __name__ == "__main__":
    seed_database()