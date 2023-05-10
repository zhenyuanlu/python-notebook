# Sets are unordered collections of unique elements
pet = {'Tub', 'Furrytail', 'Cat', 'Barkalot'}
print(type(pet))
# Output: {'Tub', 'Cat', 'Barkalot', 'Furrytail'}
# If you run it multiple times, the order will be different.
# Sets don't care about the order of the elements.


# Sets throw away the duplicate elements.
pet = {'Tub', 'Furrytail', 'Cat', 'Barkalot', 'Tub'}
print(pet)
# Output: {'Tub', 'Cat', 'Barkalot', 'Furrytail'}

# Sets are optimized for checking whether an element is contained in the set.
pet = {'Tub', 'Furrytail', 'Cat', 'Barkalot'}
print('Tub' in pet)

# What these species have in common
pet_1 = {'Tub', 'Furrytail', 'Cat', 'Barkalot'}
pet_2 = {'Tub', 'Furrytail', 'Bumblefluff ', 'Whiskerfloof'}
print(pet_1.intersection(pet_2))
# Output: {'Tub', 'Furrytail'}

# What these species don't have in common
print(pet_1.difference(pet_2))
# Output: {'Cat', 'Barkalot'}

# What these species have in common and what they don't have in common
print(pet_1.union(pet_2))
# Output: {'Tub', 'Cat', 'Barkalot', 'Furrytail', 'Bumblefluff ', 'Whiskerfloof'}


empty_set = {} # This is a dictionary
empty_set = set()
print(empty_set)