# Finance Tracker CLI Application

A command-line interface (CLI) application for managing personal finances, including tracking expenses, setting budgets, and managing spending categories.

## Features

- **User Management**: Create, view, update, and delete users
- **Category Management**: Organize expenses into categories
- **Expense Tracking**: Add, view, and delete expenses with amounts and dates
- **Budget Management**: Set monthly budgets per category and track spending against budgets
- **Financial Reports**: View spending summaries and budget vs actual spending reports

## Project Structure
```
fintrack/
├── lib/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── category.py
│   │   ├── expense.py
│   │   └── budget.py
│   ├── cli.py
│   ├── config.py
│   ├── debug.py
│   └── finance_tracker.db
├── init_db.py
├── Pipfile
├── Pipfile.lock
└── README.md
```

## Installation

1. Clone the repository and navigate to the project directory
2. Install dependencies:
```bash
   pipenv install
   pipenv shell
```

3. Initialize the database:
```bash
   python init_db.py
```

## Usage

Run the CLI application:
```bash
python lib/cli.py
```

### Main Menu Options

1. **Manage Users** - Create, view, update, delete users, and manage categories
2. **Manage Expenses** - Add, view, and delete expenses for a user
3. **Manage Budgets** - Set budgets, view budgets, and compare spending vs budgets
4. **View Reports** - Generate financial reports and summaries
5. **Exit** - Close the application

## Database Schema

### Users Table
- `id` (INTEGER PRIMARY KEY)
- `name` (TEXT UNIQUE NOT NULL)

### Categories Table
- `id` (INTEGER PRIMARY KEY)
- `name` (TEXT NOT NULL)
- `user_id` (INTEGER FOREIGN KEY)

### Expenses Table
- `id` (INTEGER PRIMARY KEY)
- `description` (TEXT NOT NULL)
- `amount` (INTEGER NOT NULL)
- `category_id` (INTEGER FOREIGN KEY)
- `user_id` (INTEGER FOREIGN KEY)
- `date` (TEXT)

### Budgets Table
- `id` (INTEGER PRIMARY KEY)
- `monthly_limit` (REAL NOT NULL)
- `month` (TEXT NOT NULL)
- `category_id` (INTEGER FOREIGN KEY)
- `user_id` (INTEGER FOREIGN KEY)

## Model Classes

### User
Manages user accounts and authentication.

**Methods:**
- `create(name)` - Create a new user
- `find_by_id(user_id)` - Find user by ID
- `find_by_name(name)` - Find user by name
- `get_all()` - Get all users
- `update(name)` - Update user name
- `delete()` - Delete user

### Category
Organizes expenses into categories.

**Methods:**
- `create(name, user_id)` - Create a new category
- `find_by_id(category_id)` - Find category by ID
- `find_by_name(name, user_id)` - Find category by name for a user
- `get_all(user_id)` - Get all categories for a user
- `update(name)` - Update category name
- `delete()` - Delete category

### Expense
Tracks individual expenses.

**Methods:**
- `create(description, amount, category_id, user_id)` - Create a new expense
- `find_by_id(expense_id)` - Find expense by ID
- `get_all(user_id)` - Get all expenses for a user
- `get_by_category(category_id, user_id)` - Get expenses by category
- `update(description, amount)` - Update expense details
- `delete()` - Delete expense

### Budget
Manages monthly spending budgets.

**Methods:**
- `create(monthly_limit, month, category_id, user_id)` - Create a new budget
- `find_by_id(budget_id)` - Find budget by ID
- `find_by_category_and_month(category_id, month, user_id)` - Find budget by category and month
- `get_all(user_id)` - Get all budgets for a user
- `update(monthly_limit)` - Update budget limit
- `delete()` - Delete budget

## Key Features

### Input Validation
- All user inputs are validated before being saved to the database
- Property setters enforce data type and value constraints
- Error messages provide feedback on validation failures

### User-Friendly Interface
- Color-coded menu system using Click library
- Clear prompts and confirmations for destructive operations
- Formatted output with proper spacing and alignment

### Data Persistence
- SQLite database for reliable data storage
- Foreign key relationships maintain data integrity
- Transaction commits ensure data consistency

## Technologies Used

- **Python 3.8+** - Programming language
- **SQLite** - Database
- **Click** - CLI framework
- **SQLAlchemy patterns** - ORM design patterns (without the full framework)

## Development Workflow

1. Create or modify a model class
2. Update the corresponding ORM methods (create, read, update, delete)
3. Test the model in the CLI
4. Add validation with property setters
5. Commit changes to git

## Future Enhancements

- Export financial reports to CSV or PDF
- Monthly recurring expenses
- Budget alerts and notifications
- Multi-currency support
- Data visualization charts
- User authentication and login
- Web interface using Flask or Django

## Author

Created as a Phase 3 project for learning Python ORM patterns and CLI design.