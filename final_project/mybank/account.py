import uuid
from datetime import datetime, timezone

from mybank import current_account
from mybank.transaction import Transaction
from mybank.settings import accounts, transactions
from mybank.middlewares import log_action


class BankAccount:
    def __init__(
        self,
        username: str,
        password: str,
        name: str,
        account_number: str,
        balance: int,
        created_at: datetime,
    ) -> None:
        self.id = uuid.uuid4()
        self.username = username
        self.password = password
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.is_active = True
        self.created_at = created_at

    def deposit(self, amount: int):
        global transactions
        transaction = Transaction(
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
            if str(current_account.id) == str(transaction["account_id"]):
                print(f"{i+1}. {transaction}")
                
    def logout(self):
        global current_account
        current_account = None
        
        print("Akkauntdan muvaffaqiyatli chiqildi!")
        
        return True
            
    def delete_account(self):
        global accounts
        global current_account
        
        for account in accounts["records"]:
            if str(current_account.id) == account["id"]:
                account["is_active"] = False
                current_account = None
                print("Akkaunt muvaffaqiyatli o'chirildi.")
                return True
        
        print("Bunday akkaunt topilmadi.")
        return False
    
    def to_dict(self):
        return {
            "id": str(self.id),
            "username": self.username,
            "password": self.password,
            "name": self.name,
            "account_number": self.account_number,
            "balance": self.balance,
            "is_active": self.is_active,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }

    def __str__(self):
        return f"BankAccount<name={self.name}>"
    

@log_action
def login():
    global accounts
    global current_account
    username: str = input("Username: ")
    password: str = input("Password: ")
    
    is_found, found_account = False, None
    for account in accounts["records"]:
        if (username == account["username"]
            and
            password == account["password"]
            and
            account["is_active"] == True
        ):
            is_found = True
            found_account = account
            break
    
    if not is_found:
        print("Bunday account mavjud emas.")
        return False
    
    current_account = BankAccount(
        username=found_account["username"],
        password=found_account["password"],
        name=found_account["name"],
        account_number=found_account["account_number"],
        balance=found_account["balance"],
        created_at=datetime.strptime(found_account["created_at"], "%Y-%m-%d %H:%M:%S")
    )
    
    print(f"Siz {current_account.username} sifatida tizimga kirdingiz.")
    
    return True

@log_action
def create_account() -> BankAccount:
    global accounts
    print("Siz yangi akkaunt ochmoqchisiz. Quyidagi ma'lumotlarni kiriting:")
    
    username: str = input("Username: ")
    
    for account in accounts["records"]:
        if username == account["username"]:
            print("Bunday username allaqachon bor!")
            return False
    
    password: str = input("Password: ")
    if len(password) < 8 or not password.isalnum():
        print("Parolingiz 8 ta harfdan kam bo'lmasligi va faqat alphanumeric bo'lishi shart.")
        return False
    confirm_password: str = input("Confirm Password: ")
    if password != confirm_password:
        print("Password mismatch.")
        return False

    name: str = input("F.I.Sh: ")
    account_number: str = input("Akkaunt raqamingiz: ")
    balance: int = int(input("Mavjud balansingiz: "))
    created_at: datetime = datetime.now(timezone.utc)

    new_account: BankAccount = BankAccount(
        username=username,
        password=password,
        name=name,
        account_number=account_number,
        balance=balance,
        created_at=created_at,
    )
    
    accounts["records"].append(new_account.to_dict())
    accounts["count"] += 1

    return new_account


@log_action
def view_all_accounts():
    print("Barcha akkauntlar ro'yxati:")
    for i, account in enumerate(accounts["records"]):
        print(f"{i + 1}. {account["name"]} - {account["balance"]}")

    is_end: str = input("Operatsiyani yakunlashni istaysizmi? ")
    if is_end == "\n":
        return None


@log_action
def search_account():
    searched_name = input("Qidirilayotgan account egasini kiriting: ")

    print("===== Natijalar =====")
    for i, account in enumerate(accounts["records"]):
        if account["is_active"] == True and searched_name.lower() in account["name"].lower():
            print(
                f"{i + 1}. {account["id"]} - {account["name"]} - {account["account_number"]}"
            )

    is_end: str = input("Operatsiyani yakunlashni istaysizmi? ")
    if is_end == "\n":
        return None