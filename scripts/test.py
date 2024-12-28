import unittest
import time
from generated_functions_gemma import factorial as factorial_gemma, palindrome as palindrome_gemma, sort_by_key as sort_by_key_gemma, BankAccount as BankAccount_gemma
from generated_functions_Qwencoder import factorial as factorial_qwencoder, palindrome as palindrome_qwencoder, sort_by_key as sort_by_key_qwencoder, BankAccount as BankAccount_qwencoder
from generated_functions_starcoder import factorial as factorial_starcoder, palindrome as palindrome_starcoder, sort_by_key as sort_by_key_starcoder, BankAccount as BankAccount_starcoder


class TestFunctions(unittest.TestCase):

    def test_factorial(self):
        test_cases = {
            0: 1,
            1: 1,
            5: 120,
            10: 3628800
        }
        for n, expected in test_cases.items():
            self.assertEqual(factorial_gemma(n), expected, f"Gemma factorial failed for {n}")
            self.assertEqual(factorial_qwencoder(n), expected, f"Qwencoder factorial failed for {n}")
            self.assertEqual(factorial_starcoder(n), expected, f"Starcoder factorial failed for {n}")

    def test_palindrome(self):
        test_cases = {
            "radar": True,
            "hello": False,
            "level": True,
            "world": False
        }
        for word, expected in test_cases.items():
            self.assertEqual(palindrome_gemma(word), expected, f"Gemma palindrome failed for '{word}'")
            self.assertEqual(palindrome_qwencoder(word), expected, f"Qwencoder palindrome failed for '{word}'")
            self.assertEqual(palindrome_starcoder(word), expected, f"Starcoder palindrome failed for '{word}'")

    def test_sort_by_key(self):
        test_cases = [
            ([{"key": 3}, {"key": 1}, {"key": 2}], "key", [{"key": 1}, {"key": 2}, {"key": 3}]),
            ([{"rank": 5}, {"rank": 3}, {"rank": 10}], "rank", [{"rank": 3}, {"rank": 5}, {"rank": 10}])
        ]
        for lst, key, expected in test_cases:
            self.assertEqual(sort_by_key_gemma(lst, key), expected, f"Gemma sort_by_key failed for {lst}")
            self.assertEqual(sort_by_key_qwencoder(lst, key), expected, f"Qwencoder sort_by_key failed for {lst}")
            self.assertEqual(sort_by_key_starcoder(lst, key), expected, f"Starcoder sort_by_key failed for {lst}")

    def test_bank_account(self):
        for AccountClass in [BankAccount_gemma, BankAccount_qwencoder, BankAccount_starcoder]:
            account = AccountClass("TestUser", 500)
            try:
                self.assertEqual(account.deposit(200), 700, f"{AccountClass.__name__} deposit failed")
            except AssertionError as e:
                print(f"Deposit Test Failed for {AccountClass.__name__}: {e}")
            try:
                self.assertEqual(account.withdraw(300), 400, f"{AccountClass.__name__} withdraw failed")
            except AssertionError as e:
                print(f"Withdraw Test Failed for {AccountClass.__name__}: {e}")
            try:
                self.assertEqual(account.get_balance(), 400, f"{AccountClass.__name__} get_balance failed")
            except AssertionError as e:
                print(f"Get Balance Test Failed for {AccountClass.__name__}: {e}")
            try:
                with self.assertRaises(Exception, msg=f"{AccountClass.__name__} insufficient funds test failed"):
                    account.withdraw(500)
            except AssertionError as e:
                print(f"Insufficient Funds Test Failed for {AccountClass.__name__}: {e}")

    def test_performance(self):
        test_cases = [5, 10, 15]
        results = {}
        for n in test_cases:
            for name, func in [("Gemma", factorial_gemma), ("Qwencoder", factorial_qwencoder), ("Starcoder", factorial_starcoder)]:
                start = time.time()
                func(n)
                elapsed = time.time() - start
                results[name] = elapsed
        print(f"Performance results: {results}")


if __name__ == "__main__":
    unittest.main()
