"""n = int(input())
d = int(input())
def div_by (n,d):
    return (n/d)% 2 == 0
        

print(div_by(n,d))"""

"""def is_even (i):
    return i%2 ==0

a = is_even(3)
b = is_even(10)

print(a,"inside is_even")"""


"""def is_even (i):
    return i%2 ==0
for i in range (1, 10):
    if is_even(i):
        print(i,"even")
    else:
        print(i,"odd")"""




'''def sum_odd(a,b):
    for i in range (10, 20):
    return i % 2 != 0

print(sum_odd(a,b))'''
"это то что я решил"
"""a= 2 
b = 4
def sum_odd(i):
    return i%2 != 0
for k in range(a,b):
    if sum_odd(k):
        print(k)"""
"Это то что я решил"
"""a = 2
b = 7
sum = 0
def sum_odd (i):
    return i % 2 != 0
for k in range (a,b):
    if sum_odd (k):
        print(k)
        sum += k

print(sum)"""

"Это то что чат гпт написал"
"""a = 2
b = 7
sum = 0
for k in range (a, b):
    if k % 2 != 0:
        print(k)
        sum+=k

print("sum", sum)"""
'примеры с слайда'
"""a = 1
b = 5
def sum_odd(a,b):
    sum_of_odd = 0 
    for i in range (a, b):
        sum_of_odd += i
    return sum_of_odd
print(sum_odd(a,b))"""

"""def sum_odd(a, b):
    sum_of_odd = 0
    i = a
    while i <= b:
        sum_of_odd += i
        i+= 1
    return sum_of_odd
print (sum_odd(8, 13))"""

"""a = 1
b = 5
def sum_odd(a,b):
    sum_of_odd = 0 
    for i in range (a, b+1):
        sum_of_odd += i
        print(i, sum_of_odd)
    return sum_of_odd
print(sum_odd(a,b))"""

"""def sum_odd(a,b):
    sum_of_odds= 0
    for i in range(a,b+1):
        if i%2 ==1:
            sum_of_odds += i
            print(i,sum_of_odds)
    return sum_of_odds
print(sum_odd(2,7))"""
"ozim shygaryga tyryskanim"
"""def is_palindrome(s):
    reversed_s = s[::-1]
    if s == reversed_s:
        return(True)
    else:
        return(False)
    
print(is_palindrome("111"))"""

"rekomendacia pokoroce ot chatgpt na zametky"

"""def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("asdasdasd"))"""

"""def add(x,y):
    return x+y
def multi(x,y):
    return x*y
print(add(1,2))
print(multi(2,8))"""

"""def f(x):
    x = x+ 1 
    print( x)
    return x
y = 3
z = f(y)"""

"""a = int(input())
b = int(input())
def div(a,b):
    if b != 0:
        return a/b
print (div(a,b))"""  


"""def calc(op, x, y):
    return op(x,y)

def add (a,b):
    return a+b

def div(a,b):
    if b!= 0:
        return a/b
    print ("demon was 0")

res = calc(add,2,3) 
print(res)

res1 = calc(div,2,1)
print(res1)"""

"""def func_a():
    print('inside func_a')
def fun_b(y):
    print('inside func_b')
    return y+1
def fun_c (f, z):
    print('inside func_c')
    return f(z)

print(func_a())
print(5+ fun_b(2))
print(fun_c(fun_b,3))"""

"lamda"
"lambda x: x%2 == 0 только один раз может изпользоваться, вызываться"

"""apply = (lambda x: x%2 == 0)

print(apply(10))"""

"""def do_twice(n,fn):
    return fn(fn(n))

print(do_twice(3,lambda x: x**2))"""

"почему ** два астерикс возведение в степень, если только один* тогда умножение"


"CLASS"
"""class Coordinate(object):
    def _init_(self,xval,yval):
        self.x = xval
        self.y = yval

c= Coordinate (3,4)
origin = Coordinate (0,0)
print (c.x)
print(origin.x)"""

"""class Coordinate(object):
    def _init_ (self, x, y):
        self.x = x
        self.y = y
    def distance(self,other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5"""











 

    



    
