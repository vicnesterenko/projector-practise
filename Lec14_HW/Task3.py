class Account:
    def __init__(self, balance, account_number):
        self._balance = balance
        self._account_number = account_number

    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("Amount must be positive")

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError("Amount must be positive")

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_number

    def __str__(self):
        return f"Account number: {self._account_number}, balance: {self._balance}"


class SavingsAccount(Account):
    def __init__(self, balance, account_number, interest):
        super().__init__(balance, account_number)
        self.interest = interest

    def add_interest_to_account(self):
        self._balance += self._balance * (self.interest / 100)
        return self._balance


class CurrentAccount(Account):
    def __init__(self, balance, account_number, limit):
        super().__init__(balance, account_number)
        self.limit = limit


class Bank:
    def __init__(self, accounts: list[Account]):
        self.accounts = accounts

    def open_account(self, account):
        self.accounts.append(account)

    def close_account(self, account):
        self.accounts.remove(account)

    def pay_dividends(self):
        for account in self.accounts:
            if isinstance(account, SavingsAccount):
                account.add_interest_to_account()
            elif isinstance(account, CurrentAccount):
                if account.get_balance() < 0:
                    print(
                        f"Letter sent for overdraft on account {account.get_account_number()}"
                    )


if __name__ == "__main__":
    account1 = SavingsAccount(1000, "1", 0)
    account2 = CurrentAccount(500, "2", -10000)
    account3 = Account.create_account("3")

    bank = Bank([account1, account2, account3])

    bank.pay_dividends()

    print(account1)
    print(account2)
    print(account3)
    bank.close_account(account3)
