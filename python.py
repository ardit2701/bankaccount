class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            interest_earned = self.balance * self.int_rate
            self.balance += interest_earned
        return self

# Example usage:
# Create a BankAccount instance with a balance of $100 and a 2% interest rate
account1 = BankAccount(int_rate=0.02, balance=100)

# Deposit $50 into the account
account1.deposit(50).display_account_info()

# Withdraw $30 from the account
account1.withdraw(30).display_account_info()

# Yield interest on the account
account1.yield_interest().display_account_info()