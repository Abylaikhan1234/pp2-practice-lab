"""# enumerate(): index + value
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

# zip(): pair elements from two lists
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")"""

"""value = "123"

# Type checking
print(type(value))
print(isinstance(value, str))

# Conversions
num = int(value)
print("Converted to int:", num)

float_num = float(value)
print("Converted to float:", float_num)

# List to string
numbers = [1, 2, 3]
string_numbers = list(map(str, numbers))
joined = ", ".join(string_numbers)
print("Joined string:", joined)"""