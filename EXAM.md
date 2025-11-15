# Python Module Final Exam

### Overview

Format: On paper. No phones, no computers, just a pen and a paper.
Time: 19:00 - 21:00
Pass Rate: 70%
Question grading: dynamic, based on the difficulty of the question

### Questions

1. Python dasturlash tili o'zi nima? U qanday ishlaydi? (2.0)
2. Pythonda mavjud built-in data tiplari: int, float, bool va None haqida tushuntiring, misol keltiring. O'zgaruvchining tipini aniqlash uchun qaysi funksiyadan foydalanamiz? (1.5)
3. Aytaylik bizda quyidagi kod berilgan. Bu yerda nima bo'layotganini tushuntiring - `x` va `y` ning adreslari bir xil bo'ladimi yoki har xil (1.5):
```python
x = 10
y = x

print(id(x), id(y))
```
4. `print()` funksiyasining `sep` va `end` parametrlari nima vazifani bajaradi? Misol keltiring. (1.0)
5. String nima? Pythonda string qanday e'lon qilinadi (bir qatorlik va ko'p qatorlik)? Sizda string mavjud bo'lsa, uni o'zgartira olasizmi? String bilan quyidagi amallarni bajarsa bo'ladimi (3.0):
    - for bilan aylanish
    - string bir qismini ajratib olish (masalan "Hello World" dan "World" ni)
    - uzunligini topish
    - bir-biriga qo'shish
6. Pythonda List va Tuple haqida tushuntiring. Ularning qanday o'xshashlik va farqlari mavjud? (2.5)
7. Pythonda Set haqida tushuntiring. Uning List va Tuple bilan qanday o'xshashlik va farqlari mavjud? (2.5)
8. Quyidagi kod muammosiz ishlaydimi? Nima uchun? (2.0)
```python
mytup = (1,2,["hi", "eshmat"], 6)
mytup[2][0] = "how are you?"
print(mytup)
```
9. Quyidagi kodlardan qaysi biri samaraliroq ishlaydi? Nima uchun? (2.0)
```python
# (1)
l = [n for n in range(0, 100, 2)]
if 78 in l:
    print(True)

# (2)
st = {n for n in range(0, 100, 2)}
if 78 in st:
    print(True)
```
10. List Comprehension nima va uning qanday ustunligi bor? U faqat List uchun ishlaydimi, tuple comprehension, set comprehension qilsa bo'lmaydimi? Misol keltiring. (2.0)
11. Dictionary nima va u nima uchun kerak? Dictionaryga yangi element qo'shish va borini o'chirish uchun nima qilamiz? Misol keltiring. (2.5)
12. For va While looplari o'rtasidagi farqni misol bilan tushuntiring. (2.0)
13. Funksiya deb nimaga aytiladi? Parametr va Argument nima? `print()` bilan `return` qanday farqi bor? Misol keltiring. (3.5)
14. Anonymous funksiyalar haqida tushuntiring. Lambda funksiyalar qachon bizga kerak bo'ladi? Misol keltiring. (2.5)
15. Funksiya boshqa funksiyani argument sifatida olishi mumkinmi? Misol keltiring. (2.5)
16. Dekorator nima? Dekoratordan qanday maqsadlarda foydalanamiz? Misol keltiring. (3.0)
17. Eshmat `myinfo.txt` nomli fayl ochib ichiga o'zi haqidagi ma'lumotlarni yozmoqchi va keyin undan qatorma-qator o'qib nechi qator yozganini bilmoqchi. Unga Pythonda kod yozib yordam bering. Context Manager ishlatmang. (4.0)
18. Context Manager o'zi nima va qanday yordam beradi? Misol keltiring. (2.0)
19. `pathlib` kutubxonasi nima uchun kerak va qanday qulayliklar beradi? Esingizda bor 3 xil methodini yozing, (masalan joriy direktoriyani olish). (3.0)
19. Pythonda Exception Handling haqida tushuntiring. `try`, `except` va `raise` qachon ishlatamiz? Misol keltiring. (2.5)
20. OOP deganda nimani tushunasiz? Class/Object va attribute/method haqida ma'lumot bering, misol keltiring. (2.5)
21. Object Method, Class Method va Static Method qanday farqlari bor? (2.0)
22. Inheritance haqida tushuntiring, u bizga nimaga kerak? Misol keltiring. Bir nechta classdan inherit qilsa bo'ladimi? (3.0)
23. Polymorphism nima va bizga qachon kerak bo'ladi? Misol keltiring. (3.0)
24. Encapsulation nima va u bizga qachon kerak bo'ladi? Misol keltiring. (3.0)
25. Pythonda Module nima? Modulda e'lon qilingan barcha o'zgaruvchi, funksiya va classlar ro'yxatini qanday olar edik? (3.0)
26. Pythonda Package nima? Papka package bo'lishi uchun qanday shartlar qanoatlanishi kerak? (3.0)
27. Aytaylik, menda quyidagi kabi fayl struktura bor (4.0):
```txt
\mypackage
    __init__.py
    mymod.py
main.py
```
U holda:
    - `mymod.py` modulini qanday import qilishim mumkin?
    - `mymod.py` moduli ichidagi `calculate` funksiyasining o'zini qanday import qila olaman?
    - `from mypackage.mymod import *` o'rniga `from mypackage import *` ishlashi uchun nima qilishim kerak?
28. JSON deb nimaga aytiladi? Pythonda `json` kutubxonasidan qanday foydalanar ekanmiz (qanday funksiyalari bor)? (4.0)