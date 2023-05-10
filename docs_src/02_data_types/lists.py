# A list of specie names
species = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
print(species)
# Output: ['Tub', 'Furrytail', 'Cat', 'Barkalot']

# Length of the list
species = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
print(len(species))
# Output: 4

# Indexing starts from 0
species = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
print(species[0])
# Output: Tub

# If index is negative, it starts from the end
species = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
print(species[-1])
# Output: Barkalot

# If we input 4, it will throw an error
species = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
# print(species[4])
# Output: IndexError: list index out of range

# List slicing
# Slicing starts from 0
species = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
# Index: 1, 2, 3, 4
print(species[0:2])
# Output: ['Tub', 'Furrytail']

# Omit the first index
species = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
print(species[:2])
# Output: ['Tub', 'Furrytail']

# Omit the second index
species = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
print(species[2:])
# Output: ['Cat', 'Barkalot']

# Omit both index
species = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
print(species[:])
# Output: ['Tub', 'Furrytail', 'Cat', 'Barkalot']

# Slicing a list of numbers
numbers_list = [1, 2, 3, 4, 5]
# Reverse Index: -5, -4, -3, -2, -1

print(numbers_list[-3:-1])
# Output: [3, 4]

print(numbers_list[-3:])
# Output: [3, 4, 5]

print(numbers_list[:-3])
# Output: [1, 2]

print(numbers_list[1:-2])
# Output: [2, 3]

numbers_list = [1, 2, 3, 4, 5]
# list[start:end:step]

print(numbers_list[0:3])
# Output: [1, 2, 3]

print(numbers_list[0:3:1])
# Output: [1, 2, 3]

print(numbers_list[0:3:2])
# Output: [1, 3]

print(numbers_list[0:3:-1])
# Output: []

print(numbers_list[-1:1:-2])
# Output: [5, 3]

print(numbers_list[::-2])
# Output: [5, 3, 1]


# Add an item to the end of the list
species = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
species.append('Hootsworth ')
print(species)
# Output: ['Tub', 'Furrytail', 'Cat', 'Barkalot', 'Hootsworth ']

# Add an item to a specific index
species = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
species.insert(2, 'Fish')
print(species)
# Output: ['Tub', 'Furrytail', 'Fish', 'Cat', 'Barkalot']

# Insert a list into a list
pet = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
pet_2 = ['Bumblefluff ', 'Whiskerfloof']
pet.insert(0, pet_2)
print(pet)
# Output: [['Bumblefluff ', 'Whiskerfloof'], 'Tub', 'Furrytail', 'Cat', 'Barkalot']
# This is not what we want

# Extend a list
pet = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
pet_2 = ['Bumblefluff ', 'Whiskerfloof']
species.extend(pet_2)
print(pet)
# Output: ['Tub', 'Furrytail', 'Cat', 'Barkalot', 'Bumblefluff ', 'Whiskerfloof']

# Remove an item from the list
pet = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
pet.remove('Tub')
print(pet)
# Output: ['Furrytail', 'Cat', 'Barkalot']

pet = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
pet.pop()
print(pet)
# Output: ['Tub', 'Furrytail', 'Cat']

pet = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
pet.pop(1)
print(pet)
# Output: ['Tub', 'Cat', 'Barkalot']

pet = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
popped_pet = pet.pop()
print(popped_pet)
# Output: Barkalot
# This is very helpful when we have a queue to keep popping until the queue is empty

# Reverse a list
pet = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
pet.reverse()
print(pet)
# Output: ['Barkalot', 'Cat', 'Furrytail', 'Tub']

# Sort a list
pet = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
pet.sort()
print(pet)
# Output: ['Barkalot', 'Cat', 'Furrytail', 'Tub']

nums = [5, 3, 2, 4, 1]
nums.sort()
print(nums)
# Output: [1, 2, 3, 4, 5]

# Instead of using .reverse(), we can use reverse = True
nums.sort(reverse = True)
print(nums)
# Output: [5, 4, 3, 2, 1]

# These methods are changing our original variables
# What if we want to keep the original variables.
pet = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
sorted_pet = sorted(pet)
print(sorted_pet)
print(pet)
# Output: ['Barkalot', 'Cat', 'Furrytail', 'Tub']
# Output: ['Tub', 'Furrytail', 'Cat', 'Barkalot']

# Search for an index of an item in the list
print(pet.index('Tub'))
# Output: 0

# If an item is in the list
print('Tub' in pet)
# Output: True

# Join a list of strings
pet_str = ','.join(pet)
print(pet_str)
# Output: Tub,Furrytail,Cat,Barkalot

# Split a string into a list by ','
pet_str = ','.join(pet)
pet_list = pet_str.split(',')
print(pet_list)
# Output: ['Tub', 'Furrytail', 'Cat', 'Barkalot']


# Deal with a list of numbers
nums = [5, 3, 2, 4, 1]
print(min(nums))
# Output: 1

nums = [5, 3, 2, 4, 1]
print(max(nums))
# Output: 5

nums = [5, 3, 2, 4, 1]
print(sum(nums))
# Output: 15


# Create empty list
empty_list = []
empty_list = list()




