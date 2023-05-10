ages = [5, 12, 3, 56, 24, 78, 1, 15, 44]
age_list = []
for age in ages:
    age_list.append(age)
print(age_list)
# Output: [5, 12, 3, 56, 24, 78, 1, 15, 44]

# Make the above for loop into a list comprehension
# [item for item in iterable]
age_list = [age for age in ages]
print(age_list)
# Output: [5, 12, 3, 56, 24, 78, 1, 15, 44]

ages = [5, 12, 3, 56, 24, 78, 1, 15, 44]
age_list = []
for age in ages:
    age_list.append(age + 1)
print(age_list)
# Output: [6, 13, 4, 57, 25, 79, 2, 16, 45]

# [expression for item in iterable]
age_list = [age + 1 for age in ages]
print(age_list)
# Output: [6, 13, 4, 57, 25, 79, 2, 16, 45]

# map(lambda)
age_list = list(map(lambda age: age + 1, ages))
print(age_list)
# Output: [6, 13, 4, 57, 25, 79, 2, 16, 45]

# `map` is faster than list comprehension, but list comprehension is more readable



ages = [5, 12, 3, 56, 24, 78, 1, 15, 44]
age_list = []
for age in ages:
    if age % 2 == 0:
        age_list.append(age)
print(age_list)
# Output: [12, 56, 24, 78, 44]


# [expression for item in iterable if condition]
age_list = [age for age in ages if age % 2 == 0]
print(age_list)
# Output: [12, 56, 24, 78, 44]

# filter(lambda)
age_list = list(filter(lambda age: age % 2 == 0, ages))
print(age_list)
# Output: [12, 56, 24, 78, 44]







# Real world example
pets = ['Tub', 'Furrytail', 'Cat', 'Barkalot', 'Bumblefluff ', 'Whiskerfloof']
output = '<ul>\n'
for pet in pets:
    output += '\t<li>{}</li>\n'.format(pet)
    # print('Address of output is {}'.format(id(output)))
output += '</ul>'
print(output)
# Output: <ul>
# <li>Tub</li>
# <li>Furrytail</li>
# <li>Cat</li>
# <li>Barkalot</li>
# <li>Bumblefluff </li>
# <li>Whiskerfloof</li>
# </ul>


pets = ['Tub', 'Furrytail', 'Cat', 'Barkalot', 'Bumblefluff ', 'Whiskerfloof']
output = '<ul>\n'
# List comprehension to create a list of formatted list items
formatted_pet_names = ['\t<li>{}</li>'.format(pet) for pet in pets]
# Join the list items with newline characters and add the closing </ul> tag
output += '\n'.join(formatted_pet_names) + '\n</ul>'
print(output)
# Output: <ul>
# <li>Tub</li>
# <li>Furrytail</li>
# <li>Cat</li>
# <li>Barkalot</li>
# <li>Bumblefluff </li>
# <li>Whiskerfloof</li>
# </ul>


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



