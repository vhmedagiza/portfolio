class Wallet:
    def __init__(self, name, balance= 0.0, transactions=None):
        if transactions is None:
            self.transactions = []
        self.name = name
        self.balance = balance

    def add_money(self, money):
        self.balance += money
        self.transactions.append({"type": "credit", "amount": money})
        print(f"New balance: {self.balance}")

    def spend_money(self,money):
        if self.balance >= money:
            self.balance -= money
            self.transactions.append({"type": "debit", "amount": money})
            print(f"New balance: {self.balance}")
        else:
            print("Insufficient balance.")

    def history(self):
        for i in self.transactions:
            print(i)

    def print_all(self):
        print(f"Name of Owner:{self.name}")
        print(f"New balance: {self.balance}")

class Saving_wallet(Wallet):
    def __init__(self, name, balance= 0.0):
        super().__init__(name, balance)
        self.savings = 0.0
    def save(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.savings += amount
            print(f"Balance: {self.balance} | Savings: {self.savings}")
        else:
            print("Insufficient balance to save.")


w1 = Wallet("Ahmed",5000)
w1.print_all()
w1.add_money(500)
w1.spend_money(700)
w1.history()
w1 = Saving_wallet("Ahmed", 5000)
w1.save(500)

