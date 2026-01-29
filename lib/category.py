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
        
    