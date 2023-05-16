# enumerate(iterable, start=0)

pets = ['Tub', 'Barkalot', 'Furrytail']
for i, pet in enumerate(pets):
    print(i, pet)
# Output: 0 Tub
# Output: 1 Barkalot
# Output: 2 Furrytail

# Using enumerate with a Different Start Index
pets = ['Tub', 'Barkalot', 'Furrytail']
for i, pet in enumerate(pets, start=1):
    print(i, pet)
# Output: 1 Tub
# Output: 2 Barkalot
# Output: 3 Furrytail


# Practical Usage of enumerate
pets = ['Tub', 'Barkalot', 'Furrytail']
for i, pet in enumerate(pets):
    if pet == 'Tub':
        pets[i] = 'Cat'
print(pets)
# Output: ['Cat', 'Barkalot', 'Furrytail']



# Exercise

def find_first_even(nums)->tuple:
    for i, num in enumerate(nums):
        if num % 2 == 0:
            break
    else:
        return ('None', 'None')
    return (i, num)

nums = [1, 3, 8, 7, 3, 2, 3]
first_even = find_first_even(nums)
print('The index and value of the first even number are: {}'.format(first_even))
# Output: The index and value of the first even number are: (2, 8)

nums = [1, 3, 1, 7, 3, 9, 3]
first_even = find_first_even(nums)
print('The index and value of the first even number are: {}'.format(first_even))
# Output: The index and value of the first even number are: ('None', 'None')
