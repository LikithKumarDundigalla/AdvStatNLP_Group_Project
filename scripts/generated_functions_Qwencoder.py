def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


def palindrome(s: str) -> bool:
    return s == s[::-1]

def sort_by_key(dicts, key):
    return sorted(dicts, key=lambda x: x.get(key))


class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            raise Exception("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                raise Exception("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        print(f"Current balance: {self.balance}")
        return self.balance

