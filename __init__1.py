class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


account1 = BankAccount("Aman", 10000)
account2 = BankAccount("Rahul", 5000)

print(account1.name)
print(account1.balance)

print(account2.name)
print(account2.balance)