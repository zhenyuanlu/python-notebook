# String is immutable, so you can't change the value of the string.

# Concatenation
original_string = "Hello, "
pet = "Tub"

# This creates a new string instead of modifying the original one
greeting = original_string + pet
print(greeting)
print('Address of original_string is: {}'.format(id(original_string)))
print('Address of greeting is: {}'.format(id(greeting)))
# Output: "Hello, Tub"
# Address of original_string is: 2186723937904
# Address of greeting is: 2186728523312


# Replace
original_string = "Hello, World!"

# This creates a new string instead of modifying the original one
new_string = original_string.replace("World", "Tub")
print(new_string)
print('Address of original_string is:{}'.format(id(original_string)))
print('Address of new_string is:{}'.format(id(new_string)))
# Output: "Hello, Tub"
# Address of original_string is:1436882337200
# Address of new_string is:1436885468848


# Upper case
original_string = "Tub is awesome!"

# This creates a new string instead of modifying the original one
uppercase_string = original_string.upper()
print(uppercase_string)
print('Address of original_string is:{}'.format(id(original_string)))
print('Address of uppercase_string is:{}'.format((id(uppercase_string))))
# Output: "TUB IS AWESOME!"
# Address of original_string is:1923265193776
# Address of uppercase_string is:1923268233008



# Slicing
original_string = "Tub is cute!"

# This creates a new string instead of modifying the original one
substring = original_string[0:3]
print(substring)
print('Address of original_string is:{}'.format(id(original_string)))
print('Address of substring is:{}'.format(id(substring)))
# Output: "Tub"
# Address of original_string is:1923265193776
# Address of substring is:1923268233008



# Strings, numbers, and tuple are immutable.
# Dictionary, list, and set are mutable.
# fronzen set is immutable.

pet_1 = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
pet_2 = pet_1
pet_1[1] = 'Furrytail 2'
print(pet_1)
print(pet_2)
# Output: ['Tub', 'Furrytail 2', 'Cat', 'Barkalot']
# Output: ['Tub', 'Furrytail 2', 'Cat', 'Barkalot']

print('Address of pet_1 is: {}'.format(id(pet_1)))
print('Address of pet_2 is: {}'.format(id(pet_2)))
#Address of pet_1 is: 2250825683136
# Address of pet_2 is: 2250825683136

# If you want to create a new list that is a copy of species_1
# so that changes made to one do not affect the other, you can use the copy method:
pet_1 = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
pet_2 = pet_1.copy()
pet_1[1] = 'Furrytail 2'
print(pet_1)
print(pet_2)

# Output: ['Tub', 'Furrytail 2', 'Cat', 'Barkalot']
# Output: ['Tub', 'Furrytail', 'Cat', 'Barkalot']

print('Address of pet_1 is: {}'.format(id(pet_1)))
print('Address of pet_2 is: {}'.format(id(pet_2)))
# Address of pet_1 is: 1704413046016
# Address of pet_2 is: 1704413120128

# You can see that the list is mutable, and the second variable in both of the lists is also changed.

# Immutable
pet_tup_1 = ('Tub', 'Furrytail', 'Cat', 'Barkalot')
pet_tup_1[1] = 'Furrytail 2'
print(pet_tup_1)
# Output: TypeError: 'tuple' object does not support item assignment

