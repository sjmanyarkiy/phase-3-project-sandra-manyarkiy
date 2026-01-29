from __init__ import CURSOR, CONN

class Category:

    all = {}

    def __init__(self, name, user_id, id = None):
        self.id = id
        self.name = name
        self.user_id = user_id

    