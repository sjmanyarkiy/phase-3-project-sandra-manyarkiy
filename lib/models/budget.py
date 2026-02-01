from config import CURSOR, CONN
from .category import Category
from .user import User

class Budget:
    
    all = {}

    def __init__(self, monthly_limit, month, category_id, user_id, id=None):
        self.id = id
        self.monthly_limit = monthly_limit
        self.month = month
        self.category_id = category_id
        self.user_id = user_id

    def __repr__(self):
        return f"<Budget {self.id}: {self.month} - ${self.monthly_limit}>"
    
    @property
    def monthly_limit(self):
        return self._monthly_limit

    @monthly_limit.setter
    def monthly_limit(self, monthly_limit):
        if isinstance(monthly_limit, (int, float)) and monthly_limit > 0:
            self._monthly_limit = monthly_limit
        else:
            raise ValueError("monthly_limit must be a positive number")
        
    @property
    def category_id(self):
        return self._category_id
    
    @category_id.setter
    def category_id(self, category_id):
        if type(category_id) is int and Category.find_by_id(category_id):
            self._category_id = category_id
        else:
            raise ValueError("category_id must reference a category in the database")
        
    @property
    def user_id(self):
        return self._user_id
    
    @user_id.setter
    def user_id(self, user_id):
        if type(user_id) is int and User.find_by_id(user_id):
            self._user_id = user_id
        else:
            raise ValueError("user_id must reference a user in the database")
        
    @property
    def category(self):
        return Category.find_by_id(self.category_id)


    @classmethod
    def create_table(cls):
        sql = """CREATE TABLE IF NOT EXISTS budgets (
            id INTEGER PRIMARY KEY,
            monthly_limit INTEGER, 
            month TEXT, 
            category_id INTEGER, 
            user_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(id),
            FOREIGN KEY (user_id) REFERENCES users(id)
        )"""

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """DROP TABLE IF EXISTS budgets"""

        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """INSERT INTO budgets (monthly_limit, month, category_id, user_id) VALUES 
        (?, ?, ?, ?)"""

        CURSOR.execute(sql, (self.monthly_limit, self.month, self.category_id, self.user_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self, monthly_limit):
        sql = """UPDATE budgets SET monthly_limit = ? WHERE id = ?"""

        CURSOR.execute(sql, (monthly_limit, self.id))
        CONN.commit()

        self.monthly_limit = monthly_limit

    def delete(self):
        sql = """DELETE FROM budgets WHERE id = ?"""

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, monthly_limit, month, category_id, user_id):
        budget = cls(monthly_limit, month, category_id, user_id)
        budget.save()
        return budget
    

    @classmethod
    def instance_from_db(cls, row):

        budget = cls.all.get(row[0])
        if budget:
            budget.monthly_limit = row[1]
            budget.month = row[2]
            budget._category_id = row[3]
            budget._user_id = row[4]
        else:
            budget = cls(row[1], row[2], row[3], row[4])
            budget.id = row[0]
            cls.all[budget.id] = budget
        return budget
    
    @classmethod
    def get_all(cls, user_id):
        sql = """SELECT * FROM budgets WHERE user_id = ?"""

        rows = CURSOR.execute(sql, (user_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, budget_id):
        sql = """SELECT * FROM budgets WHERE id = ?"""

        row = CURSOR.execute(sql, (budget_id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_category_and_month(cls, category_id, month, user_id):
        sql = """SELECT * FROM budgets WHERE category_id = ? AND month = ? AND user_id = ?"""

        row = CURSOR.execute(sql, (category_id, month, user_id)).fetchone()
        return cls.instance_from_db(row) if row else None
