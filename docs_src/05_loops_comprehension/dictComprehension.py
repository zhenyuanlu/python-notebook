# zip() function
ages = [5, 12, 3, 56, 24, 78, 1, 15, 44]
names = ['Tub', 'Barkalot', 'Furrytail']


my_list = []
for age in range(3):
    for name in names:
        my_list.append((age, name))
print(my_list)
# Output: [(0, 'Tub'), (0, 'Barkalot'), (0, 'Furrytail'), (1, 'Tub'), (1, 'Barkalot'), (1, 'Furrytail'), (2, 'Tub'), (2, 'Barkalot'), (2, 'Furrytail')]

# Using list comprehension
my_list = [(age, name) for age in range(3) for name in names]
print(my_list)
# Output: [(0, 'Tub'), (0, 'Barkalot'), (0, 'Furrytail'), (1, 'Tub'), (1, 'Barkalot'), (1, 'Furrytail'), (2, 'Tub'), (2, 'Barkalot'), (2, 'Furrytail')]

# Dictionary comprehension and zip()
ages = [5, 12, 3, 56, 24, 78, 1, 15, 44]
names = ['Tub', 'Barkalot', 'Furrytail']
# what zip does is it takes the first item from each iterable and puts them together in a tuple
# then it takes the second item from each iterable and puts them together in a tuple
# and so on
print(zip(ages, names))
# Output: <zip object at 0x0000020F6F6F0A48>
print(list(zip(ages, names)))
# Output: [(5, 'Tub'), (12, 'Barkalot'), (3, 'Furrytail')]

# Regular for loop
my_dict = {}
for age, name in zip(ages, names):
    my_dict[name] = age
print(my_dict)
# Output: {'Tub': 5, 'Barkalot': 12, 'Furrytail': 3}

# Dictionary comprehension
# {key: value for item in iterable}
my_dict = {name: age for name, age in zip(names, ages)}
print(my_dict)
# Output: {'Tub': 5, 'Barkalot': 12, 'Furrytail': 3}

# {key: value for item in iterable if condition}
my_dict = {name: age for name, age in zip(names, ages) if age > 10}
print(my_dict)
# Output: {'Barkalot': 12}

