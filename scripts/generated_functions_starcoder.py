def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)



def palindrome(word):
    return word[0:len(word)//2] == word[len(word)//2+1:]

def sort_by_key(list1,key):
    for i,num in enumerate(list1):
          list1[i]['rank'] = num[key]
    return sorted(list1, key = lambda k: k['rank'])

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            raise Exception('Insufficient funds')

    def get_balance(self):
        return self.balance

