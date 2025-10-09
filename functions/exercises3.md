# Functions as First-Class Objects & Anonymous functions

## 🇬🇧 In English
### First-Class Objects

These exercises focus on treating functions as values: assigning them, passing them as arguments, and returning them from other functions.

| # | Topic | Exercise |
| :--- | :--- | :--- |
| **1** | **Assignment** | Define a function `add(a, b)` that returns the sum of two numbers. Assign this function to a new variable called `plus`. Call `plus(5, 3)` and print the result. |
| **2** | **List Storage** | Create a list called `operations` containing the built-in functions `min`, `max`, and `sum`. Iterate through the list and apply each function to a list of numbers `[10, 20, 30]` and print the results. |
| **3** | **Argument Passing (Basic)** | Write a function `apply_operation(x, y, operation)` that takes two numbers and a function as arguments. Inside, return the result of applying the `operation` function to `x` and `y`. Use it with your `add` function from Exercise 1. |
| **4** | **Argument Passing (String)** | Write a function `process_string(s, func)` that takes a string and a function. Use the function to process the string (e.g., `str.upper` or `str.lower`) and return the result. |
| **5** | **Simple Callback** | Create a function `execute_twice(func)` that calls the passed function `func` two times. Pass a simple function that prints "Hello!" to `execute_twice`. |
| **6** | **Conditional Execution** | Define a function `safe_divide(a, b)` and a function `error_handler()`. Write a function `run_if_safe(func, handler, a, b)` that calls `func(a, b)` only if $b \neq 0$; otherwise, it calls `handler()`. |
| **7** | **Function as Return Value (Simple Closure)** | Define an **outer** function `create_multiplier(n)` that takes one number $n$ and returns an **inner** function. The inner function should take one argument $x$ and return $x \times n$. |
| **8** | **Using the Returned Function** | Use the `create_multiplier(n)` function from Exercise 7 to create two new functions: `double = create_multiplier(2)` and `triple = create_multiplier(3)`. Test them by calculating `double(5)` and `triple(5)`. |
| **9** | **Function Dispatch** | Create a dictionary called `command_map` where keys are strings ('up', 'down') and values are functions (e.g., functions that print "Moving Up" or "Moving Down"). Get a command from a variable and execute the corresponding function. |
| **10** | **Filtering with a Function** | Write a function `filter_list(data_list, criterion_func)` that takes a list and a function that returns `True` or `False`. Return a new list containing only the elements for which `criterion_func` returned `True`. Use a function that checks if a number is even as the criterion. |

***

### Lambda Functions

These exercises focus on creating and using simple, single-expression `lambda` functions.

| # | Topic | Exercise |
| :--- | :--- | :--- |
| **11** | **Basic Addition** | Write a `lambda` function that takes two arguments, $a$ and $b$, and returns their sum. Assign it to a variable called `quick_add`. Call it with $(10, 7)$ and print the result. |
| **12** | **Basic Squaring** | Write a `lambda` function that takes one argument $x$ and returns $x^2$. Call it with $9$ and print the result. |
| **13** | **Ternary Operator** | Write a `lambda` function that takes one argument $x$. If $x > 10$, return "Large"; otherwise, return "Small". Test it with $15$ and $5$. |
| **14** | **String Length Check** | Write a `lambda` function that takes one string argument $s$ and returns the length of the string. Assign it to `get_length`. |
| **15** | **Using Lambda as a Utility** | Create a list of names: `["Alice", "Bob", "Charlie"]`. Use a `lambda` function and a `for` loop to print each name prefixed with "Hello, ". |
| **16** | **Filtering with Lambda** | Use the built-in `filter()` function and a `lambda` function to filter the list `[1, 5, 8, 12, 17, 20]` to include only numbers greater than $10$. Print the resulting list. |
| **17** | **Mapping with Lambda** | Use the built-in `map()` function and a `lambda` function to convert every number in the list `[1, 2, 3, 4]` to its string representation (e.g., `"1"`, `"2"`). Print the resulting list. |
| **18** | **Reducing with Lambda (Intro)** | Import the `reduce` function from `functools`. Use `reduce()` and a `lambda` function to multiply all numbers in the list `[2, 3, 4]` together. |
| **19** | **Multiple Arguments** | Write a `lambda` function that takes three arguments $x, y, z$ and returns $(x + y) / z$. Call it with $(10, 2, 4)$. |
| **20** | **Identity Function** | Write a `lambda` function that simply returns its single argument. Use it to demonstrate that it can be used in place of a named function. |

***

### Advanced Applications

These exercises combine the two concepts, often using `lambda` functions in situations where functions are first-class objects (like sorting).

| # | Topic | Exercise |
| :--- | :--- | :--- |
| **21** | **Sorting a List of Tuples (Key)** | Sort the list of tuples `data = [('apple', 5), ('banana', 2), ('cherry', 8)]` based on the numerical value (the second element) using the `key` argument in the `sort()` method with a **`lambda` function**. |
| **22** | **Sorting a List of Dictionaries** | Sort the list of dictionaries `users = [{'name': 'Jane', 'age': 30}, {'name': 'John', 'age': 25}]` based on the value of the 'age' key, again using a **`lambda` function** as the `key`. |
| **23** | **Chaining Operations (Map & Filter)** | Use `filter()` with a `lambda` to keep only odd numbers from `[1, 2, 3, 4, 5, 6]`. Then use `map()` with a separate `lambda` to cube $(\text{power of } 3)$ the remaining numbers. |
| **24** | **Custom Sorting (Multiple Keys)** | Sort a list of strings `names = ['Zoe', 'Adam', 'Alex', 'Ben']` first by **length** (shortest first), and then **alphabetically** (A-Z) using the `key` argument in the `sorted()` function with a **tuple-returning `lambda`**. |
| **25** | **Function as Return (Lambda Closure)** | Rewrite Exercise 7 using a **`lambda` function** to define the inner function: Define `create_power(n)` that returns a `lambda` which raises its input $x$ to the power of $n$. |
| **26** | **Applying a List of Functions** | Create a list of `lambda` functions: one for adding $5$, one for subtracting $2$, and one for multiplying by $10$. Iterate through a number, say $10$, and apply all the functions sequentially, printing the result of each step. |
| **27** | **Passing a Lambda to a Named Function** | Use the `apply_operation` function from Exercise 3. Pass a **`lambda` function** to it that calculates the remainder (modulo) of two numbers. |
| **28** | **List Comprehension with Lambda Logic** | Use a **list comprehension** to create a new list from `[1, 2, 3, 4, 5]`. For each number, use a **`lambda` expression** (defined separately and called within the comprehension) to return the number only if it's even. |
| **29** | **Nested Lambda (Tricky)** | Define a **`lambda` function** that takes $a$ and returns *another* **`lambda` function** that takes $b$ and returns $a + b$. Call the outer lambda with $10$ to get a new function, and then call the new function with $5$. |
| **30** | **Function Documentation** | Define a function `log_call(func)` that takes another function as an argument. Inside `log_call`, return a new function that *first* prints a message like "Calling [function name]" and *then* executes the original `func`. Apply this to a simple printing function. |


---

## 🇺🇿 Uzbek

### 🐍 Funksiyalar birinchi darajali obyekt sifatida

Bu mashqlar funksiyalarga qiymatlar kabi munosabatda bo‘lishga qaratilgan: ularni o‘zgaruvchiga yuklash, argument sifatida uzatish va boshqa funksiyalardan qaytarish.

| \# | Mavzu | Mashq |
| :--- | :--- | :--- |
| **1** | **O‘zgaruvchiga yuklash** | Ikki son yig‘indisini qaytaradigan `add(a, b)` funksiyasini aniqlang. Bu funksiyani `plus` deb nomlangan yangi o‘zgaruvchiga yuklang. `plus(5, 3)` ni chaqiring va natijani chop eting. |
| **2** | **Ro‘yxatda saqlash** | `min`, `max` va `sum` (o‘rnatilgan) funksiyalaridan tashkil topgan `operations` nomli ro‘yxat yarating. Ro‘yxat bo‘ylab harakatlaning va har bir funksiyani `[10, 20, 30]` sonlar ro‘yxatiga qo‘llang hamda natijalarni chop eting. |
| **3** | **Argument sifatida uzatish (Asosiy)** | `apply_operation(x, y, operation)` funksiyasini yozing. U ikki son va bitta funksiyani argument sifatida qabul qilsin. Ichkarida, `operation` funksiyasini $x$ va $y$ ga qo‘llash natijasini qaytaring. Uni 1-mashqdagi **`add`** funksiyangiz bilan sinab ko‘ring. |
| **4** | **Argument sifatida uzatish (Matn)** | Bitta matn va bitta funksiyani qabul qiladigan `process_string(s, func)` funksiyasini yozing. Matnni qayta ishlash uchun (masalan, `str.upper` yoki `str.lower`) uzatilgan funksiyadan foydalaning va natijani qaytaring. |
| **5** | **Oddiy chaqiriq (Callback)** | Uzatilgan `func` funksiyasini **ikki marta** chaqiradigan `execute_twice(func)` funksiyasini yarating. Unga "Salom!" degan yozuvni chop etadigan oddiy funksiyani uzating. |
| **6** | **Shartli bajarish** | `safe_divide(a, b)` funksiyasini va `error_handler()` funksiyasini aniqlang. Agar $b \neq 0$ bo'lsa, `func(a, b)` ni chaqiradigan, aks holda `handler()` ni chaqiradigan `run_if_safe(func, handler, a, b)` funksiyasini yozing. |
| **7** | **Funksiyani qaytarish (Oddiy Closure)** | Bitta $n$ sonini qabul qiladigan va **ichki** funksiyani qaytaradigan **tashqi** funksiya `create_multiplier(n)` ni aniqlang. Ichki funksiya bitta $x$ argumentini qabul qilib, $x \times n$ ni qaytarsin. |
| **8** | **Qaytarilgan funksiyadan foydalanish** | 7-mashqdagi `create_multiplier(n)` funksiyasidan foydalanib, ikkita yangi funksiya yarating: `double = create_multiplier(2)` va `triple = create_multiplier(3)`. Ularni `double(5)` va `triple(5)` ni hisoblash orqali sinab ko‘ring. |
| **9** | **Funksiyani ajratish (Dispatch)** | Kalitlari matnlar ('up', 'down') va qiymatlari funksiyalar ("Yuqoriga harakatlanish" yoki "Pastga harakatlanish" ni chop etadigan funksiyalar) bo‘lgan `command_map` nomli lug‘at yarating. O‘zgaruvchidan buyruq oling va unga mos keladigan funksiyani bajaring. |
| **10** | **Funksiya bilan filterlash** | Bitta ro‘yxat va `True` yoki `False` qaytaradigan funksiyani qabul qiladigan `filter_list(data_list, criterion_func)` funksiyasini yozing. `criterion_func` `True` qiymatini qaytargan elementlardan iborat yangi ro‘yxatni qaytaring. Filtr (criterion) sifatida sonning **juft** ekanligini tekshiruvchi funksiyadan foydalaning. |

***

### Lambda funksiyalari

Bu mashqlar oddiy, bir ifodali `lambda` funksiyalarini yaratish va ulardan foydalanishga qaratilgan.

| \# | Mavzu | Mashq |
| :--- | :--- | :--- |
| **11** | **Oddiy qo‘shish** | Ikki $a$ va $b$ argumentini qabul qiladigan va ularning yig‘indisini qaytaradigan **`lambda` funksiyasini** yozing. Uni `quick_add` o‘zgaruvchisiga yuklang. Uni $(10, 7)$ bilan chaqiring va natijani chop eting. |
| **12** | **Oddiy kvadratlash** | Bitta $x$ argumentini qabul qiladigan va $x^2$ ni qaytaradigan **`lambda` funksiyasini** yozing. Uni $9$ bilan chaqiring va natijani chop eting. |
| **13** | **Ternary operator** | Bitta $x$ argumentini qabul qiladigan **`lambda` funksiyasini** yozing. Agar $x > 10$ bo'lsa, "Large" (Katta) ni, aks holda "Small" (Kichik) ni qaytarsin. Uni $15$ va $5$ bilan sinab ko‘ring. |
| **14** | **Matn uzunligini tekshirish** | Bitta $s$ matn argumentini qabul qiladigan va matn uzunligini qaytaradigan **`lambda` funksiyasini** yozing. Uni `get_length` ga yuklang. |
| **15** | **`lambda` ni yordamchi vosita sifatida ishlatish** | Ismlar ro‘yxatini yarating: `["Ali", "Botir", "Charos"]`. Har bir ism oldiga "Salom, " so‘zini qo‘shib chop etish uchun **`lambda` funksiyasi** va `for` tsikliga ega ekanligingizni tasdiqlang. |
| **16** | **`lambda` bilan filterlash** | O‘rnatilgan **`filter()`** funksiyasidan va **`lambda` funksiyasidan** foydalanib, `[1, 5, 8, 12, 17, 20]` ro‘yxatidan faqat $10$ dan katta sonlarni tanlang. Natijaviy ro‘yxatni chop eting. |
| **17** | **`lambda` bilan maplash** | O‘rnatilgan **`map()`** funksiyasidan va **`lambda` funksiyasidan** foydalanib, `[1, 2, 3, 4]` ro‘yxatidagi har bir sonni uning matn ko‘rinishiga (`"1"`, `"2"`, va hokazo) aylantiring. Natijaviy ro‘yxatni chop eting. |
| **18** | **`lambda` bilan reducelash (Kirish)** | `functools` modulidan **`reduce`** funksiyasini import qiling. `reduce()` va **`lambda` funksiyasidan** foydalanib, `[2, 3, 4]` ro‘yxatidagi barcha sonlarni o‘zaro ko‘paytiring. |
| **19** | **Bir nechta argument** | Uch $x, y, z$ argumentini qabul qiladigan va $(x + y) / z$ ni qaytaradigan **`lambda` funksiyasini** yozing. Uni $(10, 2, 4)$ bilan chaqiring. |
| **20** | **Identifikator funksiya** | Yagona argumentini qaytaradigan **`lambda` funksiyasini** yozing. Undan oddiy nomli funksiya o‘rnida foydalanish mumkinligini ko‘rsating. |

***

### Umumlashtirilgan Qo'llanmalar

Bu mashqlar ikkita tushunchani birlashtiradi, ko‘pincha funksiyalar birinchi darajali obyekt bo‘lgan joylarda (`sort` kabi) `lambda` funksiyalaridan foydalanadi.

| \# | Mavzu | Mashq |
| :--- | :--- | :--- |
| **21** | **Tuple ro‘yxatini saralash (Kalit)** | `data = [('apple', 5), ('banana', 2), ('cherry', 8)]` tuple ro‘yxatini ikkinchi element (son qiymati) asosida, **`lambda` funksiyasini** `sort()` metodining **`key`** argumentida ishlatib, saralang. |
| **22** | **Lug‘atlar ro‘yxatini saralash** | `users = [{'name': 'Jane', 'age': 30}, {'name': 'John', 'age': 25}]` lug‘atlar ro‘yxatini 'age' (yosh) kalitining qiymati asosida, yana **`lambda` funksiyasini** **`key`** sifatida ishlatib, saralang. |
| **23** | **Amallarni zanjirlash (`map` & `filter`)** | `filter()` va **`lambda`** yordamida `[1, 2, 3, 4, 5, 6]` dan faqat toq sonlarni qoldiring. Keyin `map()` va boshqa **`lambda`** yordamida qolgan sonlarni uchinchi darajaga (kubi) ko‘taring. |
| **24** | **Maxsus saralash (Bir nechta kalit)** | `names = ['Zoe', 'Adam', 'Alex', 'Ben']` matnlar ro‘yxatini avval **uzunligi** bo‘yicha (eng qisqasi birinchi), keyin esa **alifbo bo‘yicha** (A-Z) saralash uchun **`sorted()`** funksiyasining `key` argumentida **tuple qaytaradigan `lambda` funksiyasini** ishlating. |
| **25** | **Funksiyani qaytarish (`lambda` Closure)** | 7-mashqni ichki funksiyani aniqlash uchun **`lambda` funksiyasidan** foydalanib, qayta yozing: Kirish $x$ ni $n$ darajasiga oshiradigan **`lambda`** ni qaytaradigan `create_power(n)` ni aniqlang. |
| **26** | **Funksiyalar ro‘yxatini qo‘llash** | **`lambda` funksiyalaridan** iborat ro‘yxat yarating: biri $5$ ni qo‘shish, biri $2$ ni ayirish va biri $10$ ga ko‘paytirish uchun. $10$ soni bo‘ylab harakatlaning va barcha funksiyalarni ketma-ket qo‘llang, har bir bosqich natijasini chop eting. |
| **27** | **`lambda` ni nomli funksiyaga uzatish** | 3-mashqdagi **`apply_operation`** funksiyasidan foydalaning. Unga ikki sonning qoldig‘ini (modulosini) hisoblaydigan **`lambda` funksiyasini** uzating. |
| **28** | **`lambda` mantig‘iga ega ro‘yxat tushunish** | **Ro‘yxat tushunish** usulidan foydalanib, `[1, 2, 3, 4, 5]` dan yangi ro‘yxat yarating. Har bir son uchun, agar u juft bo‘lsa, sonning o‘zini qaytaradigan **`lambda` ifodasini** (alohida aniqlangan va ro‘yxat tushunish ichida chaqirilgan) ishlating. |
| **29** | **Ichki `lambda` (Murakkabroq)** | $a$ ni qabul qiladigan va $b$ ni qabul qilib, $a + b$ ni qaytaradigan **boshqa bir `lambda` funksiyasini** qaytaradigan **`lambda` funksiyasini** aniqlang. Tashqi `lambda` ni $10$ bilan chaqirib yangi funksiya oling, so‘ngra yangi funksiyani $5$ bilan chaqiring. |
| **30** | **Funksiyani hujjatlashtirish (Decorators ga tayyorgarlik)** | Boshqa funksiyani argument sifatida qabul qiladigan `log_call(func)` funksiyasini aniqlang. `log_call` ichida, avval "[funksiya nomi] chaqirilmoqda" kabi xabarni chop etadigan va keyin asl `func` ni bajaradigan yangi funksiyani qaytaring. Buni oddiy chop etuvchi funksiyaga qo‘llang. |