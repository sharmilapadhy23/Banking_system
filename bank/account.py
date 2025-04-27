# bank/account.py

class BankAccount:
    def __init__(self, acc_number: int, name: str, pin_hash: str, balance: float = 0.0):
        self.acc_number = acc_number
        self.name = name
        self.pin_hash = pin_hash
        self.balance = balance
        self.transactions = []  # List to store transaction history

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        self.transactions.append(f"Withdrew: {amount}")

    def add_transaction(self, description: str):
        self.transactions.append(description)
