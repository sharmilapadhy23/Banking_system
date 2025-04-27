# bank/transaction_history.py

class TransactionNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class TransactionHistory:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = TransactionNode(data)
        new_node.next = self.head
        self.head = new_node

    def get_all(self):
        current = self.head
        history = []
        while current:
            history.append(current.data)
            current = current.next
        return history[::-1]  # Return in chronological order
