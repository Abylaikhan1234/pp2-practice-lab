"""# читаем количество чисел
n = int(input())

# читаем числа
numbers = list(map(int, input().split()))

# превращаем числа в булевы значения (0 → False, остальные → True)
bool_numbers = map(bool, numbers)

# суммируем True значения (True = 1, False = 0)
count = sum(bool_numbers)

# выводим результат
print(count)"""
"""import json

book = {
    'title': '1974',
    'author': ' George Orwell',
    'isbn': ' 978-04556112132',
    'uuid': ' a0dfdfd000',
}

json_string = json.dumps(book)
print(type(json_string))
print(json_string)"""

"""import json

json_string = '{"title": "1974", "author": " George Orwell", "isbn": " 978-04556112132", "uuid": " a0dfdfd000"}'

book = json.loads(json_string)

print(type(book))
print(book)"""

"""import json

book = {
    'title': '1974',
    'author': ' George Orwell',
    'isbn': ' 978-04556112132',
    'uuid': ' a0dfdfd000',
    'count': 30,
    'genre':'antiutopia',
}

json_string = json.dumps(book)

print(json_string)"""

"надо еще пройти как доставать именно один список из jsona"

"тема import"
"чтобы в локальный пишущий код импортировать новые значение функции"
"""my_int = 1
import json
print(globals().keys())"""

"""import random 
my_list = [ 1, 2 , 3]
print (random.choice(my_list))"""

"функция dir выполняет роль что в рандпме есть, что за модули"
"""import random 
print(dir(random))"""



"date time"
"""import datetime

utc_time = datetime.datetime.now()
print(utc_time)"""

"""import datetime

utc_time = datetime.datetime.now()
print(utc_time.year)
print(utc_time.month)
print(utc_time.day)
print(utc_time.hour)
print(utc_time.minute)"""

"""import datetime
some_datetime = datetime.datetime(year = 2021, month = 4, day = 25, hour = 5, minute= 5)

print(some_datetime)"""
"здесь datetime, псам дейттайм он модуль а вот после точки дейт дейттайм это класс"

"""import datetime
current_date = datetime.date.today()

print(current_date)"""

"""import datetime

current_datetime = datetime.datetime.now()
current_date = current_datetime.date()

print(current_date)"""

"вот здесь таймделта - играет роль 1го дня оперейтор - или + делает всю остальную работу "

"""import datetime

current_datetime = datetime.datetime.now()
day_ago = current_datetime - datetime.timedelta(days=1)
print(day_ago)"""

"здесь можно дейттайм сделать читабельным благодаря функции strftime "
""

"""import datetime

current_datetime = datetime.datetime.now()

print(current_datetime.strftime("%A, %d %B %Y"))"""

"list_comrehensiions"

"""squares = []
for x in range(10):
    squares.append(x**2)

print(squares)"""

"""squares = [x ** 2 for x in range(10)]
print(squares)"""

"""even_squares = []
for x in range(10):
    if x % 2 == 0:
        even_squares.append(x** 2)

print(even_squares)"""

"""even_squares=[x ** 2 for x in range(10) if x % 2 == 0]
print(even_squares)"""

"Iteration"

"""nums = [10, 20, 30]

# This for loop:
for n in nums:
    print(n)

# Is equivalent to:
it = iter(nums)
print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30
# next(it) would raise StopIteration """

"""import json

book = {
    'janr':'uzhas',
    'god':'1899',
    'lebed':'chernii',
}
lab = json.dumps(book)
print(lab)"""

"""import json
book ='{"janr": "uzhas", "god": "1899", "lebed": "chernii"}'
data = json.loads(book)
print(data["janr"])"""