from __init__ import CURSOR, CONN
from datetime import datetime


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
        sql = """DROP IF EXISTS expenses"""
    
