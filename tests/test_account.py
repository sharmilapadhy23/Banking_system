import unittest
from bank.account import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(1, "Alice", "dummyhash", 100.0)

    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150.0)

    def test_withdraw(self):
        self.account.withdraw(30)
        self.assertEqual(self.account.balance, 70.0)

    def test_withdraw_insufficient(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(200)

    def test_deposit_negative(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-10)

    def test_transaction_history(self):
        self.account.deposit(10)
        self.assertIn("Deposited: 10", self.account.transactions)

if __name__ == '__main__':
    unittest.main()
