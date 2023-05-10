ages = [5, 12, 3, 56, 24, 78, 1, 15, 44]

# Regular generator
def gen_func(ages):
    for age in ages:
        yield age+1

my_gen = gen_func(ages)
for item in my_gen:
    print(item)
# Output: 6
# Output: 13
# Output: 4
# Output: 57
# Output: 25
# Output: 79
# Output: 2
# Output: 16
# Output: 45


# Generator comprehension
# (expression for item in iterable)
my_gen = (age for age in ages)
print(my_gen)
# Output: <generator object <genexpr> at 0x0000020F6F6F0A48>
for item in my_gen:
    print(item)
# Output: 5
# Output: 12
#...

