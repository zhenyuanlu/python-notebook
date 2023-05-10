# 2. Data Types

## 2.1. Numbers

In this section, we will cover the different number types in Python, such as integers and floating-point numbers, and how to work with them.


### 2.1.1. Integers and Floats


Python has two primary numeric types: integers (int) and floating-point numbers (float). 

Assign an integer `5` to a variable named `num`. The `print()` function is then used to output the value of `num` to the console. 
```python title="Input"
# Integers
num = 5
print(num)
```
```title="Output" 
5
```

Assign a floating-point number `5.2` to a variable named `num`. The `print()` function is then used to output the value of `num` to the console.
```python title="Input"
# Floats
num = 5.2
print(num)
```
```title="Output"
5.2
```

### 2.1.2. `type()` and `__class__`

!!! info 
    `type()` is a built-in function that returns the type of an object. It is the same as calling the object's `__class__` attribute, e.g. `object.__class__`, but which is less commonly used.

Use `type()` to check the type of a variable.
```python title="Input"
num = 5
print(type(num))
```
```title="Output"
<class 'int'>
```

The num variable is a floating-point number, so the `type()` function returns `<class 'float'>`.

```python title="Input"
# Floats
num = 5.2
print(type(num))
```
```title="Output"
<class 'float'>
```

Floats with scientific notation.
```python title="Input"
num = 5.2e3
print(type(num))
```
```title="Output"
<class 'float'>
```

Use `__class__` to check the type of a variable. 
```python title="Input"
print(num.__class__)
```
```title="Output"
<class 'int'>
```


### 2.1.3. Math Functions

Python supports various mathematical operations that can be performed on numbers, such as addition, subtraction, multiplication, division, and more. Here's a list of common mathematical operations and their corresponding symbols:

- Addition: `+`
- Subtraction: `-`
- Multiplication: `*`
- Division: `/`
- Floor Division: `//`
- Exponentiation: `**`
- Modulus: `%`

Let's see some examples of using these mathematical operations:





=== "Addition"

    ```python title="Input"
    num = 5
    print(num + 2)
    ```
    ```title="Output"
    7
    ```

=== "Subtraction"

    ```python title="Input"
    num = 5
    print(num - 2)
    ```
    ```title="Output"
    3
    ```

=== "Multiplication"

    ```python title="Input"
    num = 5
    print(num * 2)
    ```
    ```title="Output"
    10
    ```

=== "Division"

    ```python title="Input"
    num = 5
    print(num / 2)
    ```
    ```title="Output"
    2.5
    ```

=== "Floor Division"

    ```python title="Input"
    num = 5
    print(num // 2)
    ```
    ```title="Output"
    2
    ```

=== "Exponentiation"

    ```python title="Input"
    num = 5
    print(num ** 2)
    ```
    ```title="Output"
    25
    ```

=== "Modulus"

    ```python title="Input"
    num = 5
    print(num % 2)
    ```
    ```title="Output"
    1
    ```

These operations can be used in combination, following the standard order of operations (PEMDAS), to perform more complex calculations. Parentheses can be used to specify the order of operations explicitly.

**`abs()` and `round()`**

`abs()` and `round()` are two built-in functions that can be used to perform mathematical operations on numbers. 


The `abs()` function returns the absolute value of a number.

```python title="Input"
# abs() function
print(abs(-5))
```
```title="Output"
5
```

The `round()` function rounds a number to a specified number of decimal places.

```python title="Input"
# round() function
print(round(5.75))
```
```title="Output"
6
```

`round()` with 2nd argument to specify the number of decimal places. Here we round `5.75` to 1 decimal place.

```python title="Input"
# round() with 2nd argument
print(round(5.75, 1))
```
```title="Output"
5.8
```


### 2.1.4. Increment and Decrement

In Python, you can increment or decrement the value of a variable using the `+=` and `-=` operators, respectively. These operators are shorthand for adding or subtracting a value to the variable and then assigning the result back to the variable.

We use `num = num + 1` to increment the value of `num` by 1. 
```python title="Input"
# Increment
num = 5
num = num + 1
print(num)
```
```title="Output"
6
```

Increment using shorthand `+=` operator. The `+=` operator is equivalent to `num = num + 1`.


```python title="Input"
# Increment using shorthand +=
num = 5
num += 1
print(num)
```
```title="Output"
6
```

The `num = num - 1` is used to decrement the value of `num` by 1.
```python title="Input"
# Decrement
num = 5
num = num - 1
print(num)
```
```title="Output"
4
```

Decrement using shorthand `-=` operator. The `-=` operator is equivalent to `num = num - 1`.
```python title="Input"
# Decrement using shorthand -=
num = 5
num -= 1
print(num)
```
```title="Output"
4
```

Using the `+=` and `-=` operators can make your code shorter and more readable, especially when performing multiple increment or decrement operations on the same variable.


### 2.1.5. Comparison Operators



- Equal: `==`
- Not Equal: `!=`
- Greater Than: `>`
- Less Than: `<`
- Greater or Equal: `>=`
- Less or Equal: `<=`

```python title="Setting"
num_1 = 5
num_2 = 2
```

=== "Equal: =="

    ```python title="Input"
    print(num_1 == num_2)

    ```
    ```title="Output"
    False
    ```

=== "Not Equal: !="

    ```python title="Input"
    print(num_1 != num_2)
    ```
    ```title="Output"
    True
    ```

=== "Greater Than: >"

    ```python title="Input"
    print(num_1 > num_2)
    ```
    ```title="Output"
    True
    ```

=== "Less Than: <"

    ```python title="Input"
    print(num_1 < num_2)
    ```
    ```title="Output"
    False
    ```



=== "Greater or Equal: >="

    ```python title="Input"
    print(num_1 >= num_2)
    ```
    ```title="Output"
    True
    ```

=== "Less or Equal: <="

    ```python title="Input"
    print(num_1 <= num_2)
    ```
    ```title="Output"
    False
    ```



### 2.1.6. Casting

Casting is the process of converting a value from one data type to another. In Python, casting is achieved using built-in functions like `int()`, `float()`, and `complex()`.

For example, when working with numbers, you might need to convert a string to an integer or a float. This is useful when you want to perform mathematical operations on string representations of numbers.

`int()`: Convert a value to an integer
`float()`: Convert a value to a float
`complex()`: Convert a value to a complex number

Check the type of variable `num_1`. 

```python title="Input"
num_1 = '5'
print(type(num_1))
```
```title="Output"
<class 'str'>
```

If we have two numbers as strings, when we `+` them, they are concatenated instead of added.

```python title="Input"
num_1 = '5'
num_2 = '2'
print(num_1 + num_2)
```
```title="Output"
52
```

If we want to add them, we need to convert them to integers first.

```python title="Input"
# Convert string to int
num_1 = int(num_1)
num_2 = int(num_2)
print(num_1 + num_2)
```
```title="Output"
7
```

If we convert a floating number to an integer, the decimal part will be removed.

```python title="Input"
num = 5.2
print(int(num))
```
```title="Output"
5
```

If we convert an integer to a float, the result will be a float with `.0` at the end.

```python title="Input"
# float()
num = 5
print(float(num))
```
```title="Output"
5.0
```

If we convert an integer to a complex number, the result will be a complex number with `j` at the end.

```python title="Input"
# complex()
num = 5
print(complex(num))
```
```title="Output"
(5+0j)
```

`zfill()` method adds zeros (0) at the beginning of the string, until it reaches the specified length.

```python title="Input"
# zfill method
num = 5
print(str(num).zfill(3))
```
```title="Output"
005
```



## 2.2. Strings

Strings are one of the most important and commonly used data types in Python. A string is simply a sequence of characters, such as letters, numbers, and symbols. In Python, strings are created using either single quotes `'<str>'` or double quotes `"<str>"`. This tutorial will cover the basics of string manipulation in Python, including string indexing, slicing, concatenation, formatting, and various string methods.


A string variable named sentence is defined and assigned the value `"Hello World"`. The `print()` function is then used to output the value of sentence to the console. This code demonstrates how to create and output a basic string in Python. 

```python title="Input"
sentence = 'Hello World'
print(sentence)
```
```title="Output"
Hello World
```

### 2.2.1. String Basics
**Quotes**

Single quotes are faster, more readable, and more commonly used than double quotes in Python. However, if a string itself contains a single quote, then it must be escaped using a backslash \ so that Python can properly interpret the string.

In the example code, a new string variable named sentence is defined using single quotes and contains the word `"Tub's World"`. To escape the single quote in the middle of the string, a backslash is used before it. The `print()` function is then used to output the value of sentence to the console. 

```python title="Input"
# Single quote
# Use backslash to escape single quote
sentence = 'Tub\'s World'
print(sentence)
```
```title="Output"
Tub's World
```

The following is the same example as above, but using double quotes instead of single quotes. 

``` python title="Input"
# Use double quote
sentence = "Tub's World"
print(sentence)
```
```title="Output"
Tub's World
```

Triple quotes are used to create multi-line strings. In the example code, a new string variable named sentence is defined using triple quotes and contains the string `"Tub's World"` and `"is a good place to live in"`. The `print()` function is then used to output the value of sentence to the console. 

```python title="Input"
# Three double quotes for multi-line string
sentence = """Tub's World
is a good place to live in"""
print(sentence)
```
```title="Output"
Tub's World
is a good place to live in
```

**Length of a String**

The following code demonstrates how to use the `len()` function to get the length of a string.

```python title="Input"
# Use len() to get the length of a string
sentence = "Tub's World"
print(len(sentence))
```
```title="Output"
12
```

**Upper and Lower Case**

The `lower()` method converts all the characters in a string to lowercase. This is useful for case-insensitive comparisons or normalization of text data.

```python title="Input"
# Lowercase (all letters)
sentence = "Tub's World"
print(sentence.lower())
```
```title="Output"
tub's world
```

The `upper()` method converts all the characters in a string to uppercase.

```python title="Input"
# Uppercase (all letters)
sentence = "Tub's World"
print(sentence.upper())
```
```title="Output"
TUB'S WORLD
```

```python title="Input"
# Capitalize
sentence = "Tub's World"
print(sentence.capitalize())
```
```title="Output"
Tub's world
```

The `capitalize()` method capitalizes the first character of a string and makes the rest of the characters lowercase.



### 2.2.2. String Indexing
Indexing allows us to access individual characters within a string using their position, also known as the index. It is essential to understand that in Python, indexing starts from 0, meaning the first character in the string has an index of 0, the second character has an index of 1, and so on.


Here, we define a string sentence containing the text `"Tub's World"`. We then use indexing to access the character at position 0, which is `'T'`. The `print()` function displays the output, confirming that the first character in the string is indeed `'T'`.

```python title="Input"
# String indexing
# Indexing starts from 0
sentence = "Tub's World"
print(sentence[0])
```
```title="Output"
T
```


Now, let's see how negative indexing works in Python:

```python title="Input"
# If index is negative, it starts from the end
sentence = "Tub's World"
print(sentence[-1])
```
```title="Output"
d
```

Accessing an index that is out of range will result in an error.
```python title="Input"
# If we input 11, it will throw an error
sentence = "Tub's World"
print(sentence[11])
```
```title="Output"
IndexError: string index out of range
```

### 2.2.3. String Slicing

String slicing is a technique used to extract a subset of characters from a string. Slicing is done by specifying the starting and ending indices of the slice, separated by a colon. The starting index is inclusive, and the ending index is exclusive. If either the starting or ending index is omitted, it defaults to the beginning or end of the string, respectively.

!!! note "Basic Indexing"
    ```python title="Input"
    # The first index is inclusive, the second index is exclusive
    sentence = "Tub's World"
    # Index: 012345678910
    # Reverse index: 9876543210
    ```
    ```python title="Basic Syntax"
    # string[start:end:step]
    sentence = "Tub's World"
    # sentence[index:index:step]
    ```


```python title="Input"
# The first index is inclusive, the second index is exclusive
sentence = "Tub's World"
# Index: 012345678910
print(sentence[0:3])
```
```title="Output"
Tub
```

```python title="Input"
# We can also omit the first index
sentence = "Tub's World"
print(sentence[:3])
```
```title="Output"
Tub
```


```python title="Input"
# We can also omit the second index
sentence = "Tub's World"
print(sentence[3:])
```
```title="Output"
's World
```

```python title="Input"
# We can also omit both index
sentence = "Tub's World"
print(sentence[:])
```
```title="Output"
Tub's World
```

**Reverse Slicing**

If we want to print out the `World`, we can use reverse indexing to get the last 5 characters:
```python title="Input"
sentence = "Tub's World"
# Reverse index: 9876543210
print(sentence[-6:-1])
```
```title="Output"
World
```

**Step Size**

We can also specify a step size to skip characters in the string. The following code demonstrates how to use a step size of 2 to print out every other character in the string:

```python title="Input" 
# Step size
sentence = "Tub's World"
print(sentence[::2])
```
```title="Output"
Tb sWrd
```


We can also specify a step size of 2 to print out every other character in the string, starting from the second character to the :
```python title="Input" 
# Step size
sentence = "Tub's World"
print(sentence[1:6:2])
```
```title="Output"
u'
```


**Negative Step Size**

We can also use a negative step size to reverse the string:

```python title="Input"
# Negative step size
sentence = "Tub's World"
print(sentence[::-1])
```
```title="Output"
dlroW s'buT
```

We can also print out the same result by using the following code:

```python title="Input"
sentence = "Tub's World"
print(sentence[-1:2:-1])
```
```title="Output"
dlroW s'buT
```



### 2.2.4. `count()`, `find()`, and `replace()`

The `count()`, `find()`, and `replace()` methods are used to count, find, and replace substrings within a string, respectively.

`count()` returns the number of occurrences of a specified substring in the given string.

```python title="Input"
# Count (return the number of occurrences)
sentence = "Tub's World"
print(sentence.count('o'))
```
```title="Output"
1
```


`find()` returns the index of the first occurrence of a specified substring in the given string.

```python title="Input"
# Find (return the index of the first occurrence)
sentence = "Tub's World"
print(sentence.find('o'))
```
```title="Output"
8
```

`replace()` replaces all occurrences of a specified substring (old) with a new substring in the given string.

```python title="Input"
# Replace (replace old with new)
sentence = "Tub's World"
print(sentence.replace('Tub', 'Tom'))
```
```title="Output"
Tom's World
```

We can also assign the result of the replace() method back to the same variable if we want to update the original string:
```python title="Input"
# We can also assign the result to the same variable
sentence = "Tub's World"
sentence = sentence.replace('Tub', 'Tom')
print(sentence)
```
```title="Output"
Tom's World
```


### 2.2.5. String Concatenation
String concatenation is a technique used to join two or more strings together. In Python, string concatenation is done using the `+` operator.

```python title="Input"
# String concatenation
name = 'Tub'
age = 5
sentence = name + 'is' + str(age) + 'years old'
print(sentence)
```
```title="Output"
Tub is 5 years old
```

String concatenation is essential when working with dynamic content, such as user input or data from external sources, as it enables you to construct meaningful and contextually relevant strings. When concatenating strings, it's essential to pay attention to spaces and punctuation to ensure the resulting string is formatted correctly. For instance, in this example, we've added a space character between the punctuation and noun variables to separate the words in the final string.

### 2.2.6. String Formatting
String formatting is a technique used to embed values within a string. In Python, there are several ways to format strings, including using the `format()` method and using f-strings. The `format()` method allows you to embed values within a string using placeholders, which are represented by curly braces `{}`. You can also use named placeholders to improve the readability of your code. F-strings are a more recent addition to Python and provide a more concise and intuitive way to embed values within a string.

Here, we have three string variables: `name`, and an integer variable `age`. We introduce three methods for including non-string variables in a string using string formatting:

```python title="Input: Setting up variables"
# If we want to concatenate a lot of strings, 
# it is better to use string formatting
name = 'Tub'
age = 5
```
Method 1: Using the `format()` method
```python title="Input"
# Method 1
# Use format() method
sentence = '{} is {} years old'.format(name, age)
print(sentence)
```
```title="Output"
Tub is 5 years old
```

Method 2: Using the `format()` method with keyword arguments
```python title="Input"
# Method 2
# use format() method with keyword arguments
sentence = '{n} is {a} years old'.format(n=name, a=age)
print(sentence)
```
```title="Output"  
Tub is 5 years old
```

Method 3: Using `f`-strings (Python 3.6+)
```python title="Input"
# Method 3
# Use f-string (3.6+)
sentence = f'{name} is {age} years old'
print(sentence)
```
```title="Output"
Tub is 5 years old
```


In addition to the methods above, we can also modify the string content within the string formatting. In this case, we convert the name variable to uppercase using the `.upper()` method:

```python title="Input" 
# With upper case
sentence = f'{name.upper()} is {age} years old'
print(sentence)
```
```title="Output"  
TUB is 5 years old
```

All three methods allow you to easily include non-string variables in your string, without the need for explicit type conversion, making them more efficient and readable than traditional string concatenation.

### 2.2.7. `dir()` and `help()`

The `dir()` function returns a list of all attributes and methods of the specified object, while the `help()` function provides documentation on a specific attribute or method.

We pass the name variable, which is a string, to the dir() function. This will return a list of all available attributes and methods for the string object.

```python title="Input"
# dir() function returns a list of all 
# attributes and methods of the specified object
name = 'Tub'
print(dir(name))
```
```title='Output'
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
 '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__',
 '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__',
 '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__',
 '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find',
 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower',
 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans',
 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip',
 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

We can also use `help()` function to display information about the string variable, but instead of passing the variable name, we pass the string object `str` itself. 

```python title="Input"
# help() function
name = 'Tub'
print(help(str))
```
```title="Output (partial)"
Help on class str in module builtins:...
...
```


## 2.3. Lists

Lists in Python are ordered, mutable collections of items. They can store elements of different types, such as strings, integers, or other objects.

Creating a list with pet names:

```python title="Input"
# A list of pets names
pet = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
print(pet)
```
```title="Output"
['Tub', 'Furrytail', 'Cat', 'Barkalot']
```

Create an empty list using the `[]` or `list()` function:
```python title="Input"
# Create empty list
empty_list = []
# or
empty_list = list()
print(empty_list)
```
```title="Output"
[]
```

### 2.3.1. List Indexing

Check the length of the list using the `len()` function:
```python title="Input"
pet = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
print(len(pet))
```
```title="Output"
4
```

In Python the first element of a list has index `0`, which is different from other programming languages, e.g. R, where the first element has index `1`.

Access the first element of the list using the index `0`:

```python title="Input"
# Indexing starts from 0
pet = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
print(pet[0])
```
```title="Output"
Tub
```

Access the last element of the list using the index `-1`:
```python title="Input"
# If index is negative, it starts from the end
pet = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
print(pet[-1])
```
```title="Output"
Barkalot
```

Access the second element of the list using the index `1`:
```python title="Input"
```python title="Input"
# If we input 4, it will throw an error
pet = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
print(pet[4])
```
```title="Output"
IndexError: list index out of range
```

### 2.3.2. List Slicing

Slicing is a way to access a subset of a list. We can use the colon `:` to specify the start and end index of the slice. The slice will include the start index, but not the end index.

!!! note "Basic Indexing for List Slicing"
    ```python title="Basic Indexing"
    # Index: 0  1  2  3
    # Reverse index : -4 -3 -2 -1
    pet = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
    ```

    ```python title="Basic Syntax"
    # list[start:end:step]
    pet = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
    # pet[index:index:step]
    ```


Slice the first two elements of the list:
```python title="Input"
# Slicing starts from 0
pet = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
print(pet[0:2])
```
```title="Output"
['Tub', 'Furrytail']
```

If we omit the start index, the slice will start from the beginning of the list:
```python title="Input"
# Omit the first index
pet = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
print(pet[:2])
```
```title="Output"
['Tub', 'Furrytail']
```

If we omit the end index, the slice will end at the end of the list:
```python title="Input"
# Omit the second index
pet = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
print(pet[2:])
```
```title="Output"
['Cat', 'Barkalot']
```

We can also omit both indices to return the entire list:
```python title="Input"
# Omit both index
pet = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
print(pet[:])
```
```title="Output"
['Tub', 'Furrytail', 'Cat', 'Barkalot']
```

**Reverse Slicing**
Recall that the index `-1` refers to the last element of the list. We can use this to reverse the list:
```python title="Input" 
# Reverse Index: -5, -4, -3, -2, -1
numbers_list = [1, 2, 3, 4, 5]
print(numbers_list[-3:-1])
```
```title="Output"
[3, 4]
```

If we want to all the way from the last element to the `-3` index (not including the `-3` index), we can omit the last index:
```python title="Input"
print(numbers_list[-3:])
```
```title="Output"
[3, 4, 5]
```

Or we can omit the first index to all the way from the first element to the `-3` index (not including the `-3` index):
```python title="Input"
print(numbers_list[:-3])
```
```title="Output"
[1, 2]
```

We can also use positive step size to reverse the list:
```python title="Input"
print(numbers_list[1:-2])
```
```title="Output"
[2, 3]
```

**Step Size**

We can also specify the step size of the slice. For example, we can slice every other element of the list by specifying the step size as `2`:
```python title="Input"
```python title="Input"
numbers_list = [1, 2, 3, 4, 5]
# list[start:end:step]
print(numbers_list[0:3:2])
```
```title="Output"
[1, 3]
```

The default step size is `1`. We can omit the step size if we want to slice every element of the list:

Omit the step size:
```python title="Input"
print(numbers_list[0:3])
```
```title="Output"
[1, 2, 3]
```

With step size `1`:
```python title="Input"
print(numbers_list[0:3:1])
```
```title="Output"
[1, 2, 3]
```

We can also use negative step size to reverse the list:
```python title="Input"
print(numbers_list[0:3:-1])
```
```title="Output"
[]
```
However, this will return an empty list. Since the step size is negative number `-1`, the slice will start from the `0` index and then move backward to the `-1` index, which is on the opposite direction of index `3`. Therefore, it returns an empty list.

To fix this, we can reverse the start and end index:
```python title="Input"
print(numbers_list[-3::-1])
```
```title="Output"
[3, 2, 1]
```

We can also omit the start and end index to include the entire list, by a step of `-2`:
```python title="Input"
print(numbers_list[::-2])
```
```title="Output"
[5, 3, 1]
```



### 2.3.2. List Methods
There are many methods that can be used with lists. In the following examples, we will introduce couple of common methods to manipulate the list. 

Add an item to the end of the list using the `append()` method:
```python title="Input"
# Add an item to the end of the list
pet = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
pet.append('Hootsworth ')
print(pet)
```
```title="Output"
['Tub', 'Furrytail', 'Cat', 'Barkalot', 'Hootsworth ']
```

Add an item to a specific index, e.g. `2`, using the `insert()` method:
```python title="Input"
# Add an item to a specific index
pet = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
pet.insert(2, 'Fish')
print(pet)
```
```title="Output"
['Tub', 'Furrytail', 'Fish', 'Cat', 'Barkalot']
```

Now, we want to insert a list into a list after a specific location, e.g. 0, using the `insert()` method:
```python title="Input"
# Insert a list into a list
pet = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
pet_2 = ['Bumblefluff ', 'Whiskerfloof']
pet.insert(0, pet_2)
print(pet)
```
```title="Output"
[['Bumblefluff ', 'Whiskerfloof'], 'Tub', 'Furrytail', 'Cat', 'Barkalot']
```

!!! warning "`insert()` method inserts the list as a single element"
    However, this is not what we want because we want to insert the elements of the list `pet_2` into the list `pet`. 


Then we can use the `extend()` instead to do this:
```python title="Input"
# Extend a list
pet = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
pet_2 = ['Bumblefluff ', 'Whiskerfloof']
pet.extend(pet_2)
print(pet)
```
```title="Output"
['Tub', 'Furrytail', 'Cat', 'Barkalot', 'Bumblefluff ', 'Whiskerfloof']
```
Now, we have successfully inserted the elements of the list `pet_2` into the list `pet`.

We can remove an item from the list using the `remove()` method:
```python title="Input"
# Remove an item from the list
pet = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
pet.remove('Tub')
print(pet)
```
```title="Output"
['Furrytail', 'Cat', 'Barkalot']
```

We can also remove an item from the list using the `pop()` method. If we do not specify the index, it will remove the last item from the list:
```python title="Input"
pet = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
pet.pop()
print(pet)
```
```title="Output"
['Tub', 'Furrytail', 'Cat']
```

Or we can specify the index to remove the item at that index:
```python title="Input"
pet = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
pet.pop(1)
print(pet)
```
```title="Output"
['Tub', 'Cat', 'Barkalot']
```

We can also use the `pop()` method to get the item that we removed from the list, and assign it to the `popped_sp` variable:
```python title="Input"
pet = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
popped_pet = pet.pop()
print(popped_pet)
```
```title="Output"
Barkalot
```
This is very helpful when we have a queue to keep popping until the queue is empty and we want to keep track of the items that we have popped.

If we want to search for an index of an item in the list, we can use the `index()` method:
```python title="Input"
# Search for an index of an item in the list
pet = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
print(pet.index('Tub'))
```
```title="Output"
0
```

We can check if the `'Tub'` is in the pet list using the `in` keyword:
```python title="Input"
# If an item is in the list
print('Tub' in pet)
```
```title="Output"
True
```

Sometimes, we want to join a list of strings into a single string. We can use the `join()` method to do this:
```python title="Input"
# Join a list of strings
pet = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
pet_str = ','.join(pet)
print(pet_str)
```
```title="Output"
Tub,Furrytail,Cat,Barkalot
```

Or we can split the single string into a list by a specific character, e.g. `,`:
```python title="Input"
# Split a string into a list by ','
pet_str = 'Tub,Furrytail,Cat,Barkalot'
pet_list = pet_str.split(',')
print(pet_list)
```
```title="Output"
['Tub', 'Furrytail', 'Cat', 'Barkalot']
```

When dealing with a list of numbers, we can use the `min()`, `max()`, and `sum()` functions to get the minimum, maximum, and sum of the numbers in the list:

=== "`min()`"

    ```python title="Input"
    nums = [5, 3, 2, 4, 1]
    print(min(nums))
    ```
    ```title="Output"
    1
    ```

=== "`max()`"

    ```python title="Input"
    nums = [5, 3, 2, 4, 1]
    print(max(nums))
    ```
    ```title="Output"
    5
    ```

=== "`sum()`"

    ```python title="Input"
    nums = [5, 3, 2, 4, 1]
    print(sum(nums))
    ```
    ```title="Output"
    15
    ```


### 2.3.3. Sorting and Reversing

We can reverse a list of strings using the `reverse()` method in reverse alphabetical order:
```python title="Input"
# Reverse a list
pet = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
pet.reverse()
print(pet)
```
```title="Output"
['Barkalot', 'Cat', 'Furrytail', 'Tub']
```

We can sort a list of strings using the `sort()` method in alphabetical order:
```python title="Input"
# Sort a list
pet = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
pet.sort()
print(pet)
```
```title="Output"
['Barkalot', 'Cat', 'Furrytail', 'Tub']
```


We can sort a list of numbers using the `sort()` method in alphabetical order:
```python title="Input"
nums = [5, 3, 2, 4, 1]
nums.sort()
print(nums)
```
```title="Output"
[1, 2, 3, 4, 5]
```

Of course, we can also sort a list of numbers in reverse order by using `sort(reverse = True)`:
```python title="Input"
# Instead of using .reverse(), we can use reverse = True
nums.sort(reverse = True)
print(nums)
```
```title="Output"
[5, 4, 3, 2, 1]
```

However, the above methods `sort()` and `reverse()` are changing our original variables. What if we want to keep the original variables? We can use the `sorted()` function to sort a list of strings in alphabetical order:
```python title="Input"
pet = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
sorted_pet = sorted(pet)
print(sorted_pet)
print(pet)
```
```title="Output"
['Barkalot', 'Cat', 'Furrytail', 'Tub'] # sorted_pet
['Tub', 'Furrytail', 'Cat', 'Barkalot'] # original pet
```
Here, we don't change the original variable `pet` but create a new variable `sorted_pet` to store the sorted list. This is useful when we want to keep the original list unchanged.


## 2.4. Tuples

Tuples are similar to lists, but they are immutable. This means that we cannot change the contents of a tuple once it is created. Tuples are useful when we want to store a list of items that cannot be changed. 

### 2.4.1. Creating a Tuple
Create an empty tuple is similar to creating an empty list, the only difference is that we use `()` instead of `[]`, or you can use the `tuple()` function:
```python title="Input"
# Create empty tuple
empty_tuple = ()
# or
empty_tuple = tuple()
print(empty_tuple)
```
```title="Output"
()
```

Create a tuple based on the same strings as the list `pet`:
```python title="Input"
pet_tup_1 = ('Tub', 'Furrytail', 'Cat', 'Barkalot')
print(pet_tup_1)
```
```title="Output"
('Tub', 'Furrytail', 'Cat', 'Barkalot')
```

## 2.5. Immutable vs. Mutable
Immutable means that we cannot change the contents of the object. Mutable means that we can change the contents of the object. 

Here's a general overview of the advantages and disadvantages of mutable and immutable objects:

**Pros and Cons of Immutable**
=== "Pros of Immutable"
    !!! note
        **Simplicity**: Immutability makes the code easier to reason about, as you don't have to worry about unintentional changes to the object.

        **Hashable**: Immutable objects can be used as keys in dictionaries, as their content remains constant and their hash values do not change over time.

        **Optimization**: Immutable objects allow languages and compilers to perform certain optimizations that can improve the performance of a program.

        **Thread-safety**: Immutable objects are inherently thread-safe, as multiple threads cannot modify them simultaneously. This property eliminates the need for locking mechanisms when working with immutable objects in multi-threaded environments.

        **Predictability**: When you pass an immutable object to a function, you can be sure that the function will not modify the object, which ensures that the behavior of the program remains predictable.

=== "Cons of Immutable"
    !!! note
        **Memory overhead**: Since each operation on an immutable object creates a new object, it can lead to increased memory usage, especially when manipulating large objects or performing many operations.

        **Performance**: Creating new objects for each operation can be slower than modifying objects in-place, particularly in cases where the program performs many operations on objects. In such situations, using mutable data structures may be more efficient.


**Pros and Cons of Mutable**
=== "Pros of Mutable"
    !!! note
        **In-place modification**: Mutable objects can be modified in-place, which can lead to better performance and lower memory usage, especially when working with large objects or performing many operations on objects.

        **Flexibility**: Mutable objects offer more flexibility in how you can manipulate and change data, which can be helpful in certain scenarios.

=== "Cons of Mutable"
    !!! note
        **Complexity**: Mutable objects can make code harder to reason about, as you need to consider the possibility of unintentional changes to the object.

        **Thread-safety**: Mutable objects are not inherently thread-safe, and using them in multi-threaded environments can lead to race conditions and other concurrency-related issues if proper locking mechanisms are not in place.

        **Predictability**: When you pass a mutable object to a function, you cannot be sure whether the function will modify the object or not, which can make the behavior of the program less predictable.

        **Not hashable**: Mutable objects cannot be used as keys in dictionaries, as their content can change, potentially causing issues with hashing.






### 2.5.1. String is Immutable
Strings in Python are immutable, meaning you cannot change their content directly. Instead, when you perform operations like concatenation, replacement, changing the case, or slicing, you create new strings rather than modifying the original ones.

**Concatenation**

```python title="Input"
original_string = "Hello, "
pet = "Tub"

greeting = original_string + pet
print(greeting)
print('Address of original_string is: {}'.format(id(original_string)))
print('Address of greeting is: {}'.format(id(greeting)))
```
```title="Output"  
Hello, Tub  
Address of original_string is: 2186723937904
Address of greeting is: 2186728523312
```
As you can see, the memory addresses of the original string and the new string are different, confirming that a new string is created during concatenation.

**Replace**

The replace() method in Python is used to replace a specified value with another value in a string. When you use the `replace()` method, a new string is created, and the original string remains unchanged.

```python title="Input"
original_string = "Hello, World!"

new_string = original_string.replace("World", "Tub")
print(new_string)
print('Address of original_string is:{}'.format(id(original_string)))
print('Address of new_string is:{}'.format(id(new_string)))
```
```title="Output"
Hello, Tub
Address of original_string is:1436882337200
Address of new_string is:1436885468848
```
Again, the memory addresses of the original string and the new string are different, confirming that a new string is created during the replacement.


**Change the Case**

```python title="Input"
original_string = "Tub is awesome!"

uppercase_string = original_string.upper()
print(uppercase_string)
print('Address of original_string is:{}'.format(id(original_string)))
print('Address of uppercase_string is:{}'.format((id(uppercase_string))))
```
```title="Output"
TUB IS AWESOME!
Address of original_string is:1923265193776
Address of uppercase_string is:1923268233008
```
Again, the memory addresses of the original string and the new string are different.

Then you may ask what is the advantage of immutable: 

**Slicing**
When you slice a string, a new string is created, and the original string remains unchanged.

```python title="Input"
original_string = "Tub is cute!"

substring = original_string[0:3]
print(substring)
print('Address of original_string is:{}'.format(id(original_string)))
print('Address of substring is:{}'.format(id(substring)))
```
```title="Output"
Tub
Address of original_string is:1923265193776
Address of substring is:1923268233008
```


### 2.5.1. List is Mutable

```python title="Input"
pet_1 = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
pet_2 = pet_1
pet_1[1] = 'Furrytail 2'
print(pet_1)
print(pet_2)
```
```title="Output"
['Tub', 'Furrytail 2', 'Cat', 'Barkalot']
['Tub', 'Furrytail 2', 'Cat', 'Barkalot']
```
We can see that when we change the contents of `pet_1`, the contents of `pet_2` also change. This is because `pet_1` and `pet_2` are both references to the same list in memory.

```python title="Input"
print('Address of pet_1 is: {}'.format(id(pet_1)))
print('Address of pet_2 is: {}'.format(id(pet_2)))
```
```title="Output"
Address of pet_1 is: 2250825683136
Address of pet_2 is: 2250825683136
```
The address of `pet_1` and `pet_2` are the same, which means they are both references to the same list in memory.



!!! tip "Python vs. R in Variable Assignment"
    Python and R handle variable assignment differently, particularly when it comes to mutable objects like lists in Python.

    In R, when you assign one variable to another, it creates a copy of the original variable's data. This means that if you change one variable's contents, the other variable's contents remain unchanged. This behavior is known as "copy-on-write" and allows R to save memory by not duplicating data until it is necessary.

    In Python, when you assign one variable to another, you are actually creating a reference to the original variable's data, rather than copying the data itself. This means that if you change the contents of one variable, the other variable's contents will also change because they both point to the same data in memory.


If you want to create a new list that is a copy of `pet_1` like that in R and not a reference to `pet_1`, you can use the `copy()` method:
```python title="Input"
pet_1 = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
pet_2 = pet_1.copy()
pet_1[1] = 'Furrytail 2'
print(pet_1)
print(pet_2)
```
```title="Output"
['Tub', 'Furrytail 2', 'Cat', 'Barkalot']
['Tub', 'Furrytail', 'Cat', 'Barkalot']
```
We can see that when we change the contents of `pet_1`, the `pet_2` remain unchanged. This is because `pet_2` refers to a new list that is a copy of `pet_1`.

```python title="Input"
print('Address of pet_1 is: {}'.format(id(pet_1)))
print('Address of pet_2 is: {}'.format(id(pet_2)))
```
```title="Output"
Address of pet_1 is: 1704413046016
Address of pet_2 is: 1704413120128
```
The address of `pet_1` and `pet_2` are different.


### 2.5.2. Tuple is Immutable
In the other hand, tuple is immutable, so we cannot change the contents of a tuple once it is created. For example, we cannot change the second item `Furrytail` in the tuple `pet_tup_1`:
```python title="Input"
# Immutable
pet_tup_1 = ('Tub', 'Furrytail', 'Cat', 'Barkalot')
pet_tup_1[1] = 'Furrytail 2'
print(pet_tup_1)
```
```title="Output"
TypeError: 'tuple' object does not support item assignment
```
Here we get an error message `TypeError: 'tuple' object does not support item assignment` on changing the second item in the `pet_tup_1` tuple.


## 2.6. Dictionaries
Dictionaries are similar to lists, but instead of using an index to access an item, we use a key. Dictionaries are unordered, and we cannot sort them. Dictionaries are mutable, so we can change the contents of a dictionary once it is created.

### 2.6.1. Creating a Dictionary

Let's create a dictionary that stores one of our old friend `'Tub'`, its `age`, and favoriate `habitat`:
```python title="Input"
pet = {'species': 'Tub', 'age': 5, 'habitat': ['bathroom', 'kitchen']}
print(pet)
```
```title="Output"
{'species': 'Tub', 'age': 5, 'habitat': ['bathroom', 'kitchen']}
```

### 2.6.2. Accessing Items in a Dictionary

We can access the items in a dictionary by using the key `'species'`, `'age'`, and `'habitat'`:
```python title="Input"
print(pet['species'])
print(pet['age'])
print(pet['habitat'])
```
```title="Output"
Tub
5
['bathroom', 'kitchen']
```

Of course, we can use number as the key, but it is not recommended:
```python title="Input"
pet = {1: 'Tub', 'age': 5, 'habitat': ['bathroom', 'kitchen']}
print(pet[1])
```
```title="Output"
Tub
```

What if we accidently acces a key that not exist in the dictionary?
```python title="Input"
# Access a key that not exist
pet = {'species': 'Tub', 'age': 5, 'habitat': ['bathroom', 'kitchen']}
print(pet['weight'])
```
```title="Output"
KeyError: 'weight'
```
We will get an error message `KeyError: 'weight'`. 

But practically this is not ideal, sometimes we just want to check if the key is in the dictionary or not without showing error, but return a `flag`. 

We can use `get()` method to do this:
```python title="Input"
# Get method
pet = {'species': 'Tub', 'age': 5, 'habitat': ['bathroom', 'kitchen']}
print(pet.get('age'))
print(pet.get('weight'))
```
```title="Output"
5
None
```
We can see that when we use `get()` method, if the key is in the dictionary, it will return the value of the key, e.g. `5`, but if the key is not in the dictionary, it will return `None`.

We can also specify a default value to return if the key is not in the dictionary instead of `None`:
```python title="Input"
pet = {'species': 'Tub', 'age': 5, 'habitat': ['bathroom', 'kitchen']}
print(pet.get('weight', 'Not there'))
```
```title="Output"
Not there
```

### 2.6.3. Changing Items in a Dictionary

We can update the value of a key, e.g. `'weight'`:
```python title="Input"
pet = {'species': 'Tub', 'age': 5, 'habitat': ['bathroom', 'kitchen']}
pet['weight'] = 2000
print(pet)
```
```title="Output"
{'species': 'Tub', 'age': 5, 'habitat': ['bathroom', 'kitchen'], 'weight': 2000}
```

We can also use `update()` to update the values from keys in a dictionary:
```python title="Input"
pet = {'species': 'Tub', 'age': 5, 'habitat': ['bathroom', 'kitchen']}
pet.update({'weight': 1000, 'name': 'Fluffy', 'age': 6})
print(pet)
```
```title="Output"
{'species': 'Tub', 'age': 6, 'habitat': ['bathroom', 'kitchen'], 'weight': 1000, 'name': 'Fluffy'}
```

While if we want to delete the key `'age'` and its value from the dictionary, we can use `del`:
```python title="Input"
pet = {'species': 'Tub', 'age': 5, 'habitat': ['bathroom', 'kitchen']}
del pet['age']
print(pet)
```
```title="Output"
{'species': 'Tub', 'habitat': ['bathroom', 'kitchen']}
```

Or use `pop()`: 
```python title="Input"
pet = {'species': 'Tub', 'age': 5, 'habitat': ['bathroom', 'kitchen']}
pet.pop('age')
print(pet)
```
```title="Output"
{'species': 'Tub', 'habitat': ['bathroom', 'kitchen']}
```

We can also assign the popped value to a variable:
```python title="Input"
popped_age = pet.pop('age')
print(pet)
print(popped_age)
```
```title="Output"
{'species': 'Tub', 'habitat': ['bathroom', 'kitchen']}
5
```
This can be useful if we want to use the popped value later.

As we mentioned in the previous sections, `len()` can also be used to check how many keys in a dictionary:
```python title="Input"
pet = {'species': 'Tub', 'age': 5, 'habitat': ['bathroom', 'kitchen']}
print(len(pet))
```
```title="Output"
3
```

### 2.6.4. Accessing Keys and Values
We can access all the keys from a dictionary using `keys()`:
```python title="Input"
pet = {'species': 'Tub', 'age': 5, 'habitat': ['bathroom', 'kitchen']}
print(pet.keys())
```
```title="Output"
dict_keys(['species', 'age', 'habitat'])
```

We can also access all the values from a dictionary using `values()`:
```python title="Input"
print(pet.values())
```
```title="Output"
dict_values(['Tub', 5, ['bathroom', 'kitchen']])
```

If we want to access the key-value pairs, we can use `items()`:
```python title="Input"
print(pet.items())
```
```title="Output"
dict_items([('species', 'Tub'), ('age', 5), ('habitat', ['bathroom', 'kitchen'])])
```
This is convenient if we want to loop through the key-value pairs.


## 2.7. Sets

Sets are unordered collections of unique elements and are useful when we want to store a collection of items that are not in any particular order and we don't want to store duplicate items.

### 2.7.1. Creating a Set
Create an empty set is similar to creating an empty list, you can use `set()`. Although the brackets `{}` are also used to create a set, it is actually creating an empty dictionary. To create an empty set, you need to use `set()`:
```python title="Input"
empty_dict = {} # This is to create an empty dictionary
empty_set = set() # This is to create an empty set
print(type(empty_dict))
print(empty_set)
print(type(empty_set))
```
```title="Output"
<class 'dict'>
set()
<class 'set'>
```

Create a set based on the same strings as the list `pet`:
```python title="Input"
pet = {'Tub', 'Furrytail', 'Cat', 'Barkalot'}
print(type(pet))
print(pet)
```
```title="Output"
<class 'set'>
{'Tub', 'Cat', 'Barkalot', 'Furrytail'}
```

!!! tip "`set` Doesn't Care About Order"
    Notice that the order of the elements in the set is different from the order of the elements in the list `pet`. This is because sets are unordered collections of unique elements. If you run it multiple times, the order will be different as sets don't care about the order of the elements.

### 2.7.2. Set Methods
If we create a set with duplicate elements, the set will only keep one copy of the element:
```python title="Input"
# Sets throw away the duplicate elements.
pet = {'Tub', 'Furrytail', 'Cat', 'Barkalot', 'Tub'}
print(pet)
```
```title="Output"
{'Tub', 'Cat', 'Barkalot', 'Furrytail'}
```

Sets are optimized for checking whether an element is contained in the set.
```python title="Input"
pet = {'Tub', 'Furrytail', 'Cat', 'Barkalot'}
print('Tub' in pet)
print('Tub' not in pet)
```
```title="Output"
True
False
```

We can check if two sets of pet in common using `intersection()`:
```python title="Input"
# What these pet have in common
pet_1 = {'Tub', 'Furrytail', 'Cat', 'Barkalot'}
pet_2 = {'Tub', 'Furrytail', 'Bumblefluff ', 'Whiskerfloof'}
print(pet_1.intersection(pet_2))
```
```title="Output"
{'Tub', 'Furrytail'}
```

We can also check if two sets of pet not in common using `difference()`:
```python title="Input"
# What these pet don't have in common
pet_1 = {'Tub', 'Furrytail', 'Cat', 'Barkalot'}
pet_2 = {'Tub', 'Furrytail', 'Bumblefluff ', 'Whiskerfloof'}
print(pet_1.difference(pet_2))
```
```title="Output"
{'Cat', 'Barkalot'}
```

Finally, we can also union both of the sets using `union()`:
```python title="Input"
# What these pet have in common and what they don't have in common
print(pet_1.union(pet_2))
```
```title="Output"
{'Tub', 'Cat', 'Barkalot', 'Furrytail', 'Bumblefluff ', 'Whiskerfloof'}
```



