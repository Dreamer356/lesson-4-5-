4.2-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import random

class NumberEncryptor:
    def __init__(self):
        self.number = None

    def encrypt(self, number):
        operation = random.choice(['add', 'subtract'])
        if operation == 'add':
            self.number = number + random.randint(1, 10)
        else:
            self.number = number - random.randint(1, 10)

    def __str__(self):
        if self.number is not None:
            return f"Зашифроване число: {self.number}"
        else:
            return "Немає зашифрованих даних."

encryptor = NumberEncryptor()
input_number = 42
encryptor.encrypt(input_number)
print(encryptor)

3.2-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Account:
    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Поповнено рахунок {self.account_id} на {amount} грн. Новий баланс: {self.balance}")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Знято {amount} грн з рахунку {self.account_id}. Новий баланс: {self.balance}")
        else:
            print("Недостатньо коштів на рахунку.")

    def get_balance(self):
        return self.balance

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def create_account(self, account_id, initial_balance=0):
        if account_id not in self.accounts:
            account = Account(account_id, initial_balance)
            self.accounts[account_id] = account
            print(f"Створено рахунок {account_id} в банку {self.name} з початковим балансом {initial_balance} грн.")
        else:
            print(f"Рахунок {account_id} вже існує в банку {self.name}.")

    def get_account(self, account_id):
        return self.accounts.get(account_id)

my_bank = Bank("My Bank")
my_bank.create_account("12345", 1000)
my_bank.create_account("54321", 500)
account1 = my_bank.get_account("12345")
account2 = my_bank.get_account("54321")

account1.deposit(200)
account2.withdraw(300)

print(f"Баланс рахунку 12345: {account1.get_balance()} грн.")
print(f"Баланс рахунку 54321: {account2.get_balance()} грн.")
