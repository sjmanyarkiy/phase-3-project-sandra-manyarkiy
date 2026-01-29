class Budget:
    
    all = {}

    def __init__(self, monthly_limit, month, category_id, user_id, id=None):
        self.id = id
        self.monthly_limit = monthly_limit
        self.month = month
        self.category_id = category_id
        self.user_id = user_id