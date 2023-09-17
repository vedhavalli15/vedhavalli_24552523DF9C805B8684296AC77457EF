class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        self.__account_balance += amount

    def withdraw(self, amount):
        if amount > self.__account_balance:
            print("Insufficient balance.")
        else:
            self.__account_balance -= amount

    def display_balance(self):
        return self.__account_balance

account = BankAccount("123456789", "John Doe", 1000)
print("Initial account balance:", account.display_balance())

account.deposit(500)
print("After depositing 500:", account.display_balance())

account.withdraw(200)
print("After withdrawing 200:", account.display_balance())