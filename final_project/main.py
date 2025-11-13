import uuid
from datetime import datetime, timezone

# =============== Definitions


class Transaction:
    def __init__(
        self,
        id: uuid.UUID,
        account_id: uuid.UUID,
        type: str,
        amount: int,
        status: str,
        datetime: datetime,
    ) -> None:
        self.id = id
        self.type = type
        self.account_id = account_id
        self.amount = amount
        self.status = status
        self.datetime = datetime
        
    def to_dict(self):
        return {
            "id": str(self.id),
            "account_id": str(self.account_id),
            "type": self.type,
            "amount": self.amount,
            "status": self.status,
            "created_at": self.datetime
        }

    def __str__(self) -> str:
        return f"Transaction<sender={self.sender_name}, amount={self.amount}>"


class BankAccount:
    def __init__(
        self,
        id: uuid.UUID,
        name: str,
        account_number: str,
        balance: int,
        created_at: datetime,
    ) -> None:
        self.id = id
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.created_at = created_at

    def deposit(self, amount: int):
        global transactions
        transaction = Transaction(
            id=uuid.uuid4(),
            account_id=current_account.id,
            type="deposit",
            amount=amount,
            status="success",
            datetime=datetime.now(timezone.utc),
        )
        
        transactions["records"].append(transaction.to_dict())
        transactions["count"] += 1
        self.balance += amount
        
        print(f"Pul muvaffaqiyatli yechildi! Hozir hisobingizda {self.balance} summa bor.")
        
        is_end: str = input("Operatsiyani yakunlashni istaysizmi? ")
        if is_end == "\n":
            return None
        return self.balance

    def withdraw(self, amount: int):
        global transactions
        transaction = Transaction(
            id=uuid.uuid4(),
            account_id=current_account.id,
            type="withdraw",
            amount=amount,
            status="pending",
            datetime=datetime.now(timezone.utc),
        )
        if amount > self.balance:
            transaction.status = "failed"
            print("Balansingizda yetarli mablag' mavjud emas.")
            return

        self.balance -= amount
        transaction.status = "success"
        transactions["records"].append(transaction.to_dict())
        transactions["count"] += 1
        print("Pul muvaffaqiyatli yechildi!")
        
        is_end: str = input("Operatsiyani yakunlashni istaysizmi? ")
        if is_end == "\n":
            return None
        return self.balance

    def view_transactions(self):
        global transactions
        for i, transaction in enumerate(transactions["records"]):
            if str(current_account.id) == str(transaction.account_id):
                print(f"{i+1}. {transaction}")
            
    def delete_account(self):
        global current_account
        current_account = None
        
        print("Akkauntingiz muvaffaqiyatli o'chirildi!")
        
        return True

    def __str__(self):
        return f"BankAccount<name={self.name}>"


# =============== Globals

accounts: list[BankAccount] = []
transactions: dict = {
    "count": 0,
    "records": []
}
menu_text: str = """=== Bank System Menu ===
1. Create New Account
2. View All Accounts
3. Search Account
4. Deposit
5. Withdraw
6. View Transactions
7. Delete Account
8. Exit
========================"""
current_account = None

# =============== Core Logic


def create_account() -> BankAccount:
    print("Siz yangi akkaunt ochmoqchisiz. Quyidagi ma'lumotlarni kiriting:")

    name: str = input("F.I.Sh: ")
    account_number: str = input("Akkaunt raqamingiz: ")
    balance: int = int(input("Mavjud balansingiz: "))

    id: uuid.UUID = uuid.uuid4()
    created_at: datetime = datetime.now(timezone.utc)

    new_account: BankAccount = BankAccount(
        id=id,
        name=name,
        account_number=account_number,
        balance=balance,
        created_at=created_at,
    )

    global accounts
    accounts.append(new_account)

    return new_account


def view_all_accounts():
    print("Barcha akkauntlar ro'yxati:")
    for i, account in enumerate(accounts):
        print(f"{i + 1}. {account.name} - {account.balance}")

    is_end: str = input("Operatsiyani yakunlashni istaysizmi? ")
    if is_end == "\n":
        return None


def search_account():
    searched_name = input("Qidirilayotgan account egasini kiriting: ")

    print("===== Natijalar =====")
    for i, account in enumerate(accounts):
        if searched_name.lower() in account.name.lower():
            print(
                f"{i + 1}. {str(account.id)} - {account.name} - {account.account_number}"
            )

    is_end: str = input("Operatsiyani yakunlashni istaysizmi? ")
    if is_end == "\n":
        return None


# =============== Main Menu Loop


def main_menu() -> None:
    while True:
        print(menu_text)
        choice: int = int(input("Enter your choice: "))

        if choice == 1:
            global current_account
            current_account = create_account()

            print("Akkaunt muvaffaqiyatli yaratildi.")
        elif choice == 2:
            view_all_accounts()
        elif choice == 3:
            search_account()
        elif choice == 4:
            while True:
                amnt = int(input("Kiritmoqchi bo'lgan summangizni kiriting: "))
                if amnt <= 0:
                    print("Manfiy sonni kirita olmaysiz!")
                    continue
                break
            current_account.deposit(amount=amnt)
        elif choice == 5:
            while True:
                amnt = int(input("Yechmoqchi bo'lgan summangizni kiriting: "))
                if amnt <= 0:
                    print("Manfiy sonni kirita olmaysiz!")
                    continue
                break
            current_account.withdraw(amount=amnt)
        elif choice == 6:
            current_account.view_transactions()
        elif choice == 7:
            is_confirmed = input("Rostdan akkauntingizni o'chirmoqchimisiz? (Ha (1)/Yoq (0)): ")
            if is_confirmed != "1":
                continue
            current_account.delete_account()
        else:
            print("Exit")
            break


if __name__ == "__main__":
    main_menu()
