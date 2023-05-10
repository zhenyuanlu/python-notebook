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


#### Basic Usage
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


#### `break` Statement
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


#### `continue` Statement
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

#### Nested for Loops
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


#### `range()` Function
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

#### `range()` Function with Start and End
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

#### `range()` Function with Start, End, and Step
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
### 5.1.3. Else Loops
## 5.2. List Comprehensions
## 5.3. zip introduction and examples
## 5.4. enumerate introduction and examples
## 5.5. Recursive Functions