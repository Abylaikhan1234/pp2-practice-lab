"""nums = [10, 20, 30]

# This for loop:
for n in nums:
    print(n)

it = iter(nums)
print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30"""

"""my_list = [1, 2, 3]       # iterable, NOT an iterator
my_iter = iter(my_list)    # iterator

print(type(my_list))   # <class 'list'>
print(type(my_iter))   # <class 'list_iterator'>

print(next(my_iter))   # 1
print(next(my_iter))   # 2
print(next(my_iter))   # 3"""

"""class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

for num in Countdown(5):
    print(num)
# Output: 5 4 3 2 1"""

"""class EvenNumbers:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 2
        if self.current > self.limit:
            raise StopIteration
        return self.current

evens = EvenNumbers(10)
print(list(evens))  # [2, 4, 6, 8, 10]"""

'generator'
"""def my_generator():
    print("First")
    yield 1
    print("Second")
    yield 2
    print("Third")
    yield 3

gen = my_generator()
print(type(gen))    # <class 'generator'>

print(next(gen))    # prints "First", returns 1
print(next(gen))    # prints "Second", returns 2
print(next(gen))    # prints "Third", returns 3
# next(gen) would raise StopIteration"""


"""from datetime import datetime

now = datetime.now()

print(now.strftime("%Y-%m-%d"))           # 2026-02-19
print(now.strftime("%d/%m/%Y"))           # 19/02/2026
print(now.strftime("%A, %B %d, %Y"))      # Thursday, February 19, 2026
print(now.strftime("%I:%M %p"))           # 02:30 PM
print(now.strftime("%H:%M:%S"))"""          # 14:30:45