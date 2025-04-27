# dsa/sorting.py

def merge_sort(accounts, key=lambda x: x.balance):
    """
    Sorts a list of accounts based on a key (default: balance) using merge sort.
    Returns a new sorted list.
    """
    if len(accounts) <= 1:
        return accounts
    mid = len(accounts) // 2
    left = merge_sort(accounts[:mid], key)
    right = merge_sort(accounts[mid:], key)
    return merge(left, right, key)

def merge(left, right, key):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
