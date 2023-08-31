import unittest
from io import StringIO
from unittest.mock import patch

from Bank import Bank, Account, SavingsAccount, CurrentAccount


class TestBankMethods(unittest.TestCase):
    def setUp(self):
        self.account1 = SavingsAccount(1000, "1", 0)
        self.account2 = CurrentAccount(500, "2", -10000)
        self.bank = Bank([self.account1, self.account2])

    def test_open_account(self):
        initial_account_count = len(self.bank.accounts)
        new_account = Account.create_account("3")
        self.bank.open_account(new_account)

        self.assertEqual(len(self.bank.accounts), initial_account_count + 1)
        self.assertIn(new_account, self.bank.accounts)
        self.assertEqual(new_account.get_balance(), 0.0)

    def test_pay_dividends(self):
        with patch("sys.stdout", new_callable=StringIO) as captured_output:
            self.bank.pay_dividends()
            output = captured_output.getvalue()
            self.assertIn(
                f"Letter sent for overdraft on account {self.account2.get_account_number()}",
                output,
            )
            self.assertEqual(
                self.account1.get_balance(),
                1000,
            )


if __name__ == "__main__":
    unittest.main()
