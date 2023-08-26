# in progress
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
        super.__init__(balance, account_number)
        self.interest = interest

    def add_interest_to_account(self):
        pass


class CurrentAccount(Account):
    def __init__(self, balance, account_number, limit):
        super.__init__(balance, account_number)
        self.limit = limit


# class Bank()
