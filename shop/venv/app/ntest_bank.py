import unittest
from bank import BankAccount

class AccountBalanceTestCases(unittest.TestCase):
    def setUp(self):
        self.account_yangu = BankAccount()

    def test_balance(self):
        self.assertEqual(self.account_yangu.balance, 3000, msg= 'Account balance Invalid')

    def test_deposit(self):
        self.account_yangu.deposit(4000)
        self.assertEqual(self.account_yangu.balance, 7000, msg='deposit has jam')

    def test_withdraw(self):
        self.account_yangu.withdraw(500)
        self.assertEqual(self.account_yangu.balance, 2500, msg='withdraw has jam')

    def test_invalid_trans(self):
        self.assertEqual(self.account_yangu.withdraw(6000), "invalid transaction", msg ='invalid transaction')
