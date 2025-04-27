# bank/transaction.py

class Transaction:
    def __init__(self, tx_type: str, amount: float, src_acc: int, dest_acc: int = None):
        self.tx_type = tx_type  # 'deposit', 'withdraw', 'transfer'
        self.amount = amount
        self.src_acc = src_acc
        self.dest_acc = dest_acc
        self.status = "pending"
