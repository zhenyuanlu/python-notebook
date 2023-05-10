# 3. Control and Functions


## 3.1. Conditionals and Booleans

`if` statements are used to control the flow of the program. It allows us to execute a block of code if a certain condition is met.
`else` statements are used to execute a block of code if the condition is not met.
`elif` is to add more conditions to the `if` statement, which stands for `else if`.

### 3.1.1. `if` and Boolean Values
```python title="Input"
if True:
    print("It's true!")
```
```title="Output"
It's true!
```

What if we change the condition to `False`?
```python title="Input"
if False:
    print("It's true!")
```
```title="Output"
# Nothing will be printed
```
This is because that the condition is `False`, so the block of code is not executed.


In real practice, we don't hardcode the condition to be `True` or `False`, we basically assess the condition to be `True` or `False`

For example, we can use comparison operators to compare two values:
```python title="Input"
pet = 'Tub'
if pet == 'Tub':
    print("It's true!")
```
```title="Output"
It's true!
```

!!! info "Comparison Operators"
    Recall the operator we used in the previous chapter. This time, we use them in the condition, plus the identity operator `is`.

    - Equal: `==`
    - Not Equal: `!=`
    - Greater Than: `>`
    - Less Than: `<`
    - Greater or Equal: `>=`
    - Less or Equal: `<=`
    - Identity: `is`

### 3.1.2. `if`, `else`  and `elif`
Let's continue on the previous example. We campare `pet` and `Tub` to see if the pet is `Tub`

```python title="Input"
pet = 'Tub'
if pet == 'Tub':
    print("Pet is Tub!")
else:
    print("Pet is not Tub!")
```
```title="Output"
Pet is Tub!
```

If we change the value of `pet` to `Barkalot`, the condition is not met, so the `else` statement is executed.
```python title="Input"
pet = 'Barkalot'
if pet == 'Tub':
    print("Pet is Tub!")
else:
    print("Pet is not Tub!")
```
```title="Output"
Pet is not Tub!
```

We can also use `elif` to add more conditions to the `if` statement. Here we have two conditions, `pet == 'Tub'` and `pet == 'Barkalot'`. If the first condition is not met, we move on to the next condition. If the second condition is not met, we move on to the `else` statement:

```python title="Input"
pet = 'Barkalot'
if pet == 'Tub':
    print("Pet is Tub!")
elif pet == 'Barkalot':
    print("Pet is Barkalot!")
else:
    print("Pet is not Tub!")
```
```title="Output"
Pet is Barkalot!
```

### 3.1.3. `is` vs. `==`
Now, we investigate the difference between `is` and `==`:

- `is` checks if two variables point to the **same object in memory**.

- `==` checks if **the values** of two variables are equal.


Here, we have two list with the same values. 

```python title="Input"
pet_1 = ['Tub', 'Barkalot', 'Furrytail']
pet_2 = ['Tub', 'Barkalot', 'Furrytail']
```
We use `==` to compare them, and the result is `True`. 
```python title="Input"
print(pet_1 == pet_2)
```
```title="Output"
True
```
This is because that the values of the two lists are the same.

If we use `is` to compare them, the result is `False`.
```python title="Input"
print(pet_1 is pet_2)
```
```title="Output"
False
```
The reason is that `pet_1` and `pet_2` point to different objects in memory.

We can check out the memory address of the two objects using `id()`:
```python title="Input"
print(id(pet_1))
print(id(pet_2))
```
```title="Output"
2398480322752
2398482691520
```
You can see that the memory addresses are different.

But if we assign `pet_2` to `pet_1`, they will point to the same object in memory, and of course have the same values.
```python title="Input"
pet_2 = pet_1
print(pet_1 == pet_2)
print(pet_1 is pet_2)
```
```title="Output"
True
True
```
Now, the memory addresses are the same:

### 3.1.4. `and`, `or` and `not`

We can use `and` and `or` to combine conditions. 

- `and` means both conditions must be met

- `or` means at least one condition must be met

For example, we want to check if **both** the account name is `Tub` and the passcode is correct by using `and`:
```python title="Input"
account_name = 'Tub'
account_passcode = True

if account_name == 'Tub' and account_passcode:
    print("Login successful!")
else:
    print("Login failed!")
```
```title="Output"
Login successful!
```

If we want to know if at least one of the account name or account passcode is correct, we use `or`:
```python title="Input"
account_name = 'Tub'
account_passcode = True

if account_name == 'Tub' or account_passcode:
    print("Name or passcode is correct!")
else:
    print("Name and passcode are incorrect!")
```
```title="Output"
Name or passcode is correct!
```

If we want to negate a condition, we use `not`. 

- `not` means the condition must not be met
```python title="Input"
account_passcode = True
if not account_passcode:
    print("Please enter your passcode!")
else:
    print("Login successful!")
```
```title="Output"
Login successful!
```
Here, we use `not` to negate the condition `account_passcode == True` to `account_passcode == False`. 
Therefore, the condition must not be met, and the `else` statement is not executed. 

If we remove `not`, the condition must be met, which is `account_passcode == True`, and the `if` statement is executed. 
```python title="Input"
account_passcode = True
if account_passcode:
    print("Please enter your passcode!")
else:
    print("Login successful!")
```
```title="Output"
Please enter your passcode!
```


### 3.1.5. `in` and `not in`

We can use `in` to check if a value is in a list. 

- `in` means the value must be in the list

- `not in` means the value must not be in the list

Here is the example of `in`:
```python title="Input"
pets = ['Tub', 'Barkalot', 'Furrytail']
if 'Tub' in pets:
    print("Tub is in the list!")
else:
    print("Tub is not in the list!")
```
```title="Output"
Tub is in the list!
```

If we use `not in`, the condition is negated, and the `else` statement is executed:
```python title="Input"
pets = ['Tub', 'Barkalot', 'Furrytail']
if 'Tub' not in pets:
    print("Tub is not in the list!")
else:
    print("Tub is in the list!")
```
```title="Output"
Tub is in the list!
```

### 3.1.6. False Values

!!! info "False Values"
    In Python, the following values are considered as `False`:

    - `False`
    - `None`
    - `0` (any zero numeric types)
    - Empty sequence. e.g., `''`, `()`, `[]`.
    - Empty mapping. e.g., `{}`.


`False` is considered as False:
```python title="Input"
account_name = False
if account_name:
    print("Login successful!")
else:
    print("Please enter your account name!")
```
```title="Output"
Please enter your account name!
```

`None` is considered as False:
```python title="Input"
account_name = None
if account_name:
    print("Login successful!")
else:
    print("Please enter your account name!")
```
```title="Output"
Please enter your account name!
```

Only number `0` is considered as False:
```python title="Input"
account_name = 0
if account_name:
    print("Login successful!")
else:
    print("Please enter your account name!")
```
```title="Output"
Please enter your account name!
```

Empty sequences, e.g. `''`, `()`, `[]`, are considered as False:
```python title="Input"
account_name = ''
if account_name:
    print("Login successful!")
else:
    print("Please enter your account name!")
```
```title="Output"
Please enter your account name!
```


Empty dictionary is considered as False
```python title="Input"
account_name = {}
if account_name:
    print("Login successful!")
else:
    print("Please enter your account name!")
```
```title="Output"
Please enter your account name!
```




## 3.2. Functions

In this section, we will walk you through various examples related to functions in Python, exploring different concepts such as defining and calling functions, arguments, default values, and more.

### 3.2.1. Functions Basics


First, let's define a simple function called hello_tub:
```python title="Input"
def hello_tub():
    pass
print(hello_tub)
```

```title="Output"
<function hello_world at 0x000001E5F1F9B790>
```
This function does nothing, as it contains a pass statement. When you print the function, you will get the memory address of the function object:


```python title="Input"
print(hello_tub())
```

```title="Output"
None
```
Calling the function with `hello_tub()` returns None, as the function has no return statement.


Now, let's modify the hello_tub function to print a greeting:
```python title="Input"
def hello_tub():
    print('Hello Tub')
hello_tub()
```

```title="Output"
Hello Tub
```

Using functions is advantageous when you want to reuse code. For instance, if you want to change the greeting from `Tub` to `Barkalot`, you only need to modify the function's implementation, and all the calls to the function will use the updated greeting.

For example, if we want to call `Hello Tub` twice, we can do the following:
```python title="Input"
print('Hello Tub')
print('Hello Tub')
```
```title="Output"
Hello Tub
Hello Tub
```
But this is not convenient, as we have to repeat the same code twice. Instead, we can define a function and call it twice, and even if we want to change both `Tub`:

```python title="Input"
def hello_tub():
    print('Hello Barkalot')
hello_tub()
hello_tub()
```
```title="Output"
Hello Barkalot
Hello Barkalot
```

Functions can also return values, take parameters, and have default values for parameters. Here are some examples:

```python title="Input"
def hello_tub():
    return 'Hello Tub'
print(hello_tub())
```
```title="Output"
Hello Tub
```

We can also call the function with a method, e.g. `lower()`, to convert the returned value to lowercase:

```python title="Input"
print(hello_tub().lower())
```
```title="Output"
hello tub
```


Functions can also return values, take parameters, and have default values for parameters. Here are some examples:

```python title="Input"
def hello_tub(name):
    return 'Hello ' + name
print(hello_tub('Tub'))
```
```title="Output"
Hello Tub
```

```python title="Input"
def hello_tub(name):
    return 'Hello {}'.format(name)
print(hello_tub('Tub'))
```
```title="Output"
Hello Tub
```

We set up a default value for the name parameter, so that if we don't pass a value for name, the function will use the default value:
```python title="Input"
def hello_tub(greeting, name = 'Tub'):
    return '{}, {}'.format(greeting, name)
print(hello_tub('Hello'))
```
```title="Output"
Hello, Tub
```

When we pass a value for name, the default value is ignored:
```python title="Input"
print(hello_tub('Hello', 'Barkalot'))
```
```title="Output"
Hello, Barkalot
```


### 3.2.2. Positional Arguments

In Python, non-default arguments (those without default values) must be defined before default arguments (those with default values). In the given code, the greeting parameter has a default value, while name does not. This causes a SyntaxError.


```python title="Input"
def hello_tub(greeting = 'Hello', name):
    return '{}, {}'.format(greeting, name)
```
```title="Output"
SyntaxError: non-default argument follows default argument
```

To fix this issue, you should move the non-default argument before the default argument:

```python title="Input"
def hello_tub(name, greeting='Hello'):
    return '{}, {}'.format(greeting, name)
```
Now, the function works as expected, and you can call it with or without providing a greeting argument:

```python title="Input"
print(hello_tub('Tub'))
print(hello_tub('Tub', 'Hi'))
```
```title="Output"
Hello, Tub
Hi, Tub
```


Below let's go through a real example how to find the number of days in a month
!!! note "Example - Find the number of days in a month"
    Credits: [Python Standard Library](https://docs.python.org/3/library/index.html), and Corey Schafer.

    Number of days per month. First value placeholder for indexing purposes.

    ```python title="month_days"
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ```
    The `is_leap()` function takes a year as input and returns True if it's a leap year, and False otherwise. Leap years are those divisible by 4, but not divisible by 100, unless they are also divisible by 400.

    ```python title="is_leap()"
    def is_leap(year):
        """
        Return True for leap years, False for non-leap years.
        """
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    ```
    The `days_in_month()` function takes a year and a month as input and returns the number of days in that month for that year. It checks if the input year is a leap year and adjusts the number of days in February accordingly. If an invalid month is provided, it returns `Invalid Month`.

    ```python title="days_in_month()"
    def days_in_month(year, month):
        """
        Return number of days in that month in that year.
        """
        if not 1 <= month <= 12:
            return 'Invalid Month'

        if month == 2 and is_leap(year):
            return 29

        return month_days[month]
    ```
    Finally, the code demonstrates calling the `is_leap()` and `days_in_month()` functions with specific inputs:

    ```python title="Print"
    print(is_leap(2023))
    print(days_in_month(2023, 4))
    ```
    ```title="Output"
    False
    30
    ```


### 3.2.3. `*args` and `**kwargs`

In the following code, there are several concepts being illustrated: `*args`, `**kwargs`, and two custom functions `is_leap()` and `days_in_month()`.

`*args` and `**kwargs` are used in function definitions to allow passing a variable number of arguments. `*args` is used for passing a variable number of non-keyword (positional) arguments, while `**kwargs` is used for passing a variable number of keyword arguments.



```python title="Input"
def pet_info(*args, **kwargs):
    print(args)
    print(kwargs)
pet_info('Tub', 'Barkalot', 'Furrytail', pet1 = 'Tub', pet2 = 'Barkalot', pet3 = 'Furrytail')
```
```title="Output"
('Tub', 'Barkalot', 'Furrytail')
{'pet1': 'Tub', 'pet2': 'Barkalot', 'pet3': 'Furrytail'}
```
In the `pet_info()` function, both `*args` and `**kwargs` are used. When you call the function with different types of arguments, you can see how they are grouped and printed:


```python title="Input"
def pet_info(*args, **kwargs):
    print(args)
    print(kwargs)

favorite_food = ['Carrot', 'Brocolli', 'Ice Cream']
info = {'name': 'Tub', 'age': 25}
pet_info(favorite_food, info)
```
In the first call to pet_info, we pass a list `favorite_food` and a dictionary info as arguments without using the `*` or `**` unpacking operators. This means the entire list and dictionary are treated as single positional arguments. The output shows that args contains a tuple with two elements: the list `favorite_food` and the dictionary info. Since we didn't provide any keyword arguments, kwargs is an empty dictionary.

```title="Output"
(['Carrot', 'Brocolli', 'Ice Cream'], {'name': 'Tub', 'age': 25})
{}
```

In the second call to pet_info, we use the `*` and `**` unpacking operators to pass the list favorite_food and the dictionary info as individual elements. The `*` operator unpacks the list elements as positional arguments, and the `**` operator unpacks the dictionary items as keyword arguments. In this case, the output shows that args contains a tuple with three elements ('`Carrot`', '`Brocolli`', '`Ice Cream`') and kwargs contains a dictionary with the keys and values from the info dictionary.

```python title="Input"
pet_info(*favorite_food, **info)
```
```title="Output"
('Carrot', 'Brocolli', 'Ice Cream')
{'name': 'Tub', 'age': 25}
```


### 3.2.3. Variable Scope - LEGB rule


In this section, we are discussing variable scope in Python, which determines where a variable can be accessed or modified. Python searches for a variable following the LEBG rule and order: Local, Enclosing, Global, and Built-in.


**Local**
A variable defined within a function has local scope. It can only be accessed inside that function.

```python title="Input"
def test():
    y = 'local variable y'
    print(y)

test()
```
```title="Output"
local variable y
```

**Global**

A variable defined outside any function has global scope. It can be accessed both inside and outside of functions.

In the following example, we define a variable `x` outside of the `test()` function. We can access and modify this variable inside the function. 

```python title="Input"
x = 'global variable x'

def test():
    y = 'local variable y'
    print(x)

test()
print(x)
```
```title="Output"
global variable x
global variable x
```
Here the results are the same because we are accessing the global variable `x` inside the function. However, if we try to access the local variable `y` outside of the function, we get an error.

```python title="Input"
print(y)
```
```title="Output"
NameError: name 'y' is not defined
```

What if we have a variable with the same name inside and outside of a function? In this case, the local variable takes precedence over the global variable. The following example demonstrates this:

```python title="Input"
x = 'global variable x'
def test():
    x = 'local variable x'
    print(x)

test()
print(x)
```
```title="Output"
local variable x
global variable x
```
This example shows that the python searches for a variable in the local scope first. If it doesn't find it, it searches the global scope. This is the reason that we get the local variable `x` inside the function first and the global variable `x` next

If it doesn't find it there, it will throw an error. 

In the next example, we demonstrate how to use the global keyword to change the value of a global variable within a function. 

```python title="Input"
# What if we want to set a new global x
x = 'global variable x'
def test():
    global x
    x = 'local variable x'
    print(x)

test()
print(x)
```
```title="Output"
local variable x
local variable x
```

In this example, we use the `global` keyword to change the value of the global variable `x` inside the function, although this is not recommended in the practice because it can lead to unexpected behavior and make the code difficult to debug and review. 

You can also do the following:

```python title="Input"
def test():
    global x
    x = 'local variable x'
    print(x)

test()
print(x)
```
```title="Output"
local variable x
local variable x
```

However, it is not recommended to use global often.

```python title="Input"
def test(z):
    print(z)

test('local variable z')
print(z)
```
```title="Output"
local variable z
NameError: name 'z' is not defined
```

**Built-in**

In this example, we are discussing the built-in scope in Python. Built-in scope refers to the predefined functions and variables available in Python, which are part of the standard library.

Python has a set of built-in functions, like min(), max(), print(), etc., which are readily available for use.

```python title="Input"
# Built-in
import builtins
# print(dir(builtins))

minimum = min([1,2,3])
print(minimum)
```
```title="Output"
1
```

However, you should avoid overwriting built-in functions with your own functions or variables. Doing so can lead to errors or unintended behavior.

```python title="Input"
# If we overwrite the built-in function min()
def min():
    pass

m = min([1,2,3])
print(m)
```
```title="Output"
TypeError: min() takes 0 positional arguments but 1 was given
```

To avoid conflicts with built-in functions, it's a good practice to use different names for your own functions. 

So the best way to do this is to use a different name instead of the default name `min()`.

```python title="Input"
def find_min():
    pass

minimum = min([1,2,3])
print(minimum)
```
```title="Output"
1
```

Being mindful of built-in functions and avoiding name conflicts will help you write clean, error-free code.

**Enclosing**


In this example, we discuss the concept of enclosing scope in Python. Enclosing scope is the scope of variables that are defined in an outer function but not in the global scope. Enclosing scope variables are accessible from the inner function.

Let's look at an example:

```python title="Input"
x = 'global variable x'
def outer():
    x = 'local-outer variable x'

    def inner():
        x = 'local-inner variable x'
        print(x) # 1st print

    inner() # 1st call for 1st print
    print(x) # 2nd print


outer() # 2nd call for 1st print and 2nd print
print(x) # 3rd print
```
```title="Output"
local-inner variable x
local-outer variable x
global variable x
```

The `outer()` function has its own local variable `x`, and the `inner()` function also has its own local variable x. When we call the functions, the inner function prints its local variable `x`, the outer function prints its local variable `x`, and then the global variable x is printed.


Now let's use the nonlocal keyword to modify the enclosing variable from the inner function:

```python title="Input"
x = 'global variable x'
def outer():
    x = 'local-outer variable x'

    def inner():
        nonlocal x # Make our local-inner variable x to be the enclosing variable x
        x = 'local-inner variable x'
        print(x)

    inner()
    print(x)

outer()
print(x)
```
```title="Output"
local-inner variable x
local-inner variable x
global variable x
```

In this case, we use the nonlocal keyword inside the `inner()` function to indicate that we want to modify the enclosing variable `x` (the one defined in the `outer()` function) instead of creating a new local variable. When the functions are called, both the inner and outer functions print the modified enclosing variable `x`, and then the global variable `x` is printed.