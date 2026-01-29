from __init__ import CURSOR, CONN

class User:

    all = {}

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

    def save(self):
        sql = """INSERT INTO users (name) VALUES (?)"""

        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """UPDATE users SET name = ? WHERE id = ?"""

        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    def delete(self):
        sql = """DELETE * FROM users WHERE ID = ?"""

        CURSOR.execute(sql, (self.id))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create_user(cls, name):
        user = cls(name)
        user.save()
        return user
    
    @classmethod
    def instance_from_db(cls, row):
        user = cls.all.get(row[0])

        if user:
            user.name = row[1]
        else:
            user = cls(row[1])
            user.id = row[0]
            cls.all[user.id] = user
        return user
    
    @classmethod
    def get_all(cls):
        """Get all users"""
        sql = "SELECT * FROM users"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, user_id):
        """Find user by ID"""
        sql = "SELECT * FROM users WHERE id = ?"
        row = CURSOR.execute(sql, (user_id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        """Find user by name"""
        sql = "SELECT * FROM users WHERE name = ?"
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
        
 
