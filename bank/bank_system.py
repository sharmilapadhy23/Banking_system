# bank/bank_system.py

from bank.account import BankAccount
import bcrypt

class BankSystem:
    def __init__(self):
        self.accounts = {}  # Dictionary for fast account lookup

    def create_account(self, acc_number: int, name: str, pin: str):
        if acc_number in self.accounts:
            raise ValueError("Account number already exists.")
        pin_hash = bcrypt.hashpw(pin.encode(), bcrypt.gensalt()).decode()
        account = BankAccount(acc_number, name, pin_hash)
        self.accounts[acc_number] = account
        return account

    def delete_account(self, acc_number: int):
        if acc_number not in self.accounts:
            raise ValueError("Account not found.")
        del self.accounts[acc_number]

    def get_account(self, acc_number: int):
        return self.accounts.get(acc_number)

    def authenticate(self, acc_number: int, pin: str):
        account = self.get_account(acc_number)
        if not account:
            return False
        return bcrypt.checkpw(pin.encode(), account.pin_hash.encode())
