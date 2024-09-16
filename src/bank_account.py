from src.exceptions import InsufficientFundsError, WithdrawalTimeRestrictionError, WithdrawalDayRestrictionError
from datetime import datetime

class BankAccount:
    def __init__(self, balance=0, log_file=None):
        self.balance = balance
        self.log_file = log_file
        self.log_transaction('Cuenta creada')
        
    def log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, mode='a') as f:
                f.write(f"{message}\n")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.log_transaction(f"Deposited {amount}.  New balance is: {self.balance}")
        return self.balance

    def withdraw(self, amount):
        now = datetime.now()    # obtenenmos hora actual
        if now.hour < 8 or now.hour > 17:  # si hora de retiro está por fuera del lapso lanzamos error o excepción
            raise WithdrawalTimeRestrictionError("Withdrawals are only allowed from 8am to 5pm.")
        
        if now.weekday() == 5 or now.weekday() == 6: # obtenemos dia actual
            raise WithdrawalDayRestrictionError("Withdrawals are only allowed from monday to friday")

        if amount > self.balance:
            raise InsufficientFundsError(
                f"Withdrawal of {amount} exceeds balance {self.balance}"
            )
        if amount > 0:
            self.balance -= amount
            self.log_transaction(f"Withdrawed {amount}.  New balance is: {self.balance}")
        return self.balance
    
    def get_balance(self):
        self.log_transaction(f"Checked balance.  Currente balance is: {self.balance}")
        return self.balance
    