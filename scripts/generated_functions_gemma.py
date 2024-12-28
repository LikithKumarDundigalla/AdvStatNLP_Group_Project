def factorial(n):
    result = 1
    if n == 0:
        return 1
    else:
        while n:
            result = n * factorial(n - 1)
            n = n - 1
            return result
        return factorial(n)

def palindrome(n):
    if str(n)==str(n)[::-1]:
        return True
    else:
        return False


def sort_by_key(list, key):
    if list is None:
        return None
    if len(list) == 0:
        return list
    else:
        return sorted(list, key=key)

class BankAccount:
    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance
    def deposit(self, amount):
        self.balance = amount+self.balance
        return self.balance
    def withdraw(self, amount):
        if self.balance-amount<0:
            raise Exception("Insufficient funds")
        self.balance -= amount
        return self.balance
    def get_balance(self): return self.balance