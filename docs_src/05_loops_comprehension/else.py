# else clause

# The else clause executes after the loop completes normally.

tub_age = 5

if tub_age > 18:
    print('Tub is an adult.')
else:
    print('Tub is a child.')

# Output: Tub is a child.


# Another example may not be so obvious. And always makes people confused.

pets = ['Tub', 'Barkalot', 'Furrytail']

for pet in pets:
    print(pet)
else: # More like a `no break` statement
    print('No more pets.')

# Output: Tub
# Output: Barkalot
# Output: Furrytail
# Output: No more pets.

# You may think why the `else` statement is executed?
# Here the `else` statement is more like the `no break` statement.

# For example
for pet in pets:
    print(pet)
    if pet == 'Barkalot':
        break
else:
    print('No more pets.')
# Output: Tub
# Output: Barkalot

# The `else` statement is not executed because the loop is terminated by the `break` statement.


for pet in pets:
    print(pet)
    # Now the loop is not terminated by the `break` statement
    # as the condition is never met.
    if pet == 'NOT EXIST':
        break
else: # More like a `no break` statement
    print('No more pets.')
# Output: Tub
# Output: Barkalot
# Output: Furrytail
# Output: No more pets.


# This is also the same as for `while` loop.
age = 7
while age >=5:
    print(age)
    age -= 1
else: # More like a `no break` statement
    print('End')
# Output: 7
# Output: 6
# Output: 5
# Output: End

age = 7
while age >=5:
    print(age)
    age -= 1
    if age == 6:
        break
else: # More like a `no break` statement
    print('End')
# Output: 7
# Output: 6


# Practical Samples
# Find the first even number in a list
nums = [1, 3, 8, 7, 3, 2, 3]
def find_first_even(nums)->str:
    for num in nums:
        if num % 2 == 0:
            break
    else:
        num = 'None'
    return num

first_even = find_first_even(nums)
print('First even number is: {}'.format(first_even))
# Output: First even number is: 8

# Or nums = [1, 3, 1, 7, 3, 9, 3]
nums = [1, 3, 1, 7, 3, 9, 3]
first_even = find_first_even(nums)
print('First even number is: {}'.format(first_even))
# Output: First even number is: None
