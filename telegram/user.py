class User:
    def __init__(self, user_data):
        self.id = user_data['result']['id']
        self.first_name = user_data['result']['first_name']
        self.username = user_data['result']['username']
        
    def __str__(self):
        return f"I am {self.first_name} {self.username}"
    