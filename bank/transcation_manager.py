# bank/transaction_manager.py

from collections import deque

class TransactionManager:
    def __init__(self):
        self.pending_transactions = deque()  # Queue for batch processing

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def process_next(self, bank_system):
        if not self.pending_transactions:
            return None
        tx = self.pending_transactions.popleft()
        # Process transaction (simplified)
        try:
            src_acc = bank_system.get_account(tx.src_acc)
            if tx.tx_type == 'deposit':
                src_acc.deposit(tx.amount)
                tx.status = "completed"
            elif tx.tx_type == 'withdraw':
                src_acc.withdraw(tx.amount)
                tx.status = "completed"
            elif tx.tx_type == 'transfer':
                dest_acc = bank_system.get_account(tx.dest_acc)
                src_acc.withdraw(tx.amount)
                dest_acc.deposit(tx.amount)
                tx.status = "completed"
            else:
                tx.status = "failed"
        except Exception as e:
            tx.status = f"failed: {e}"
        return tx
