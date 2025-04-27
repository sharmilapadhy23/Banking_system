# Banking_system

A modular, command-line banking system built in Python, designed to demonstrate real-world application of Data Structures and Algorithms (DSA). This project is ideal for showcasing practical coding skills, system design, and algorithmic thinking on your resume.

---

## 🚀 Features

- **Account Management**: Create, delete, and manage bank accounts.
- **Authentication**: Secure login with PIN hashing (`bcrypt`).
- **Transactions**: Deposit, withdraw, and transfer funds between accounts.
- **Transaction History**: Efficiently stored using linked lists.
- **Batch Processing**: Queue-based system for pending transactions.
- **Sorting & Searching**: Merge sort for account reports and binary search for fast lookups.
- **Security**: PINs are hashed; all inputs validated.
- **Test Coverage**: Includes unit tests for core modules.

---

## 🗂️ Project Structure

banking-system-dsa/
│
├── README.md
├── requirements.txt
├── main.py
│
├── bank/
│ ├── account.py
│ ├── bank_system.py
│ ├── transaction.py
│ ├── transaction_manager.py
│ ├── transaction_history.py
│ └── transfer_graph.py
│
├── dsa/
│ ├── sorting.py
│ ├── searching.py
│ └── linked_list.py
│
└── tests/
├── test_account.py
├── test_bank_system.py
└── test_dsa.py

text

---

## ⚙️ Installation & Usage

1. **Clone the repository:**
    ```
    git clone https://github.com/sharmilapadhy23/Banking_system.git
    cd banking-system-dsa
    ```

2. **(Optional) Create and activate a virtual environment:**
    ```
    python -m venv env
    # On Windows:
    env\Scripts\activate
    # On macOS/Linux:
    source env/bin/activate
    ```

3. **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```

4. **Run the application:**
    ```
    python main.py
    ```

5. **Run the tests:**
    ```
    python -m unittest discover tests
    ```

---

## 🧑‍💻 Example Usage

- **Create an account** with a unique account number, your name, and a PIN.
- **Log in** using your account number and PIN.
- **Deposit, withdraw, or transfer** money to other accounts.
- **View your transaction history**.
- **List all accounts sorted by balance**.

---

## 📚 Data Structures & Algorithms Used

- **Hash Table (dict)**: Fast account lookup.
- **Queue (collections.deque)**: Batch transaction processing.
- **Linked List**: Transaction history storage.
- **Merge Sort**: Sorting accounts by balance.
- **Binary Search**: Fast account search in sorted lists.
- **Graph (optional/advanced)**: Fraud detection via transfer network analysis.
- **bcrypt**: Secure PIN hashing.

---

## 🧪 Testing

The project includes unit tests for all main modules.  
Run all tests with:
python -m unittest discover tests

text

## 🌟 Why This Project?

This project demonstrates:
- Real-world application of DSA concepts in Python.
- Secure, modular software design.
- Practical problem-solving and system thinking.
- Readiness for software engineering, backend, or fintech roles.

---

## 👤 Author

Sharmila Padhy
[GitHub](https://github.com/sharmilapadhy23) | [LinkedIn](https://www.linkedin.com/in/sharmila-padhy-60a82b251/)

