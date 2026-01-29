from __init__ import CURSOR, CONN
from user import User

class Category:

    all = {}

    def __init__(self, name, user_id, id = None):
        self.id = id
        self.name = name
        self.user_id = user_id

    def __repr__(self):
        return f"<Category {self.id}: {self.name}>"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a string")
        
    @property
    def user_id(self):
        self._user_id

    @user_id.setter
    def user_id(self, user_id):
        if isinstance(user_id, int) and User.find_by_id(user_id):
            self._user_id = user_id
        else:
            raise ValueError("user_id must reference a user in the database")
        
    @classmethod
    def create_table(cls):
        sql = """CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            name TEXT,
            user_id INTEGERR,
            FOREIGN KEY (user_id) references users(id)
        
        )"""

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def delete_table(cls):
        sql = """DELETE TABLE IF EXISTS categories"""

        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """INSERT INTO categories (name, user_id) VALUES (?, ?)"""


        CURSOR.execute(sql, (self.name, self.user_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """UPDATE categories SET name = ?, user_id = ? WHERE id = ?"""

        CURSOR.execute(sql, (self.name, self.user_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """DELETE * FROM categories WHERE id = ?"""

        CURSOR.execute(sql, (self.id))
        CONN.commit()

    @classmethod
    def create_category(cls, name, user_id):
        category = cls(name, user_id)
        category.save()
        return category
    
    @classmethod
    def instance_from_db(cls, row):

        category = cls.all.get(row[0])

        if category:
            category.name = row[1]
            category.user_id = row[2]
        else:
            category = cls(row[1], row[2])
            category.id = row[0]
            category.all[category.id] = category

        return category
    
    @classmethod
    def find_by_id(cls):





    
        
    