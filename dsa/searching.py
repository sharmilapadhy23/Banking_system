# dsa/searching.py

def binary_search(accounts, target_acc_number, key=lambda x: x.acc_number):
    """
    Performs binary search on a sorted list of accounts.
    Returns the account if found, else None.
    """
    left, right = 0, len(accounts) - 1
    while left <= right:
        mid = (left + right) // 2
        acc_number = key(accounts[mid])
        if acc_number == target_acc_number:
            return accounts[mid]
        elif acc_number < target_acc_number:
            left = mid + 1
        else:
            right = mid - 1
    return None
