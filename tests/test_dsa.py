import unittest
from dsa.sorting import merge_sort
from dsa.searching import binary_search
from dsa.linked_list import LinkedList

class DummyAccount:
    def __init__(self, acc_number, balance):
        self.acc_number = acc_number
        self.balance = balance

class TestDSA(unittest.TestCase):
    def setUp(self):
        self.accounts = [
            DummyAccount(3, 300.0),
            DummyAccount(1, 100.0),
            DummyAccount(2, 200.0)
        ]

    def test_merge_sort(self):
        sorted_accounts = merge_sort(self.accounts, key=lambda x: x.balance)
        balances = [acc.balance for acc in sorted_accounts]
        self.assertEqual(balances, [100.0, 200.0, 300.0])

    def test_binary_search(self):
        sorted_accounts = merge_sort(self.accounts, key=lambda x: x.acc_number)
        acc = binary_search(sorted_accounts, 2)
        self.assertIsNotNone(acc)
        self.assertEqual(acc.acc_number, 2)
        self.assertIsNone(binary_search(sorted_accounts, 99))

    def test_linked_list(self):
        ll = LinkedList()
        ll.insert_at_end(10)
        ll.insert_at_end(20)
        ll.insert_at_beginning(5)
        self.assertEqual(ll.to_list(), [5, 10, 20])

if __name__ == '__main__':
    unittest.main()
