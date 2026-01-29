"""
Test cases for Finance Tracker CLI
Run with: python -m pytest tests.py -v
Or run with: python tests.py
"""

import sys
import os

# from db.models import User, Category, Expense, Budget

from config import CURSOR, CONN
from models.user import User
from models.category import Category
from models.expense import Expense
from models.budget import Budget

# ==================== SETUP & TEARDOWN ====================

def setup_test_db():
    """Create test database tables"""
    User.create_table()
    Category.create_table()
    Expense.create_table()
    Budget.create_table()

def teardown_test_db():
    """Drop all test tables"""
    User.drop_table()
    Category.drop_table()
    Expense.drop_table()
    Budget.drop_table()
    User.all.clear()
    Category.all.clear()
    Expense.all.clear()
    Budget.all.clear()

# ==================== USER TESTS ====================

def test_user_create():
    """Test creating a new user"""
    setup_test_db()
    user = User.create("John Doe")
    
    assert user.id is not None
    assert user.name == "John Doe"
    assert user.id in User.all
    print("✅ test_user_create passed")
    teardown_test_db()

def test_user_find_by_id():
    """Test finding a user by ID"""
    setup_test_db()
    user1 = User.create("John")
    found_user = User.find_by_id(user1.id)
    
    assert found_user is not None
    assert found_user.name == "John"
    assert found_user.id == user1.id
    print("✅ test_user_find_by_id passed")
    teardown_test_db()

def test_user_find_by_name():
    """Test finding a user by name"""
    setup_test_db()
    user1 = User.create("Alice")
    found_user = User.find_by_name("Alice")
    
    assert found_user is not None
    assert found_user.name == "Alice"
    print("✅ test_user_find_by_name passed")
    teardown_test_db()

def test_user_get_all():
    """Test getting all users"""
    setup_test_db()
    User.create("User1")
    User.create("User2")
    User.create("User3")
    
    all_users = User.get_all()
    assert len(all_users) == 3
    print("✅ test_user_get_all passed")
    teardown_test_db()

def test_user_update():
    """Test updating a user"""
    setup_test_db()
    user = User.create("Original")
    user.update("Updated")
    
    found_user = User.find_by_id(user.id)
    assert found_user.name == "Updated"
    print("✅ test_user_update passed")
    teardown_test_db()

def test_user_delete():
    """Test deleting a user"""
    setup_test_db()
    user = User.create("DeleteMe")
    user_id = user.id
    
    user.delete()
    found_user = User.find_by_id(user_id)
    
    assert found_user is None
    assert user_id not in User.all
    print("✅ test_user_delete passed")
    teardown_test_db()

def test_user_name_validation():
    """Test user name validation"""
    setup_test_db()
    user = User("Valid")
    
    try:
        user.name = ""
        assert False, "Should raise ValueError for empty name"
    except ValueError as e:
        assert "non-empty string" in str(e)
    
    try:
        user.name = 123
        assert False, "Should raise ValueError for non-string"
    except ValueError as e:
        assert "non-empty string" in str(e)
    
    print("✅ test_user_name_validation passed")
    teardown_test_db()

# ==================== CATEGORY TESTS ====================

def test_category_create():
    """Test creating a new category"""
    setup_test_db()
    user = User.create("John")
    category = Category.create("Food", user.id)
    
    assert category.id is not None
    assert category.name == "Food"
    assert category.user_id == user.id
    print("✅ test_category_create passed")
    teardown_test_db()

def test_category_find_by_id():
    """Test finding a category by ID"""
    setup_test_db()
    user = User.create("John")
    cat1 = Category.create("Transport", user.id)
    found_cat = Category.find_by_id(cat1.id)
    
    assert found_cat is not None
    assert found_cat.name == "Transport"
    print("✅ test_category_find_by_id passed")
    teardown_test_db()

def test_category_find_by_name():
    """Test finding a category by name"""
    setup_test_db()
    user = User.create("John")
    Category.create("Entertainment", user.id)
    found_cat = Category.find_by_name("Entertainment", user.id)
    
    assert found_cat is not None
    assert found_cat.name == "Entertainment"
    print("✅ test_category_find_by_name passed")
    teardown_test_db()

def test_category_get_all():
    """Test getting all categories for a user"""
    setup_test_db()
    user = User.create("John")
    Category.create("Food", user.id)
    Category.create("Transport", user.id)
    Category.create("Entertainment", user.id)
    
    categories = Category.get_all(user.id)
    assert len(categories) == 3
    print("✅ test_category_get_all passed")
    teardown_test_db()

def test_category_update():
    """Test updating a category"""
    setup_test_db()
    user = User.create("John")
    cat = Category.create("OldName", user.id)
    cat.update("NewName")
    
    found_cat = Category.find_by_id(cat.id)
    assert found_cat.name == "NewName"
    print("✅ test_category_update passed")
    teardown_test_db()

def test_category_delete():
    """Test deleting a category"""
    setup_test_db()
    user = User.create("John")
    cat = Category.create("DeleteMe", user.id)
    cat_id = cat.id
    
    cat.delete()
    found_cat = Category.find_by_id(cat_id)
    
    assert found_cat is None
    print("✅ test_category_delete passed")
    teardown_test_db()

def test_category_name_validation():
    """Test category name validation"""
    setup_test_db()
    user = User.create("John")
    cat = Category("Valid", user.id)
    
    try:
        cat.name = ""
        assert False, "Should raise ValueError for empty name"
    except ValueError as e:
        assert "non-empty string" in str(e)
    
    print("✅ test_category_name_validation passed")
    teardown_test_db()

# ==================== EXPENSE TESTS ====================

def test_expense_create():
    """Test creating a new expense"""
    setup_test_db()
    user = User.create("John")
    cat = Category.create("Food", user.id)
    expense = Expense.create("Groceries", 50.00, cat.id, user.id)
    
    assert expense.id is not None
    assert expense.description == "Groceries"
    assert expense.amount == 50.00
    assert expense.category_id == cat.id
    print("✅ test_expense_create passed")
    teardown_test_db()

def test_expense_find_by_id():
    """Test finding an expense by ID"""
    setup_test_db()
    user = User.create("John")
    cat = Category.create("Transport", user.id)
    exp1 = Expense.create("Gas", 45.00, cat.id, user.id)
    found_exp = Expense.find_by_id(exp1.id)
    
    assert found_exp is not None
    assert found_exp.description == "Gas"
    assert found_exp.amount == 45.00
    print("✅ test_expense_find_by_id passed")
    teardown_test_db()

def test_expense_get_all():
    """Test getting all expenses for a user"""
    setup_test_db()
    user = User.create("John")
    cat = Category.create("Food", user.id)
    
    Expense.create("Pizza", 15.00, cat.id, user.id)
    Expense.create("Burger", 12.00, cat.id, user.id)
    Expense.create("Sushi", 25.00, cat.id, user.id)
    
    expenses = Expense.get_all(user.id)
    assert len(expenses) == 3
    print("✅ test_expense_get_all passed")
    teardown_test_db()

def test_expense_get_by_category():
    """Test getting expenses by category"""
    setup_test_db()
    user = User.create("John")
    food_cat = Category.create("Food", user.id)
    transport_cat = Category.create("Transport", user.id)
    
    Expense.create("Pizza", 15.00, food_cat.id, user.id)
    Expense.create("Gas", 45.00, transport_cat.id, user.id)
    Expense.create("Burger", 12.00, food_cat.id, user.id)
    
    food_expenses = Expense.get_by_category(food_cat.id, user.id)
    assert len(food_expenses) == 2
    assert all(exp.category_id == food_cat.id for exp in food_expenses)
    print("✅ test_expense_get_by_category passed")
    teardown_test_db()

def test_expense_update():
    """Test updating an expense"""
    setup_test_db()
    user = User.create("John")
    cat = Category.create("Food", user.id)
    exp = Expense.create("Pizza", 15.00, cat.id, user.id)
    
    exp.update("Sushi", 25.00)
    found_exp = Expense.find_by_id(exp.id)
    
    assert found_exp.description == "Sushi"
    assert found_exp.amount == 25.00
    print("✅ test_expense_update passed")
    teardown_test_db()

def test_expense_delete():
    """Test deleting an expense"""
    setup_test_db()
    user = User.create("John")
    cat = Category.create("Food", user.id)
    exp = Expense.create("DeleteMe", 10.00, cat.id, user.id)
    exp_id = exp.id
    
    exp.delete()
    found_exp = Expense.find_by_id(exp_id)
    
    assert found_exp is None
    print("✅ test_expense_delete passed")
    teardown_test_db()

def test_expense_amount_validation():
    """Test expense amount validation"""
    setup_test_db()
    user = User.create("John")
    cat = Category.create("Food", user.id)
    exp = Expense("Pizza", 15.00, cat.id, user.id)
    
    try:
        exp.amount = -10
        assert False, "Should raise ValueError for negative amount"
    except ValueError as e:
        assert "positive number" in str(e)
    
    try:
        exp.amount = 0
        assert False, "Should raise ValueError for zero"
    except ValueError as e:
        assert "positive number" in str(e)
    
    print("✅ test_expense_amount_validation passed")
    teardown_test_db()

def test_expense_description_validation():
    """Test expense description validation"""
    setup_test_db()
    user = User.create("John")
    cat = Category.create("Food", user.id)
    exp = Expense("Pizza", 15.00, cat.id, user.id)
    
    try:
        exp.description = ""
        assert False, "Should raise ValueError for empty description"
    except ValueError as e:
        assert "non-empty string" in str(e)
    
    print("✅ test_expense_description_validation passed")
    teardown_test_db()

# ==================== BUDGET TESTS ====================

def test_budget_create():
    """Test creating a new budget"""
    setup_test_db()
    user = User.create("John")
    cat = Category.create("Food", user.id)
    budget = Budget.create(300.00, "January 2025", cat.id, user.id)
    
    assert budget.id is not None
    assert budget.monthly_limit == 300.00
    assert budget.month == "January 2025"
    print("✅ test_budget_create passed")
    teardown_test_db()

def test_budget_find_by_id():
    """Test finding a budget by ID"""
    setup_test_db()
    user = User.create("John")
    cat = Category.create("Transport", user.id)
    budget1 = Budget.create(200.00, "January 2025", cat.id, user.id)
    found_budget = Budget.find_by_id(budget1.id)
    
    assert found_budget is not None
    assert found_budget.monthly_limit == 200.00
    print("✅ test_budget_find_by_id passed")
    teardown_test_db()

def test_budget_find_by_category_and_month():
    """Test finding a budget by category and month"""
    setup_test_db()
    user = User.create("John")
    cat = Category.create("Food", user.id)
    Budget.create(300.00, "January 2025", cat.id, user.id)
    
    found_budget = Budget.find_by_category_and_month(cat.id, "January 2025", user.id)
    assert found_budget is not None
    assert found_budget.monthly_limit == 300.00
    print("✅ test_budget_find_by_category_and_month passed")
    teardown_test_db()

def test_budget_get_all():
    """Test getting all budgets for a user"""
    setup_test_db()
    user = User.create("John")
    cat1 = Category.create("Food", user.id)
    cat2 = Category.create("Transport", user.id)
    
    Budget.create(300.00, "January 2025", cat1.id, user.id)
    Budget.create(200.00, "January 2025", cat2.id, user.id)
    Budget.create(300.00, "February 2025", cat1.id, user.id)
    
    budgets = Budget.get_all(user.id)
    assert len(budgets) == 3
    print("✅ test_budget_get_all passed")
    teardown_test_db()

def test_budget_update():
    """Test updating a budget"""
    setup_test_db()
    user = User.create("John")
    cat = Category.create("Food", user.id)
    budget = Budget.create(300.00, "January 2025", cat.id, user.id)
    
    budget.update(500.00)
    found_budget = Budget.find_by_id(budget.id)
    
    assert found_budget.monthly_limit == 500.00
    print("✅ test_budget_update passed")
    teardown_test_db()

def test_budget_delete():
    """Test deleting a budget"""
    setup_test_db()
    user = User.create("John")
    cat = Category.create("Food", user.id)
    budget = Budget.create(300.00, "January 2025", cat.id, user.id)
    budget_id = budget.id
    
    budget.delete()
    found_budget = Budget.find_by_id(budget_id)
    
    assert found_budget is None
    print("✅ test_budget_delete passed")
    teardown_test_db()

def test_budget_monthly_limit_validation():
    """Test budget monthly_limit validation"""
    setup_test_db()
    user = User.create("John")
    cat = Category.create("Food", user.id)
    budget = Budget(300.00, "January 2025", cat.id, user.id)
    
    try:
        budget.monthly_limit = -100
        assert False, "Should raise ValueError for negative limit"
    except ValueError as e:
        assert "positive number" in str(e)
    
    try:
        budget.monthly_limit = 0
        assert False, "Should raise ValueError for zero"
    except ValueError as e:
        assert "positive number" in str(e)
    
    print("✅ test_budget_monthly_limit_validation passed")
    teardown_test_db()

# ==================== INTEGRATION TESTS ====================

def test_full_workflow():
    """Test a complete workflow: user → categories → expenses → budgets"""
    setup_test_db()
    
    # Create user
    user = User.create("Alice")
    assert user.id is not None
    
    # Create categories
    food_cat = Category.create("Food", user.id)
    transport_cat = Category.create("Transport", user.id)
    
    # Add expenses
    exp1 = Expense.create("Groceries", 50.00, food_cat.id, user.id)
    exp2 = Expense.create("Gas", 45.00, transport_cat.id, user.id)
    exp3 = Expense.create("Lunch", 15.00, food_cat.id, user.id)
    
    # Set budgets
    budget1 = Budget.create(300.00, "January 2025", food_cat.id, user.id)
    budget2 = Budget.create(200.00, "January 2025", transport_cat.id, user.id)
    
    # Verify relationships
    user_expenses = Expense.get_all(user.id)
    assert len(user_expenses) == 3
    
    food_expenses = Expense.get_by_category(food_cat.id, user.id)
    assert len(food_expenses) == 2
    total_food = sum(exp.amount for exp in food_expenses)
    assert total_food == 65.00
    
    user_budgets = Budget.get_all(user.id)
    assert len(user_budgets) == 2
    
    print("✅ test_full_workflow passed")
    teardown_test_db()

# ==================== RUN ALL TESTS ====================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("RUNNING FINANCE TRACKER TESTS")
    print("="*60 + "\n")
    
    # User tests
    test_user_create()
    test_user_find_by_id()
    test_user_find_by_name()
    test_user_get_all()
    test_user_update()
    test_user_delete()
    test_user_name_validation()
    
    # Category tests
    test_category_create()
    test_category_find_by_id()
    test_category_find_by_name()
    test_category_get_all()
    test_category_update()
    test_category_delete()
    test_category_name_validation()
    
    # Expense tests
    test_expense_create()
    test_expense_find_by_id()
    test_expense_get_all()
    test_expense_get_by_category()
    test_expense_update()
    test_expense_delete()
    test_expense_amount_validation()
    test_expense_description_validation()
    
    # Budget tests
    test_budget_create()
    test_budget_find_by_id()
    test_budget_find_by_category_and_month()
    test_budget_get_all()
    test_budget_update()
    test_budget_delete()
    test_budget_monthly_limit_validation()
    
    # Integration tests
    test_full_workflow()
    
    print("\n" + "="*60)
    print("✅ ALL TESTS PASSED!")
    print("="*60 + "\n")