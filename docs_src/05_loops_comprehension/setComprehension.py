ages = [5, 12, 3, 56, 24, 78, 1, 15, 44]
names = ['Tub', 'Barkalot', 'Furrytail']

my_set = set()
for age in ages:
    my_set.add(age)
print(my_set)
# Output: {1, 3, 5, 12, 15, 44, 56, 78}

# Set comprehension
# {expression for item in iterable}
my_set = {age for age in ages}
print(my_set)
# Output: {1, 3, 5, 12, 15, 44, 56, 78}

# {expression for item in iterable if condition}
my_set = {age for age in ages if age > 10}
print(my_set)
# Output: {12, 15, 44, 56, 78}

