# Number

# type() is a built-in function that returns the type of an object.

# Numbers
num = 5
print(type(num))
# Output: <class 'int'>

print(num.__class__)
# Output: <class 'int'>

# Floats
num = 5.2
print(type(num))
# Output: <class 'float'>

# Floats with scientific notation
num = 5.2e3
print(type(num))
# Output: <class 'float'>


# Mathmatic Operations
# Addition: +
# Subtraction: -
# Multiplication: *
# Division: /
# Floor Division: //
# Exponent: **
# Modulus: %

num = 5
print(num + 2)
# Output: 7

num = 5
print(num - 2)
# Output: 3

num = 5
print(num * 2)
# Output: 10

num = 5
print(num / 2)
# Output: 2.5

num = 5
print(num // 2)
# Output: 2

num = 5
print(num ** 2)
# Output: 25

num = 5
print(num % 2)
# Output: 1


# abs() function
print(abs(-5))
# Output: 5

# round() function
print(round(5.75))
# Output: 6

# round() with 2nd argument
print(round(5.75, 1))
# Output: 5.8

# Increment and Decrement
num = 5
num = num + 1
print(num)
# Output: 6

num = 5
num += 1
print(num)
# Output: 6

num = 5
num -= 1
print(num)
# Output: 4


# Comparison Operators
# Equal: ==
# Not Equal: !=
# Greater Than: >
# Less Than: <
# Greater or Equal: >=
# Less or Equal: <=

num_1 = 5
num_2 = 2

print(num_1 == num_2)
# Output: False

print(num_1 != num_2)
# Output: True

print(num_1 > num_2)
# Output: True

print(num_1 < num_2)
# Output: False

print(num_1 >= num_2)
# Output: True

print(num_1 <= num_2)
# Output: False


# Casting
num = '5'
print(type(num))
# Output: <class 'str'>

num_1 = '5'
num_2 = '2'
print(num_1 + num_2)
# Output: 52

# Convert string to int
num_1 = int(num_1)
num_2 = int(num_2)
print(num_1 + num_2)
# Output: 7

# int()
# float()
# complex()

# int()
num = 5.2
print(type(num))
# Output: <class 'float'>


num = 5.2
print(int(num))
# Output: 5

# float()
num = 5
print(type(num))
# Output: <class 'int'>

num = float(num)
print(num)
# Output: 5.0

# complex()
num = 5
print(type(num))
# Output: <class 'int'>

num = complex(num)
print(num)
# Output: (5+0j)


# zfill method (add leading zeros)
num = 5
print(str(num).zfill(3))
# Output: 005


