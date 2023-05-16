# 5. Loops and Comprehensions

## 5.1. Loops
This chapter provides an overview of loops and iterations in Python, specifically focusing on the `for`, `while`, and `else` statements.

### 5.1.1. For Loops

- Basic Usage: The for loop iterates over a list of pets and prints each pet's name. This is the simplest usage of a for loop.
- `break` Statement: The for loop is used in combination with a conditional statement and break, which terminates the loop once a specific condition is met. In this case, the loop is terminated when the pet name is `Barkalot`.
- `continue` Statement: The continue statement is used to skip the rest of the current loop iteration and immediately start the next one. Here, when the pet name is `Barkalot`, the loop prints a special message and then immediately starts the next iteration, skipping the usual print statement.
- Nested for Loops: This demonstrates the concept of nested loops, where a for loop is contained within another for loop. The outer loop iterates over the pet names, and the inner loop iterates over the letters `a` and `b` or the numbers `0` and `1`.
- `range()` Function: The `range()` function generates a sequence of numbers over which the for loop iterates. The function can be called with different numbers of arguments to change the start, end, and step size of the sequence.

This chapter provides an excellent foundation for understanding loops in Python. The various concepts and techniques it introduces are fundamental to many kinds of programming tasks.


**Basic Usage**

```python title="Input"
pets = ['Tub', 'Barkalot', 'Furrytail']
for pet in pets:
    print(pet)
```
```python title="Output"
Tub
Barkalot
Furrytail
```
This code creates a list of pet names, then uses a `for` loop to iterate over each item in the list. Each time through the loop, it prints the current pet name.


**`break` Statement**

```python title="Input"
pets = ['Tub', 'Barkalot', 'Furrytail']
for pet in pets:
    if pet == 'Barkalot':
        print('We got Barkalot!')
        break
    print(pet)
```
```python title="Output"
Tub
We got Barkalot!
```
This code is similar to the previous example, but it includes an `if` statement that checks whether the current pet name is `Barkalot`. If it is, the code prints a special message and then uses the `break` statement to immediately exit the loop.


**`continue` Statement**

```python title="Input"
# `continue` statement skip the current iteration and continue with the next.
# Here we skip the `Barkalot` pet and print `We got Barkalot!` instead.
pets = ['Tub', 'Barkalot', 'Furrytail']
for pet in pets:
    if pet == 'Barkalot':
        print('We got Barkalot!')
        continue
    print(pet)
```
```python title="Output"
Tub
We got Barkalot!
Furrytail
```

Again, this code is similar to the previous examples. The difference is that when the current pet name is `Barkalot`, it uses the `continue` statement to immediately start the next iteration of the loop, skipping the `print(pet)` statement for `Barkalot`.

**Nested for Loops**

```python title="Input"
for pet in pets:
    for letter in 'ab':
        print(letter, pet)
```
```python title="Output"
a Tub
b Tub
a Barkalot
b Barkalot
a Furrytail
b Furrytail
```
Here, the outer `for` loop iterates over the list of pet names, and the inner `for` loop iterates over the string 'ab'. For each combination of pet name and letter, it prints the letter and the pet name.


**`range()` Function**

```python title="Input"
for pet in pets:
    for num in range(2):
        print(num, pet)
```
```python title="Output"
0 Tub
1 Tub
0 Barkalot
1 Barkalot
0 Furrytail
1 Furrytail
```

This code is the same as the previous example, but the inner loop iterates over the numbers produced by `range(2)`, which are 0 and 1.

**`range()` Function with Start and End**

```python title="Input"
for num in range(0, 5):
    print(num)
```
```python title="Output"
0
1
2
3
4
```

This code uses the `range()` function to generate a sequence of numbers from 0 to 4. The `for` loop iterates over these numbers, printing each one.

**`range()` Function with Start, End, and Step**

```python title="Input"
for num in range(0, 5, 2):
    print(num)
```
```python title="Output"
0
2
4
```

This code is similar to the previous example, but it adds a step size of 2 to the `range()` function. This means it only generates every second number in the range from 0 to 4, so the `for` loop prints the numbers 0, 2, and 4.


### 5.1.2. While Loops
In Python, a `while` loop repeatedly executes a target statement as long as a given condition is true.

For example:
```python title="Input"
num = 1
while num < 5:
    print(num)
    num += 1
```
```python title="Output"
1
2
3
4
```

The `while` loop above continues executing until the condition `num < 5` is no longer true, which occurs after the fourth iteration.

**Using `break` with While Loop**

The `break` statement is used to exit a `while` loop prematurely. When a `break` statement is encountered inside the loop, the loop is immediately terminated, and program control resumes at the next statement following the loop.

In the following code, `break` is triggered when `num` equals 3, causing an early exit from the loop.

```python title="Input"
num = 1
while num < 5:
    if num == 3:
        break
    print(num)
    num += 1
```
```python title="Output"
1
2
```

**`break` in an Infinite Loop**

An infinite `while` loop can be created using `while True:`. This loop will run indefinitely unless it encounters a `break` statement.

`break` is used to stop an otherwise infinite loop when num equals 3:

```python title="Input"
num = 1
while True:
    if num == 3:
        break
    print(num)
    num += 1
```
```python title="Output"
1
2
```

**If Statement versus While Loop**

An `if` statement checks a condition once, whereas a `while` loop continues to execute the block of code as long as the condition is true.

```python title="Input"
num = 1
if num < 5:
    print(num)
    num += 1
```
```python title="Output"
1
```

In this code, the `if` statement checks the condition `num < 5` once and then executes the block of code if the condition is true. After that, it doesn't check the condition again or repeat the block of code. This is the main difference between a `while` loop and an `if` statement.



### 5.1.3. Else Clause with Loops

The `else` clause in Python can also be used with loops. Unlike in an `if` statement, where `else` executes when the `if` condition is false, with loops, the else clause executes after the loop completes normally, i.e., when no `break` statement has been encountered.

**If-Else**

The else clause executes after the loop completes normally.

Here's a simple example of an `if-else` statement:

```python title="Input"
tub_age = 5

if tub_age > 18:
    print('Tub is an adult.')
else:
    print('Tub is a child.')
```
```python title="Output"
Tub is a child.
```

The `else` clause is executed because the `if` condition is false.

**Else with For Loop**

In the context of a `loop`, an else statement can be thought of as a "no break" statement. It will execute once the loop has finished iterating over the items.

Another example may not be so obvious. And always makes people confused:

```python title="Input"
pets = ['Tub', 'Barkalot', 'Furrytail']

for pet in pets:
    print(pet)
else: # More like a `no break` statement
    print('No more pets.')
```
```python title="Output"
Tub
Barkalot
Furrytail
No more pets.
```

The `else` statement associated with a loop (either a `for` or `while` loop) in Python might initially seem confusing since in many other programming languages `else` is associated only with `if` statements.


**You may think why the `else` statement is executed?**

In Python, the `else` clause in a loop executes when the loop has finished iterating over all items (in a `for` loop) or when the condition becomes false (in a `while` loop), but not when the loop is prematurely ended by a `break` statement.

Let's break down the above example:

 - The `for` loop begins iterating over the `pets` list. For each pet in `pets`, it prints the pet's name.

 - When there are no more items left in the `pets` list, the loop's condition becomes false (it has run out of items to process). At this point, instead of just ending, it checks if there is an `else` clause associated with it.

 - Since there is an `else` clause, it runs the code inside the `else` block. The print statement inside the `else` block runs, outputting `No more pets.`.


So, the phrase `no break` used in comments beside the `else` statement means that if the loop finishes its iterations normally without encountering a `break` statement (i.e., it was not forced to stop prematurely), the code inside the else block will be executed.

This behavior is particularly useful when you use a loop to search for an item in a list or another data structure. If the item is found, you can use the `break` statement to stop the loop, and the `else` block will be ignored. If the item isn't found and the loop ends normally after checking all items, the `else` block will run, allowing you to handle the case where the item isn't found.

To understand this, let's have a more concrete example:


**In `for` loops**
=== "`else` terminated by `break`"
    ```python title="Input"
    for pet in pets:
        print(pet)
        if pet == 'Barkalot':
            break
    else:
        print('No more pets.')
    ```
    ```python title="Output"
    Tub
    Barkalot
    ```
    The `else` statement is not executed because the loop is terminated by the `break` statement.

=== "`else` not terminated by `break` and plays as `no break`"
    ```python title="Input"
    for pet in pets:
        print(pet)
        # Now the loop is not terminated by the `break` statement
        # as the condition is never met  as the above example.
        # You can remove the `if` statement, and it will still work.
        if pet == 'NOT EXIST':
            break
    else: # More like a `no break` statement.
        print('No more pets.')
    ```
    ```python title="Output"
    Tub
    Barkalot
    Furrytail
    No more pets.
    ```



**This is also the same as for `while` loop.**

=== "`else` within `while` loop and terminated by `break`"
    ```python title="Input"
    age = 7
    while age >=5:
        print(age)
        age -= 1
    else: # More like a `no break` statement
        print('End')
    ```
    ```python title="Output"
    7
    6
    5
    End
    ```
    The `else` statement is not executed because the loop is terminated by the `break` statement.

=== "`else` within `while` loop and plays as `no break`"
    ```python title="Input"
    age = 7
    while age >=5:
        print(age)
        age -= 1
        if age == 6:
            break
    else: # More like a `no break` statement
        print('End')
    ```
    ```python title="Output"
    7
    6
    ```


In this exercise, you'll create a function that searches for a specific number in a list using a for `loop` and an `else` clause. The function should print a message indicating whether or not the number was found in the list.

!!! tip "Exercise 1: Search Number in List"


    Tasks:

    1. Write a function `search_number_in_list` that takes two parameters: a list of numbers (`numbers_list`) and a number to search (`search_number`).

    1. Inside the function, start a `for` loop that iterates over each number in `numbers_list`.

    1. Inside the loop, use an `if` statement to check if the current number equals `search_number`. If it does, print a message like `Number {`search_number`} found in the list!`, and then use the `break` statement to immediately exit the loop.

    1. After the `for` loop, write an `else` clause that prints a message like `Number {search_number} not found in the list.`. This `else` clause should be executed if the `for` loop completes all its iterations without hitting the `break` statement.

    1. Test your function with a list of numbers and a search number of your choice.

    Here's a skeleton of the function to get you started:

    === "Skeleton to started"

        ```python title="Skeleton"
        def search_number_in_list(numbers_list, search_number)-->str:
        # Your code here
        pass

        # Test the function
        numbers = [1, 3, 5, 7, 9, 11]
        search_number = 7
        search_number_in_list(numbers, search_number)
        ```

        ```python title="Expected Ouput"
        Number 7 found in the list!
        ```
        Or if you search for a number not in the list:

        ```python title="Expected Ouput"
        Number {search_number} not found in the list.
        ```


    === "Solution"

        ```python title="Solution"
        numbers = [1, 3, 5, 7, 9, 11]
        search_number = 7

        for num in numbers:
            if num == search_number:
                print(f'Number {search_number} found in the list!')
                break
        else:
            print(f'Number {search_number} not found in the list.')
        ```

In this exercise, you'll modify the function `find_first_even` to return the index of the first even number found in the list. If no even number is found, the function should return `None`.

!!! tip "Exercise 2: Find First Even Number Function"

    Tasks:

    1. Modify the function `find_first_even` that takes a list of numbers (`nums`) as parameter.

    2. Inside the function, start a `for` loop that iterates over number/s in `nums`.

    3. Inside the loop, use an `if` statement to check if the current number is even. If it is, return the current `num` and then use the `break` statement to immediately exit the loop.

    4. After the `for` loop, write an `else` clause that returns `None`. This `else` clause should be executed if the `for` loop iterates over all the numbers from the list without hitting the `break` statement. In other words, we didn't find any even number in the list.

    5. Test your function with a list of numbers of your choice.

    Here's a skeleton of the function to get you started:

    === "Skeleton to started"

        ```python title="Skeleton"
        def find_first_even(nums)-->str:
            # Your code here
            pass

        # Test the function
        nums = [1, 3, 5, 7, 9, 11]
        # It should print `First even number is: 8`
        print('First even number is: {}'.format(first_even))  
        nums = [1, 3, 5, 2, 9, 11]
        # It should print `First even number is: None`
        print('First even number is: {}'.format(first_even))  
        ```

        ```python title="Expected Ouput"
        First even number is: 8
        First even number is: None
        ```


    === "Solution"

        ```python title="Solution"
        def find_first_even(nums)->str:
            for num in nums:
                if num % 2 == 0:
                    break
            else:
                num = 'None'
            return num
        ```


## 5.2. `enumerate()` function

The `enumerate` function is a built-in function in Python that allows you to loop over something and have an automatic counter, or index tracker. It adds a counter as the key of the enumerate object, alongside the items of the iterable, returning an enumerate object which you can convert to a list, tuple or other data structures. The function signature is as follows:

`enumerate(iterable, start=0)`

- `iterable`: any object that supports iteration
- `start`: the index value from which the counter should start, default is 0

### 5.2.1. Basic Usage of enumerate()

```python title="Input"
pets = ['Tub', 'Barkalot', 'Furrytail']
for i, pet in enumerate(pets):
    print(i, pet)
```
```python title="Output"
0 Tub
1 Barkalot
2 Furrytail
```
Here, `enumerate(pets)` returns a sequence of tuples, and each tuple consists of two items: the index and the value of the corresponding item in the iterable. `i` and `pet` are tuple unpacking the result returned by enumerate.



### 5.2.2. Using enumerate with a Different Start Index

In this example, the index starts at `1` (instead of the default 0) because we've set `start=1`.

```python title="Input"
pets = ['Tub', 'Barkalot', 'Furrytail']
for i, pet in enumerate(pets, start=1):
    print(i, pet)
```
```python title="Output"
1 Tub
2 Barkalot
3 Furrytail
```


### 5.2.3. Practical Usage of enumerate

`enumerate` is particularly useful when you need to track the index of items within a loop. For example, if you want to replace an item in a list:

```python title="Input"
pets = ['Tub', 'Barkalot', 'Furrytail']
for i, pet in enumerate(pets):
    if pet == 'Tub':
        pets[i] = 'Cat'
print(pets)
```
```python title="Output"
['Cat', 'Barkalot', 'Furrytail']
```
In the above code, we use `enumerate` to get the index of each pet. When we find the pet `Tub`, we use the index to replace `Tub` with `Cat` in the original list.

Now it's time to try using `enumerate` in your own code! Try to think of situations where you need both the item and its index within a loop. 

!!! tip "Exercise: Find First Even Number and Its Index"

    Tasks:

    1. Modify the function `find_first_even` that takes a list of numbers (`nums`) as parameter.

    2. Inside the function, start a `for` loop that iterates over each number in `nums`. You'll need to use the `enumerate` function so that you have access to the index of each number.

    3. Inside the loop, use an `if` statement to check if the current number is even. If it is, return the current index and number as a `tuple(index, number)`, and then use the `break` statement to immediately exit the loop.

    4. After the `for` loop, write an `else` clause that returns `(None, None)`. This `else` clause should be executed if the `for` loop completes all its iterations without hitting the `break` statement.

    5. Test your function with a list of numbers of your choice.

    Here's a skeleton of the function to get you started:

    === "Skeleton to started"

        ```python title="Skeleton"
        def find_first_even(nums)->tuple(int, int):
            # Your code here
            return (i, num)

        nums = [1, 3, 8, 7, 3, 2, 3]
        first_even = find_first_even(nums)
        print('The index and value of the first even number are: {}'.format(first_even))
        # Output: The index and value of the first even number are: (2, 8)

        nums = [1, 3, 1, 7, 3, 9, 3]
        first_even = find_first_even(nums)
        print('The index and value of the first even number are: {}'.format(first_even))
        # Output: The index and value of the first even number are: ('None', 'None')
        ```

        ```python title="Expected Ouput"
        The index and value of the first even number are: (2, 8)
        The index and value of the first even number are: ('None', 'None')
        ```


    === "Solution"

        ```python title="Solution"
        def find_first_even(nums)->tuple(int, int):
            for i, num in enumerate(nums):
                if num % 2 == 0:
                    break
            else:
                return ('None', 'None')
            return (i, num)
        ```



## 5.3. List Comprehensions

List comprehensions are a powerful feature in Python, allowing you to create lists from existing lists or other iterable objects. They provide a concise way to apply operations to the values in a sequence.


### 5.3.1. Basic List Comprehensions


Consider the following example where we have a list of ages, and we want to create a new list with the same ages:

**Using For loop**

```python title="Input"
ages = [5, 12, 3, 56, 24, 78, 1, 15, 44]
age_list = []
for age in ages:
    age_list.append(age)
print(age_list)
```
```python title="Output"
[5, 12, 3, 56, 24, 78, 1, 15, 44]
```

Now, we make the above for loop into a list comprehension

```python title="Input"
# [item for item in iterable]
age_list = [age for age in ages]
print(age_list)
```
```python title="Output"
[5, 12, 3, 56, 24, 78, 1, 15, 44]
```

Another example, we also apply operations to the values in the sequence. For example, we can add 1 to each age:

**Using For loop**

```python title="Input"
ages = [5, 12, 3, 56, 24, 78, 1, 15, 44]
age_list = []
for age in ages:
    age_list.append(age + 1)
print(age_list)
```
```python title="Output"
[6, 13, 4, 57, 25, 79, 2, 16, 45]
```

**List comprehension**

```python title="Input"
# [expression for item in iterable]
age_list = [age + 1 for age in ages]
print(age_list)
```
```python title="Output"
[6, 13, 4, 57, 25, 79, 2, 16, 45]
```

### 5.3.2. Comparing List Comprehensions and `map`

`map()` is a built-in function that applies a function to each item in an iterable object. It returns a map object, which can be converted into a list or tuple. 

Let's see how we can use `map` to add 1 to each age as the previous example:

```python title="Input"
age_list = list(map(lambda age: age + 1, ages))
print(age_list)
```
```python title="Output"
[6, 13, 4, 57, 25, 79, 2, 16, 45]
```

`map` is faster than list comprehension, but list comprehension is more readable.


### 5.3.3. List Comprehensions with Conditionals

You can also include conditions in your list comprehension. For example, we can create a list that only contains even ages:

**Using For loop**

```python title="Input"
ages = [5, 12, 3, 56, 24, 78, 1, 15, 44]
age_list = []
for age in ages:
    if age % 2 == 0:
        age_list.append(age)
print(age_list)
```
```python title="Output"
[12, 56, 24, 78, 44]
```

**List comprehension**

```python title="Input"
# [expression for item in iterable if condition]
age_list = [age for age in ages if age % 2 == 0]
print(age_list)
```
```python title="Output"
[12, 56, 24, 78, 44]
```

**Using `lambda` with `filter`**


```python title="Input"
# filter(lambda)
age_list = list(filter(lambda age: age % 2 == 0, ages))
print(age_list)
```
```python title="Output"
[12, 56, 24, 78, 44]
```



### 5.3.4. Real World Example

List comprehensions can be used to solve real-world problems more concisely. For example, let's say you want to create an unordered HTML list from a list of pet names:


**Using For loop**

```python title="Input"
pets = ['Tub', 'Furrytail', 'Cat', 'Barkalot', 'Bumblefluff ', 'Whiskerfloof']
output = '<ul>\n'
for pet in pets:
    output += '\t<li>{}</li>\n'.format(pet)
    # print('Address of output is {}'.format(id(output)))
output += '</ul>'
print(output)
```
```python title="Output"
<ul>
<li>Tub</li>
<li>Furrytail</li>
<li>Cat</li>
<li>Barkalot</li>
<li>Bumblefluff </li>
<li>Whiskerfloof</li>
</ul>
```

- Tub
- Furrytail
- Cat
- Barkalot
- Bumblefluff
- Whiskerfloof


**List comprehension**

```python title="Input"
pets = ['Tub', 'Furrytail', 'Cat', 'Barkalot', 'Bumblefluff ', 'Whiskerfloof']
output = '<ul>\n'
# List comprehension to create a list of formatted list items
formatted_pet_names = ['\t<li>{}</li>'.format(pet) for pet in pets]
# Join the list items with newline characters and add the closing </ul> tag
output += '\n'.join(formatted_pet_names) + '\n</ul>'
print(output)
```
```python title="Output"
<ul>
<li>Tub</li>
<li>Furrytail</li>
<li>Cat</li>
<li>Barkalot</li>
<li>Bumblefluff </li>
<li>Whiskerfloof</li>
</ul>
```

### 5.3.5. Performance Comparison: For Loop vs List Comprehension

Let's compare the performance of using a `for` loop vs a list comprehension to generate a list of formatted numbers:

```python title="Input"
import timeit
import random

# Create a list of 10,000 random numbers between 0 and 100
nums = [random.randint(0, 100) for i in range(10000)]

# For loop implementation
def for_loop():
    output = '<ul>\n'
    for num in nums:
        output += '\t<li>{}</li>\n'.format(num)
    output += '</ul>'
    return output

# List comprehension implementation
def list_comprehension():
    output = '<ul>\n' + ''.join(['\t<li>{}</li>\n'.format(num) for num in nums]) + '</ul>'
    return output

# Measure the execution time of both implementations
for_loop_time = timeit.timeit(for_loop, number=1000)
list_comprehension_time = timeit.timeit(list_comprehension, number=1000)

print("For loop execution time: ", for_loop_time)
print("List comprehension execution time: ", list_comprehension_time)
```
```python title="Output"
For loop execution time:  0.01699999999999999
List comprehension execution time:  0.012999999999999956
```

When running this code, you'll find that the list comprehension implementation is typically faster than the `for` loop implementation. This is because list comprehensions are optimized for performance in Python, and they can often perform the same task more quickly than the equivalent `for` loop. However, the difference in speed may not be significant unless you're dealing with very large data sets.

It's also worth noting that while list comprehensions can be faster and more concise, they can also be harder to read if they become too complex. Therefore, it's important to strike a balance between performance and readability when writing your code.

=== "Pros of List Comprehensions vs For Loops"
    - **Succinctness**: List comprehensions provide a concise way to create lists. They can often achieve the same result as a for-loop in a single, short line of code.

    - **Speed**: List comprehensions are generally faster than for-loops because they are specifically optimized for creating new lists.

    - **Functionality**: List comprehensions can incorporate conditionals and multiple for-loops, enabling quite complex list creation in a single line.

=== "Cons of List Comprehensions Vs For Loops"
    - **Readability**: List comprehensions can be harder to read than for-loops, especially if they are complex.

    - **MemoryUsage**: List comprehensions create new lists in memory, which can cause problems if you're working with very large data sets.

    - **Debugging**: List comprehensions can be harder to debug than for-loops, especially if they are complex.


## 5.4. zip() Function 


In Python, the `zip()` function is used to combine corresponding elements from multiple iterables (like lists or tuples) into tuples. Let's first understand it with an example:

```python title="Input"
ages = [5, 12, 3, 56, 24, 78, 1, 15, 44]
names = ['Tub', 'Barkalot', 'Furrytail']

print(zip(ages, names))
print(list(zip(ages, names)))
```
```python title="Output"
<zip object at 0x0000020F6F6F0A48>
[(5, 'Tub'), (12, 'Barkalot'), (3, 'Furrytail')]
```
What zip does is it takes the first item from each iterable and puts them together in a tuple then it takes the second item from each iterable and puts them together in a tuple and so on. The result is a zip object that we can convert into a list of tuples using the `list()` function.

### 5.4.1. zip() with for Loop

In the following example, the `zip()` function pairs up the elements from ages and names lists by their indices.

```python title="Input"
ages = [5, 12, 3, 56, 24, 78, 1, 15, 44]
names = ['Tub', 'Barkalot', 'Furrytail']

my_list = []
for age in range(3):
    for name in names:
        my_list.append((age, name))
print(my_list)
```
```python title="Output"
[(0, 'Tub'), (0, 'Barkalot'), (0, 'Furrytail'), (1, 'Tub'), (1, 'Barkalot'), (1, 'Furrytail'), (2, 'Tub'), (2, 'Barkalot'), (2, 'Furrytail')]
```
We can utilize this function along with comprehensions for more complex operations.

### 5.4.2. zip() with List Comprehension

Similarly, we can use` zip()` with list comprehensions. Let's create a list of tuples where each tuple consists of a number and a pet name:

```python title="Input"
my_list = [(age, name) for age in range(3) for name in names]
print(my_list)
```
```python title="Output"
[(0, 'Tub'), (0, 'Barkalot'), (0, 'Furrytail'), (1, 'Tub'), 
(1, 'Barkalot'), (1, 'Furrytail'), (2, 'Tub'), (2, 'Barkalot'), (2, 'Furrytail')]
```

This code creates a tuple for each combination of age and name, and adds it to the list. Here, `age` ranges from `0` to `2`, and `name` is taken from the `names` list.

## 5.5. Dictionary Comprehensions

A dictionary comprehension is similar to a list comprehension, but it constructs a dictionary instead of a list.

If we want to create a dictionary that maps each pet's name to its age, we can use a for-loop like this:


**Regular For Loop with zip()**

```python title="Input"
my_dict = {}
for age, name in zip(ages, names):
    my_dict[name] = age
print(my_dict)
```
```python title="Output"
{'Tub': 5, 'Barkalot': 12, 'Furrytail': 3}
```

**Dictionary comprehension with zip()**

```python title="Input"
# {key: value for item in iterable}
my_dict = {name: age for name, age in zip(names, ages)}
print(my_dict)
```
```python title="Output"
{'Tub': 5, 'Barkalot': 12, 'Furrytail': 3}
```
Here, `name`: `age` is the key-value pair for each item in the dictionary.


We can also add a condition in the dictionary comprehension to filter the items:

```python title="Input"
# {key: value for item in iterable if condition}
my_dict = {name: age for name, age in zip(names, ages) if age > 10}
print(my_dict)
```
```python title="Output"
{'Barkalot': 12}
```

This will include only the pets that are older than 10 in the dictionary.


## 5.6. Set Comprehensions

Set comprehensions work just like list and dictionary comprehensions, but they produce a set, which is an unordered collection of unique elements.

Let's start with an example where we want to create a set from the ages list:

```python title="Input"
ages = [5, 12, 3, 56, 24, 78, 1, 15, 44]
names = ['Tub', 'Barkalot', 'Furrytail']

my_set = set()
for age in ages:
    my_set.add(age)
print(my_set)
```
```python title="Output"
{1, 3, 5, 12, 15, 44, 56, 78}
```

We're creating a set and adding each age to it. The resulting set includes each age once, even if it appeared multiple times in the list.

We can achieve the same result more succinctly with a set comprehension:

```python title="Input"
# {expression for item in iterable}
my_set = {age for age in ages}
print(my_set)
```
```python title="Output"
{1, 3, 5, 12, 15, 44, 56, 78}
```

Here, `age for age in ages` is the expression for each item in the set.

Similar to list and dictionary comprehensions, we can also include a condition in the set comprehension:

```python title="Input"
# {expression for item in iterable if condition}
my_set = {age for age in ages if age > 10}
print(my_set)
```
```python title="Output"
{12, 15, 44, 56, 78}
```

This will include only the ages that are greater than `10` in the set.

In summary, set comprehensions provide a concise way to create sets in Python. They can be especially useful when you need to remove duplicates from a list or other iterable, because sets automatically discard duplicate values.

## 5.6. Generator Compreshensions
Generator comprehensions are an elegant way to create generators using a syntax that is similar to list comprehensions. In fact, you can convert a list comprehension into a generator comprehension just by replacing the square brackets `[]` with parentheses `()`.

Generators are a powerful feature in Python for creating iterable objects. They are a key component of Python's approach to handling large data streams or sequences of data because they enable you to create an iterable object without needing to store all of the values in memory at once. This can provide substantial performance benefits when dealing with large data sets.

We will cover more details in the next [Chapter](http://www.zhenyuanlu.com/python-notebook/06_iterable_iterator_generator/). 


### 5.6.1. Traditional Generator Function

The gen_func function is a generator function that takes a list of ages as an argument. Inside this function, we iterate over the ages list using a for loop. For each age in ages, we yield the value of age incremented by 1. The yield keyword is used in Python generator functions as a sort of "return" that does not end the function, but instead provides a value and pauses the function's execution until the next value is requested.

```python title="Input"
ages = [5, 12, 3, 56, 24, 78, 1, 15, 44]

def gen_func(ages):
    for age in ages:
        yield age+1

my_gen = gen_func(ages)
for item in my_gen:
    print(item)
```
```python title="Output"
6
13
4
57
25
79
2
16
45
```

The `gen_func` function is a generator function that takes a list of `ages` as an argument. Inside this function, we iterate over the `ages` list using a `for` loop. For each `age` in `ages`, we `yield` the value of `age` incremented by 1. The `yield` keyword is used in Python generator functions as a sort of "return" that does not end the function, but instead provides a value and pauses the function's execution until the next value is requested.

We call our generator function `gen_func` with the `ages` list as the argument, and the result (a generator object) is assigned to `my_gen`. Then we use a `for` loop to iterate over the generator object, which causes the generator function to execute and `yield` its values one by one. Each yielded value is printed out.




### 5.6.2. Generator Comprehension

The second part of the code shows a generator comprehension, which is a more compact way of creating a generator. The syntax is very similar to list comprehensions, but uses parentheses `()` instead of square brackets `[]`.

```python title="Input"
# (expression for item in iterable)
my_gen = (age for age in ages)
print(my_gen)

for item in my_gen:
    print(item)
```
```python title="Output"
<generator object <genexpr> at 0x0000020F6F6F0A48>
5
12
3
...
```

This line creates a generator object that will generate the same values as the `ages` list, but on-demand, not storing the entire list in memory.

Generators, both through traditional functions and comprehensions, are a powerful tool in Python. They provide an efficient way to work with large data sets or streams of data that would be inefficient or impractical to store in memory all at once.


<!-- ## 5.4. enumerate introduction and examples
## 5.5. Recursive Functions -->