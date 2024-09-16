import unittest, os
from unittest.mock import patch
from src.exceptions import InsufficientFundsError, WithdrawalTimeRestrictionError
from src.bank_account import BankAccount

class BankAccountTests(unittest.TestCase):   # Clase con métodos de prueba

    def setUp(self):    # método a ejecutar antes de cada prueba
        self.account = BankAccount(balance = 1000, log_file="log_transaction.txt")

    def tearDown(self): # método a ejecutar despúes de cada prueba
        if os.path.exists(self.account.log_file):   # miramos si archivo log existe
            os.remove(self.account.log_file)

    def count_lines(self, filename):    # Método para contar líneas del log (este método no es prueba)
        with open(filename, "r") as f:
            return len(f.readlines())

    def test_deposit(self): # prueba depósito
        new_balance = self.account.deposit(500)
        self.assertEqual(new_balance, 1500, "Balance is not iqual")

    def test_withdraw(self):    # prueba retiro
        new_balance = self.account.withdraw(200)
        self.assertEqual(new_balance, 800, "Balance is not iqual")

    def test_get_balance(self): # prueba para obtener balance
        self.assertEqual(self.account.get_balance(), 1000)

    def test_log_transaction(self): # Prueba de creación del log
        self.account.deposit(500)
        self.assertTrue(os.path.exists(self.account.log_file)) # Miramos si el archivo log existe

    def test_count_transactions(self):  # Probamos método count_lines
        assert self.count_lines(self.account.log_file) == 1
        self.account.deposit(500)
        assert self.count_lines(self.account.log_file) == 2
    
    def test_withdraw_raises_error_when_insuffcient_funds(self):
        with self.assertRaises(InsufficientFundsError):
            self.account.withdraw(2000)
    
    @patch("src.bank_account.datetime")
    def test_withdraw_during_business_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        new_balance = self.account.withdraw(100)
        self.assertEqual(new_balance, 900)

    @patch("src.bank_account.datetime")
    def test_withdraw_disallow_before_business_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 7
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(100)

    @patch("src.bank_account.datetime")
    def test_withdraw_disallow_after_business_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 18
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(100)