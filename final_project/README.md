# Final Project - Bank Account Management System

Mazkur project Python moduli uchun yakuniy CLI dastur bo'lib, ushbu modulda o'tilgan barcha mavzularni qamrab oladi. Projectning maqsadi Bank operatsiyalari bajarilishini simulyatsiya qilish va shu o'rinda OOP, funksiyalar, fayllar bilan ishlash va boshqa ko'plab Python featurelarini amalda qo'llashdan iborat.

---

### Overview

Main Menu quyidagi ko'rinishda bo'ladi:

```
=== Bank System Menu ===
1. Create New Account
2. View All Accounts
3. Search Account
4. Deposit
5. Withdraw
6. View Transactions
7. Delete Account
8. Exit
========================
Enter your choice: 
```

Dasturni 3 bosqichli tuzib boramiz. Quyida har bir bosqichda aynan qanday tasklar bajarilishi bilan tanishasiz.

#### Version 1: Core Logic (non-persistent storage)

Dastlabki bosqichda biz barcha fundamental birliklar va strukturalarni qurib olamiz. Ma'lumotlar persistent emas, ya'ni dasturni to'xtatib boshidan ishga tushirganda ma'lumotlar yo'qoladi. 

Tuzishimiz kerak bo'lgan konstruksiyalar:
- `BankAccount` classi. 
    - Atributlari: id: uuid, name: str, account_number: str (5440 8100 1234 4321 kabi), balance: int, transactions: list[Transaction]
    - Metodlari: deposit(amount: int), withdraw(amount: int), display_info(), record_transaction(type: str, amount: int)
- `Transaction` classi.
    - Atributlari: id: uuid, type: str, sender_name: str, receiver_name: str, amount: int, status: str, datetime: datetime
    - Metodlari: `__str__()`


Barcha accountlar `accounts` deb nomlangan listda saqlanadi. Bunda, list ichida `BankAccount` klassidan olingan “mahsulot”lar, yoxud obyektlar saqlanadi. Masalan:

```python
class BankAccount:
	# O'ziz yozasiz
	pass

account1 = BankAccount()
accounts.append(account1)
```

Tranzaksiyalar esa har bir `BankAccount` classining `transactions` listida saqlanadi.

Quyida bizga kerak bo'lgan funksiyalar bilan tanishamiz:

**1. Create New Account**
- Foydalanuvchidan ism, akkaunt raqami va dastlabki summani so'rang.
- id fieldi uchun `uuid()` kutubxonasidan foydalanib unique ID yarating.
- yaratilgan `BankAccount` obyektini `accounts` listiga qo'shing.

**2. View All Accounts**
Tizimda mavjud barcha akkauntlarni list qilib chiqaradi. Bunda BankAccount objectining `display_info()` yoki `__str__()` methodidan foydalaning.

**3. Search Account**
List ichidan kiritilgani bo’yicha account qidirish. Bunda user account nomi bo’yicha qidirishi mumkin.

**4. Deposit**
Accountga pul kirimi. `balance` atributini to’g’ridan-to’g’ri emas, maxsus method bilan (masalan `deposit()`) o’zgartirasiz. Amalga oshirilgan transaksiyalar transactions listiga saqlab boriladi. Har bir transaksiya alohida dictionary sifatida saqlanishi kerak, bunda uning tuzilishi:

```python
transaction = {
	"datetime": "2025-13-04 13:00:00.000Z", # or datetime object
	"account_holder": "account_holder_name",
	"account_number": "account_number",
	"amount": 500,
	# other related data if any
}
```

**5. Withdraw**
Accountdan pul chiqimi. Bunda ham balance attributini shu method yordamida kamaytirasiz (belgilangan miqdorda). Amalga oshirilgan transaksiya transactions listiga dictionary ko’rinishida saqlanadi.

**6. View Transactions**
Mazkur akkauntda amalga oshirilgan transaksiyalar listini ko’rish. Bunda transactions listi (atribut) bo’ylab iterate qilinadi va har bir transaction dictionarysi ichidagi ma’lumot ekranga chiqariladi.

**7. Delete Account**
Accountni o’chirish imkoniyati. Agar user akkauntini o’chirishga qaror qilsa, shu user account raqami bilan bir xil fayl ochiladi va barcha tranzaksiyalari faylga saqlab qo’yiladi.

**8. Exit**
Chiqish.

---

#### Version 2: Adding Persistent Storage (File and JSON)

Oddiy list va dictionary bilan ishlaydigan holatga kelgach, endi ma'lumotlarni doimiy xotiraga saqlash masalasini ko'rishimiz kerak. Bunda biz JSON faylga saqlashimiz maqsadga muvofiqdir.

- `data` nomli papka oching va unda `accounts.json` faylini yarating. 
- dastur ishga tushganda mavjud akkauntlarni `accounts.json` faylidan o'qiydigan va agar fayl bo'sh bo'lsa bo'sh listligicha qoladigan logika yozing. Potensial errorlarni ham handle qiling.
- Dastur yakunlanganda barcha akkauntlar `accounts.json` fayliga yozilsin.
- `data` papkasi ichida `transactions.json` faylini yarating.
- dastur ishga tushganda mavjud tranzaksiyalarni `transactions.json` faylidan o'qiydigan va agar fayl bo'sh bo'lsa bo'sh listligicha qoladigan logika yozing. Potensial errorlarni ham handle qiling.
- dastur yakunlanganda barcha tranzaksiyalar `transactions.json` fayliga yozilsin.

#### Version 3: Authentication, Middleware and Modularization

3-bosqichda esa dasturni real hayotga yaqinroq bo'lishi uchun package-module ko'rinishiga olib kelamiz. Shuningdek Logging uchun middleware (decorator) yozamiz.

- Dasturni modular ko'rinishga olib keling. Bunda:
	- `main.py` faqatgina dasturni yurgizish uchun
	- `bankacc/cli.py` - CLI qismi uchun
	- `bankacc/bank_account.py` - Bank Account va unga bog'liq funksiyalar
	- `bankacc/transaction.py` - Transaction va unga bog'liq funksiyalar
	- `bankacc/utils.py` - Qo'shimcha utilita funksiyalar
- Foydalanuvchi har bir operatsiyani amalga oshirganda uni terminalga log qilib yozuvchi `log_action()` nomli dekorator yozing. 
- Akkaunt uchun register/login/logout xususiyatini qo'shing.

#### Version 4: Fix Auth Flow in Modular Structure, Give Admin Access

3-versiyadan keyin bizda muammo paydo bo'ldi - endi bizda 1 ta katta package va 5-6 ta module bor. Bitta global `current_user` o'zgaruvchisi login qilgan mavjud userni ushlab tura olmay qoldi, sababi biz `accounts.py` faylida `login()` qilganimizda o'zgaruvchiga qiymat bersak-da bu qiymat faqat o'sha `accounts.py` moduli uchun o'zgaryapti, lekin `settings.py` (original lokatsiyasi) da haliyam None qolib ketmoqda.
4-versiyada muammoga approachni o'zgartiramiz. 

❗️ Ayni paytda `BankAccount` klassi ham ma'lumotni ham uning ustidagi amallar (`deposit`, e.g.) ni o'zida ushlab turibdi. Bu esa `current_account` da albatta Account objecti turishiga majburlaydi. Lekin bu o'z navbatida yuqoridagi namespace muammosiga olib keladi.
✅ Shu sabab, barcha logika metodlarni mustaqil funksiyalarga olib o'tamiz va `BankAccount` klassi faqatgina ma'lumot ushlovchi **data model** sifatida qoldiramiz (aslida ham backendda shunday bo'ladi).

❗️❗️ Ayni paytda bizda global `accounts` va `transactions` o'zgaruvchilari mavjud va ular live obyektlarni ushlab turibdi. Har dastur o'chganida ularni qayta JSON faylga yozyapmiz, lekin bu yaxshi fikr emas. Sababi bizda endi 2 ta ma'lumot manbayi bor - JSON va global live objectlar. Qaysi biri haqiqat? Muammo. Dastur exitni bosib emas Ctrl+C bilan yakunlansachi?
✅ Har operatsiyada biz JSON faylga to'g'ridan-to'g'ri yozishimiz kerak. Ya'ni, deposit bo'ldimi, birdan yangi tranzaksiya aynan JSON faylga qo'shilishi talab etiladi.

Qo'shimcha funksionalliklar:
- Maxsus admin akkaunt qo'shing va Admin akkaunt barcha akkaunt egalari ro'yxatini hamda barcha tranzaksiyalar ro'yxatini ko'ra olishini ta'minlang.
- Main Menu tugmalarini user login qilgan qilmagani va admin yoki admin emasligiga qarab ko'rinadigan qiling.