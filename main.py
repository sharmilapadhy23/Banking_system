# main.py

from bank.bank_system import BankSystem
from bank.transcation import Transaction
from bank.transcation_manager import TransactionManager
from dsa.sorting import merge_sort

def main_menu():
    print("\n==== Banking System ====")
    print("1. Create Account")
    print("2. Login")
    print("3. List Accounts (sorted by balance)")
    print("4. Exit")
    return input("Select an option: ")

def account_menu():
    print("\n---- Account Menu ----")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Transfer")
    print("4. Show Transaction History")
    print("5. Logout")
    return input("Select an option: ")

def main():
    bank = BankSystem()
    tx_manager = TransactionManager()
    current_acc = None

    while True:
        if not current_acc:
            choice = main_menu()
            if choice == '1':
                try:
                    acc_number = int(input("Enter new account number: "))
                    name = input("Enter name: ")
                    pin = input("Set a 4-digit PIN: ")
                    acc = bank.create_account(acc_number, name, pin)
                    print(f"Account created for {name} (Acc #: {acc_number})")
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == '2':
                try:
                    acc_number = int(input("Enter account number: "))
                    pin = input("Enter PIN: ")
                    if bank.authenticate(acc_number, pin):
                        current_acc = bank.get_account(acc_number)
                        print(f"Welcome, {current_acc.name}!")
                    else:
                        print("Authentication failed.")
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == '3':
                accounts = list(bank.accounts.values())
                sorted_accounts = merge_sort(accounts, key=lambda x: x.balance)
                print("\nAccounts sorted by balance:")
                for acc in sorted_accounts:
                    print(f"Acc #: {acc.acc_number}, Name: {acc.name}, Balance: {acc.balance}")
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")
        else:
            choice = account_menu()
            if choice == '1':
                try:
                    amount = float(input("Deposit amount: "))
                    tx = Transaction('deposit', amount, current_acc.acc_number)
                    tx_manager.add_transaction(tx)
                    tx_manager.process_next(bank)
                    print(f"Deposited {amount}. New balance: {current_acc.balance}")
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == '2':
                try:
                    amount = float(input("Withdraw amount: "))
                    tx = Transaction('withdraw', amount, current_acc.acc_number)
                    tx_manager.add_transaction(tx)
                    tx_manager.process_next(bank)
                    print(f"Withdrew {amount}. New balance: {current_acc.balance}")
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == '3':
                try:
                    dest_acc_number = int(input("Transfer to account #: "))
                    amount = float(input("Amount to transfer: "))
                    tx = Transaction('transfer', amount, current_acc.acc_number, dest_acc_number)
                    tx_manager.add_transaction(tx)
                    tx_manager.process_next(bank)
                    print(f"Transferred {amount} to account {dest_acc_number}. New balance: {current_acc.balance}")
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == '4':
                print("Transaction history:")
                for t in current_acc.transactions:
                    print(" -", t)
            elif choice == '5':
                print(f"Goodbye, {current_acc.name}!")
                current_acc = None
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    main()
