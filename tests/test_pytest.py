import pytest
from src.bank_account import BankAccount
import unittest

@pytest.mark.parametrize("ammount, expected", [
     (100, 1100),
     (3000, 4000),
     (4500, 5500)
])
def test_deposit_varios_ammounts(ammount, expected):
    account = BankAccount(balance=1000, log_file="transactions.txt")
    new_balance = account.deposit(ammount)
    assert new_balance == expected



