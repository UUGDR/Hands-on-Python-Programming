# Bank Account System
# Fill in every ________ to complete the program.

________ Account:
    bank_name = 'Python National Bank'   # class attribute: shared by every account
    total_accounts = 0

    def ________(self, owner, balance=0):
        ________.owner = owner
        self._balance = balance          # leading _ means "for internal use"
        ________.total_accounts += 1

    @________
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount ________ 0:
            ________ ValueError('Deposit must be positive')
        self._balance ________ amount

    def withdraw(self, amount):
        if amount ________ self._balance:
            raise ValueError('Insufficient funds')
        self._balance ________ amount

    def month_end(self):
        pass                             # a basic account has no month-end work

    def ________(self):
        return f'{type(self).__name__:<16} {self.owner:<5} ${self._balance:>9,.2f}'


class SavingsAccount(________):          # inherits everything from Account
    def __init__(self, owner, balance=0, rate=0.02):
        ________().__init__(owner, balance)
        self.rate = rate

    def month_end(self):                 # overrides Account.month_end
        self._balance += self._balance * self.rate / ________


class CheckingAccount(Account):
    def __init__(self, owner, balance=0, overdraft=100):
        super().__init__(owner, balance)
        self.overdraft = overdraft

    def ________(self, amount):          # overrides Account.withdraw
        if amount > self._balance ________ self.overdraft:
            raise ValueError('Overdraft limit exceeded')
        self._balance -= amount

    def month_end(self):
        self._balance -= 5               # monthly fee


class Bank:
    def __init__(self):
        self.accounts = ________

    def open_account(self, account):
        self.accounts.________(account)

    def run_month_end(self):
        for account in ________.accounts:
            account.________()           # each class does its own month-end work

    def total_balance(self):
        return ________(account.balance for account in self.accounts)


# --- Main program ---
bank = ________()
bank.open_account(Account('Ana', 500))
bank.open_account(SavingsAccount('Ben', 1200, rate=0.06))
bank.open_account(CheckingAccount('Cara', 300))

bank.accounts[0].deposit(250)            # Ana: 500 + 250
bank.accounts[2].withdraw(350)           # Cara overdraws, which checking allows
try:
    bank.accounts[0].withdraw(900)       # Ana only has 750
except ________ as error:
    print('Error:', error)

bank.run_month_end()
print(f'--- {Account.bank_name} ---')
for account in bank.accounts:
    print(account)
print(f'Accounts opened: {Account.________}')
print(f'Total balance  : ${bank.total_balance():,.2f}')
