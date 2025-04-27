import unittest
from bank.bank_system import BankSystem

class TestBankSystem(unittest.TestCase):
    def setUp(self):
        self.bank = BankSystem()
        self.acc = self.bank.create_account(1, "Bob", "1234")

    def test_create_and_get_account(self):
        acc = self.bank.get_account(1)
        self.assertIsNotNone(acc)
        self.assertEqual(acc.name, "Bob")

    def test_duplicate_account(self):
        with self.assertRaises(ValueError):
            self.bank.create_account(1, "Charlie", "5678")

    def test_delete_account(self):
        self.bank.delete_account(1)
        self.assertIsNone(self.bank.get_account(1))

    def test_authenticate(self):
        self.assertTrue(self.bank.authenticate(1, "1234"))
        self.assertFalse(self.bank.authenticate(1, "wrongpin"))

if __name__ == '__main__':
    unittest.main()
