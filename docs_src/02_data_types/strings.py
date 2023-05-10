sentence = 'Hello World'
print(sentence)
# Output: Hello World

# Single quote vs Double quote
# Single quote is faster than double quote
# Single quote is more readable than double quote
# Single quote is more common than double quote

# use backslash to escape single quote
sentence = 'Tub\'s World'
print(sentence)
# Output: Tub's World

# or use double quote
sentence = "Tub's World"
print(sentence)
# Output: Tub's World

# three double quotes for multi-line string
sentence = """Tub's World
is a good place to live in"""
print(sentence)
# Output: Tub's World

# string length
sentence = "Tub's World"
print(len(sentence))
# Output: 12


# string indexing
# indexing starts from 0
sentence = "Tub's World"
print(sentence[0])
# Output: T

# if index is negative, it starts from the end
sentence = "Tub's World"
print(sentence[-1])
# Output: d

# if we input 11, it will throw an error
sentence = "Tub's World"
print(sentence[11])
# Output: IndexError: string index out of range


# string slicing
# slicing starts from 0
sentence = "Tub's World"
print(sentence[0:3])
# Output: Tub
# the first index is inclusive, the second index is exclusive

# we can also omit the first index
sentence = "Tub's World"
print(sentence[:3])
# Output: Tub

# we can also omit the second index
sentence = "Tub's World"
print(sentence[3:])
# Output: 's World

# we can also omit both index
sentence = "Tub's World"
print(sentence[:])
# Output: Tub's World

sentence = "Tub's World"
# Reverse index: 9876543210
print(sentence[-6:-1])
# Output: World

sentence = "Tub's World"
print(sentence[::2])
# Output: Tb sWrd

sentence = "Tub's World"
print(sentence[1:6:2])
# Output: u'


sentence = "Tub's World"
print(sentence[::-1])
# Output: dlroW s'b

sentence = "Tub's World"
print(sentence[-1:2:-1])
# Output: dlroW s'b


# lowercase
sentence = "Tub's World"
print(sentence.lower())
# Output: tub's world

# uppercase
sentence = "Tub's World"
print(sentence.upper())
# Output: TUB'S WORLD

# capitalize
sentence = "Tub's World"
print(sentence.capitalize())
# Output: Tub's world

# count (return the number of occurrences)
sentence = "Tub's World"
print(sentence.count('o'))
# Output: 1

# find (return the index of the first occurrence)
sentence = "Tub's World"
print(sentence.find('o'))
# Output: 8

# replace (replace old with new)
sentence = "Tub's World"
print(sentence.replace('Tub', 'Tom'))
# Output: Tom's World

# you can also assign the result to the same variable
sentence = "Tub's World"
sentence = sentence.replace('Tub', 'Tom')
print(sentence)
# Output: Tom's World


# String concatenation
name = 'Tub'
age = 5
sentence = name + ' is ' + str(age) + 'years old'
print(sentence)
# Output: Tub is 5 years old

# if we want to concatenate a lot of strings, it is better to use string formatting
name = 'Tub'
age = 5
# Method 1
sentence = '{} is {} years old'.format(name, age)
print(sentence)
# Output: Tub is 5 years old

# Method 2
# use format() method with keyword arguments
sentence = '{n} is {a} years old'.format(n=name, a=age)
print(sentence)
# Output: Tub is 5 years old

# Method 3
# use f-string
sentence = f'{name} is {age} years old'
print(sentence)
# Output: Tub is 5 years old

# With upper case
sentence = f'{name.upper()} is {age} years old'
print(sentence)
# Output: TUB is 5 years old


# dir() function
# dir() function returns a list of all attributes and methods of the specified object
name = 'Tub'
print(dir(name))
# Output: ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
# '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__',
# '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find',
# 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower',
# 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans',
# 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip',
# 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

# help() function
name = 'Tub'
print(help(str))

# Output: Help on class str in module builtins:
print(help(str.lower))


