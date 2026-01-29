from config import CURSOR, CONN
from datetime import datetime
from .category import Category
from .user import User


class Expense:

    all = {}

    def __init__(self, description, amount, category_id, user_id, id=None, date=None):
        self.id = id
        self.description = description
        self.amount = amount
        self.category_id = category_id
        self.user_id = user_id
        self.date = date or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __repr__(self):
        return f"<Expense {self.id}: {self.description} - ${self.amount}>"
    
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description):
        if isinstance(description, str) and len(description):
            self._description = description
        else:
            raise ValueError("description must be a non-empty string")
        
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            self._amount = amount
        else:
            raise ValueError("amount must be a positive number")

    @property
    def category_id(self):
        return self._category_id
    
    @category_id.setter
    def category_id(self, category_id):
        if type(category_id) is int and Category.find_by_id(category_id):
            self._category_id = category_id
        else:
            raise ValueError("category id must exist in the category table")

    @property
    def user_id(self):
        return self._user_id
    
    @user_id.setter
    def user_id(self, user_id):
        if type(user_id) is int and User.find_by_id(user_id):
            self._user_id = user_id
        else:
            raise ValueError("user_id must exist in the user table")

    
    @classmethod
    def create_table(cls):
        sql = """CREATE TABLE IF NOT EXISTS expenses (

            id INTEGER PRIMARY KEY,
            description TEXT,
            amount INTEGER,
            category_id INTEGER,
            user_id INTEGER,
            date TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (category_id) REFERENCES categories(id)
        
        )"""

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """DROP TABLE IF EXISTS expenses"""

        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """INSERT INTO expenses (description, amount, date, category_id, user_id) VALUES (?, ?, ?, ?, ?)"""

        CURSOR.execute(sql, (self.description, self.amount, self.date, self.category_id, self.user_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self, description, amount):
        sql = """UPDATE expenses SET description = ?, amount = ? WHERE id = ?"""

        CURSOR.execute(sql, (description, amount, self.id))
        CONN.commit()
        self.description = description
        self.amount = amount

    def delete(self):
        sql = """DELETE FROM expenses WHERE id = ?"""

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, description, amount, category_id, user_id):
        expense = cls(description, amount, category_id, user_id)
        expense.save()
        return expense
    
    @classmethod
    def instance_from_db(cls, row):
        expense = cls.all.get(row[0])

        if expense:
            expense.description = row[1]
            expense.amount = row[2]
            expense.date = row[3]
            expense.category_id = row[4]
            expense._user_id = row[5]
        else:
            expense = cls(row[1], row[2], row[4], row[5], row[0], row[3])
            cls.all[expense.id] = expense
        return expense
    
    @classmethod
    def get_all(cls, user_id):
        sql = """SELECT * FROM expenses WHERE user_id = ?"""

        rows = CURSOR.execute(sql, (user_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, expense_id):
        sql = "SELECT * FROM expenses WHERE id = ?"
        row = CURSOR.execute(sql, (expense_id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def get_by_category(cls, category_id, user_id):
        sql = "SELECT * FROM expenses WHERE category_id = ? AND user_id = ?"
        rows = CURSOR.execute(sql, (category_id, user_id)).fetchall()
        return [cls.instance_from_db(row) for row in rows]

        

    
    
