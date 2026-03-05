class BankAccount:
    def __init__(self, account_number , owner_name , balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
    def deposit(self , amount):
        self.balance += amount
    def withdraw(self , amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount
    def check_balance(self):
        print(f"The balance for account {self.account_number} is {self.balance}")

Acc1 = BankAccount("12345" , "Saeesh" , 1000)
Acc1.deposit(500)
Acc1.withdraw(250)
Acc1.check_balance()
