from __init__ import CURSOR, CONN

class User:

    def __init__(self, name, id = None):
        self.id = id
        self.name = name

    def __repr__(self):
        return f'<User {self.id}: {self.name}>'
    

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a string")

    @classmethod   
    def create(self):
        sql = """CREATE TABLE IF NOT EXISTS users (

            id INTEGER PRIMARY KEY,
            name TEXT
        
        )"""

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop(self):
        sql = """DROP TABLE IF EXISTS users"""

        CURSOR.execute(sql)
        CONN.commit()

    def save(self, name):
        sql = """INSERT INTO users (name) VALUES (?)"""

        CURSOR.execute(sql, (name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
 
