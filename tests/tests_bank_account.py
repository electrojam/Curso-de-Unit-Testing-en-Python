import unittest

from src.bank_account import BankAccount

class BankAccountTets(unittest.TestCase):   # Clase con métodos de prueba

    def setUp(self):
        self.account = BankAccount(balance = 1000)

    def test_deposit(self): # prueba depósito
        new_balance = self.account.deposit(500)
        assert new_balance == 1500

    def test_withdraw(self):    # prueba retiro
        new_balance = self.account.withdraw(200)
        assert new_balance == 800

    def test_get_balance(self): # prueba para obtener balance
        assert self.account.get_balance() == 1000