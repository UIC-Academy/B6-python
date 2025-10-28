class BankAccount:
    called_count = 0
    total_money = 0
    
    def __init__(self, name, card_number, balance):
        self.name = name
        self.card_number = card_number
        self.balance = balance
        
        BankAccount.total_money += self.balance
    
    def deposit(self, amount: int):
        self.balance = self.balance + amount
        BankAccount.total_money += amount
        
    def withdraw(self, amount: int):
        if amount > self.balance:
            raise ValueError("You don't have enough money!")

        self.balance = self.balance - amount
        BankAccount.total_money -= amount
        
    def delete_account(self):
        print("Balance is chopped")
        del self.balance

zafarbeks_card = BankAccount(
    name="Zafarbek",
    card_number="5614 3467 2134 8765",
    balance=10000000
)

javohirs_card = BankAccount(
    name="Javohir",
    card_number="4916 1231 3456 7711",
    balance=70000000
)

print("Bank balansi:", BankAccount.total_money)

zafarbeks_card.withdraw(5000000)
print(zafarbeks_card.balance)

zafarbeks_card.deposit(4000000)
print(zafarbeks_card.balance)

zafarbeks_card.withdraw(6000000)
print(zafarbeks_card.balance)

print("Bank balansi:", BankAccount.total_money)

# Statefulness - o'zida ma'lum qiymat saqlab turish
javohirs_card.withdraw(55000000)

print("Bank balansi:", BankAccount.total_money)

javohirs_card.delete_account()

# print(javohirs_card, javohirs_card.balance)

print(vars(BankAccount))