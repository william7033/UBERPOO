from account import Account

class user(Account):
    def __init__(self, name,
    document, email, passaword):
    super().__init__(name, document, email, 
    passaword)