class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []

    def add_account(self, account): #método para agregar una cuenta a la lista de cuentas del usuario
        self.accounts.append(account)
    
    def get_total_balance(self):    #método obtner balance de todas las cuentas
        return sum(account.get_balance() for account in self.accounts)