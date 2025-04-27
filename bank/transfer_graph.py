# bank/transfer_graph.py

from collections import defaultdict

class TransferGraph:
    def __init__(self):
        self.graph = defaultdict(list)  # Adjacency list

    def add_transfer(self, src_acc, dest_acc):
        self.graph[src_acc].append(dest_acc)

    def get_transfers(self, acc_number):
        return self.graph[acc_number]
