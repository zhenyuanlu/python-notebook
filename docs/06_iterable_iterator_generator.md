# 6. Iterable, Iterator and Generator

In Python, Iterables and Iterators might seem similar, but they serve distinct purposes and have unique characteristics.

An **Iterable** is an object that can be looped over. This means you can go through its elements one by one, typically using a for loop. Lists, tuples, strings, and dictionaries are all examples of Iterables. They need to implement an `__iter__()` method that returns an Iterator or a `__getitem__()` method for indexed access.

An **Iterator**, on the other hand, is an object that keeps track of its current state during iteration. It must have a `__next__()` method, which returns the next item in the sequence and moves forward, and an `__iter__()` method that returns self. One key aspect of Iterators is that they can only move forward; you can't get an item that has already been iterated over unless you create a new Iterator.

So, the primary difference is that while both can be iterated over, an Iterator also keeps track of its current position in the Iterable. While all **Iterators** are **Iterables** (because they implement an `__iter__()` method), not all **Iterables** are **Iterators** (because they do not provide a `__next__()` method). The power of Iterators comes from their ability to provide items one at a time rather than storing all items in memory at once, which is especially useful when working with large data sets.

A **generator** is a specific type of iterator, which allows us to implement an iterator in a clear and concise way. It's a special kind of function that returns an iterator which we can iterate over to yield sequence of values.

The main difference between a function and a generator in Python is the presence of the yield keyword. While a return statement completely finishes a function execution, yield produces a value and suspends the function’s execution. The function can then be resumed from where it left off, allowing the function to produce a series of values over time, rather than computing them all at once and sending them back.


## 6.1. Iterable 

Data types are **Iterables** in Python:

- Lists
- Tuples
- Strings
- Dictionaries
- Sets
- Generators


In Python, an **Iterable** is an object that can be iterated (looped) over. Essentially, if an object has an `__iter__()` method, it is an Iterable.

You can use `dir()` to check if an object is iterable


Here's an example:

```python title="Input"
pets = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
for pet in pets:
    print(pet)
```
```python title="Output"
Tub
Furrytail
Cat
Barkalot
```

In this case, `pets` is a list, and lists in Python are **Iterables**. We can loop over the list using a `for` loop, and it will print each pet's name one at a time.

### 6.1.1. Checking if an Object is Iterable

You can check whether an object is iterable by using Python's built-in `dir()` function. If `__iter__` appears in the output, the object is iterable.

```python title="Input"
print('__iter__' in dir(pets))  # Will output: True
```
```python title="Output"
True
```


## 6.2. Iterator

An Iterator, on the other hand, is an object with a state that remembers where it is during iteration. While all Iterator objects are Iterable, not all Iterables are Iterators.

An Iterator object is initialized using the `iter()` method, and the `next()` method is used for iteration. Important to note, an Iterator can only move forward; it cannot go backward.

Let's turn our list of pets into an Iterator:

```python title="Input"
pets = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
print(next(pets))
```
```python title="Output"
Output: TypeError: 'list' object is not an iterator
```
Here we get an error because `pets` is a list, and lists are not Iterators. We can, however, turn it into an Iterator using the `iter()` method:

```python title="Input"
iterator_obj = pets.__iter__()
print(iterator_obj)
```
```python title="Output"
<list_iterator object at 0x000001E0F9F4B4C0>
```

Or a better way to do it is:
```python title="Input"
iterator_obj = iter(pets)
print(iterator_obj)
```
```python title="Output"
<list_iterator object at 0x000001E0F9F4B4C0>
```
Now, `iterator_obj` is an **Iterator**. You can't use `next()` directly on the list pets (you would get a `TypeError`), but you can on `iterator_obj`. Let's print the names one by one:

```python title="Input"
print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj)) # This will raise StopIteration error
```
```python title="Output"
Tub
Furrytail
Cat
Barkalot
StopIteration
```
Calling `next()` again would result in a StopIteration error, as there are no more items to iterate over. This is how Python signals the end of an Iterator.

## 6.2.1. Handling StopIteration

We can handle the `StopIteration` error elegantly using a try/except block. Here's how to loop over all the elements of an **Iterator**, stopping cleanly when there are no more items:

```python title="Input"
pets = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
iterator_obj = iter(pets)
while True:
    try:
        next_obj = next(iterator_obj)
        print(next_obj)
    except StopIteration:
        break
```
```python title="Output"
Tub
Furrytail
Cat
Barkalot
``` 

This will print out each pet's name, just like the `for` loop did earlier, but this time we're using the Iterator's `next()` method.

When we reach the end of the Iterator and a `StopIteration` exception is thrown, our `except` clause catches it and we `break` out of the loop, preventing any errors.

NOTE: Here is one example of how to create a Iterator class, we will cover more details in Chapter 7

!!! example "Creating a Custom Iterator"

    Let's look at an example: the `NumIter` class, which is a simple iterator that counts numbers within a given range.
    ```python title="Input"
    class NumIter:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        else:
            return_val = self.current
            self.current += 1
            return return_val
    ```
    Here's what's happening in this code:

    1. The `__init__` method initializes the iterator. It takes a `start` and an `end` as arguments, which determine the range of numbers that the iterator will cover. self.current is used to keep track of the current number in the sequence.

    1. The `__iter__` method is what makes this class an Iterable. It returns `self`, indicating that an instance of the class is its own iterator.

    1. The `__next__` method is the heart of an Iterator. It returns the next value in the sequence each time it's called, and increments `self.current` to prepare for the next call. When there are no more numbers left in the sequence, it raises the `StopIteration` exception, signalling that all values have been returned.

    Now, let's see how we can use this NumIter class:
    
    ```python title="Input"
    nums = NumIter(1, 5)
    for num in nums:
        print(num)
    ```
    ```python title="Output"
    1
    2
    3
    4
    ```
    In this code, we create an instance of `1` that starts at `1` and ends at `5`. We then use a `1` loop to iterate over `1`. This will output the numbers `1` to `4`, one per line.

    Note that after you've iterated over an **Iterator**, it's "`exhausted`" and you can't iterate over it again. So if you try to use the `1` loop with 1 again, it won't print anything.

    However, if we create a new instance, we can manually iterate over it using the `next()` function:
    ```python title="Input"
    nums = NumIter(1, 5)
    print(next(nums))
    print(next(nums))
    print(next(nums))
    print(next(nums))
    print(next(nums))
    ```
    ```python title="Output"
    1
    2
    3
    4
    StopIteration
    ```
    This allows us to manually control when we want the next value, but remember that if you try to get the next value after the iterator is exhausted, it will raise a StopIteration exception.


## 6.3. Generator

A **generator** is a special type of iterator in Python. Generators don't store all their values in memory, but generate them on the fly. This makes them more memory efficient, especially when dealing with large data sets. It doesn't need __iter__() and __next__() methods

### 6.3.1. Creating a Generator

A generator function looks very much like a regular function, but instead of returning a value, it yields it. Here's an example:


```python title="Input"
def iter_nums(start, end):
    current = start
    while current < end:
        yield current
        current +=1
```
In this example, `iter_nums` is a generator function. It takes a `start` and an `end` argument and yields numbers from `start` up to, but not including, `end`.
We can iterate over this generator using the `next()` function:

```python title="Input"
nums = iter_nums(1, 5)
print(next(nums))
print(next(nums))
print(next(nums))
```

```python title="Output"
1
2
3
```

Or we can use a `for` loop:

```python title="Input"
nums = iter_nums(1, 5)
for num in nums:
    print(num)
```
```python title="output"
1
2
3
4
```
This will output numbers 1 through 4.

Generator function is more readable than iterator class we created previously.

**Another example**

```python title="Input"
numbers = [1, 2, 3, 4, 5]

# Now we have a list of numbers, and we want to double each number in the list
def double_nums(nums):
    output = []
    for num in nums:
        output.append(num*2)
    return output

output_nums = double_nums(numbers)
print(output_nums)
```
```python title="Output"
[2, 4, 6, 8, 10]
```
We can easily turn this function into a generator by replacing the append and return statements with a yield statement:
    
```python title="Input"
numbers = [1, 2, 3, 4, 5]
def double_nums(nums):
    for num in nums:
        yield num*2

output_nums = double_nums(numbers)
print(output_nums)
```
As the generator doesn't store the values in memory
You will get the generator object:
```python title="Output"
<generator object double_nums at 0x000001E0F9F4B040>
```

To get the values, you can use `next()`:
```python title="Input"
print(next(output_nums))
```
```python title="Output"
2
```

Or output as a list:

```python title="Input"
print(list(output_nums))
```
```python title="Output"
[2, 4, 6, 8, 10]
```

Of course you can also convert it to the list comprehension as we mentioned in the [Chapter 5](http://127.0.0.1:8000/python-notebook/05_loops_comprehensions/#53-list-comprehensions):

```python title="Input"
numbers = [1, 2, 3, 4, 5]
output_nums_list = [num*2 for num in numbers]
print(output_nums_list)
```
```python title="Output"
[2, 4, 6, 8, 10]
```

### 6.3.2. Generator Expressions
If you replace the square brackets with the parentheses, you will get the generator object:
```python title="Input"
output_nums_generator = (num*2 for num in numbers)
print(list(output_nums_generator))
```
```python title="Output"
[2, 4, 6, 8, 10]
```
In this case, `(num * 2 for num in numbers)` is a generator expression that generates doubled numbers.

### 6.3.3. Generator vs Iterator

In Python, both iterator and generator can be used to iterate over a sentence, word by word. They provide a convenient way to process each word individually. Let's see how we can create an iterator and a generator to do this.

#### Creating a Sentence Iterator

First, let's create an iterator. The iterator class, SentIter, will split the sentence into words and yield each word one by one:


```python title="Input"
class SentIter:
    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.words = sentence.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        else:
            return_val = self.words[self.index]
            self.index += 1
            return return_val
```
Here's how to use this iterator:

```python title="Input"
corpus = "Tub likes Blue Cheese"
words = SentIter(corpus)
for word in words:
    print(word)
```
```python title="Output"
Tub
likes
Blue
Cheese
```
This code will output each word of the sentence on a new line.

#### Creating a Sentence Generator

Now, let's see how we can do the same thing with a generator. We'll write a function, `iter_sent`, that takes a sentence, splits it into words, and yields each word:


```python title="Input"
def iter_sent(sentence):
    for word in sentence.split():
        yield word
```
And here's how to use this generator:
```python title="Input"
words = iter_sent(corpus)
for word in words:
    print(word)
```
```python title="Output"
Tub
likes
Blue
Cheese
```
As you can see, the generator function is shorter and simpler than the iterator class. This is one of the reasons why generators are often preferred over iterators in Python.

### 6.3.4. Generator Performance

In Python, a generator is a simpler and more memory-efficient alternative to a list, especially when the list is large. To demonstrate the difference, let's compare the memory usage and execution time of a list and a generator.

Firstly, let's import the necessary modules. We'll use `random` for generating random data, `time` for measuring execution time, `psutil` and `os` for measuring memory usage:

Installation of psutil via `conda`:
```bash
conda install -c conda-forge psutil
```


!!! example "Performance Comparison: List vs Generator in Python"
    I adapte the code with minor updates from [Corey](https://github.com/CoreyMSchafer/code_snippets/tree/master/Generators) to compare the performance of list and generator
    ```python title="Dependencies"
    import random
    import time
    import psutil
    import os
    import sys
    ```
    Then, let's define a function to measure the current memory usage:

    ```python title="Input"
    def memory_usage_psutil():
        process = psutil.Process(os.getpid())
        mem = process.memory_info().rss / float(2 ** 20)
        return mem
    ```
    Next, let's prepare some dummy data for our test:

    ```python title="Dummy Data"
    names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
    majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']
    ```

    Before generating the data, we'll check and print the memory usage:

    ```python title="Memory Usage (Before)"
    print('Memory (Before): {}Mb'.format(memory_usage_psutil()))
    ```
    Now let's define a function to generate a list of people:
    ```python title="Functions for List"
    def people_list(num_people):
        result = []
        for i in range(num_people):
            person = {
                        'id': i,
                        'name': random.choice(names),
                        'major': random.choice(majors)
                    }
            result.append(person)
        return result
    ```
    And a function to generate the same data as a generator:
    ```python title="Function for Generator"
    def people_generator(num_people):
        for i in range(num_people):
            person = {
                        'id': i,
                        'name': random.choice(names),
                        'major': random.choice(majors)
                    }
            yield person
    ```
    Now let's measure the memory usage and execution time of generating the data using the list and the generator:

    ```pythont title="List - Memory Usage"
    # Use people_list for comparison
    t1 = time.process_time()
    people = people_list(1000000)
    t2 = time.process_time()

    print('Memory (After) : {}Mb'.format(memory_usage_psutil()))
    print('Took {} Seconds'.format(t2-t1))
    ```
    ```python title="Output"
    Memory (Before): 41.6484375Mb
    Memory (After) : 265.08984375Mb
    Took 0.59375 Seconds
    ```
    You can see the memory usage increased by `223.44140625Mb` after generating the list of people. Now let's see how the generator performs:

    ```python title="Generator - Memory Usage"
    # Use people_generator for comparison
    t1 = time.process_time()
    people = people_generator(1000000)
    t2 = time.process_time()

    print('Memory (After) : {}Mb'.format(memory_usage_psutil()))
    print('Took {} Seconds'.format(t2-t1))
    ```
    ```python title="Output"
    Memory (Before): 41.60546875Mb
    Memory (After) : 41.61328125Mb
    Took 0.0 Seconds
    ```
    As you can see, the memory usage increased by only `0.0078125Mb` after generating the generator object. This is because the generator doesn't store the data in memory. Instead, it yields each person one by one. This is why the memory usage of the generator is much lower than that of the list.






