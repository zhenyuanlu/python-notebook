
# Key value pairs
# Dictionaries are unordered
# Dictionaries are mutable

pet = {'species': 'Tub', 'age': 5, 'habitat': ['bathroom', 'kitchen']}
print(pet)
# Output: {'species': 'Tub', 'age': 5, 'habitat': ['bathroom', 'kitchen']}

print(pet['species'])
# Output: Tub

pet = {1: 'Tub', 'age': 5, 'habitat': ['bathroom', 'kitchen']}
print(pet[1])
# Output: Tub

# Access a key that not exist
pet = {'species': 'Tub', 'age': 5, 'habitat': ['bathroom', 'kitchen']}
print(pet['weight'])
# Output: KeyError: 'weight'

# Get method
pet = {'species': 'Tub', 'age': 5, 'habitat': ['bathroom', 'kitchen']}
print(pet.get('age'))
# Output: 5
print(pet.get('weight'))
# Output: None

pet = {'species': 'Tub', 'age': 5, 'habitat': ['bathroom', 'kitchen']}
print(pet.get('weight', 'Not exist'))
# Output: Not exist


pet = {'species': 'Tub', 'age': 5, 'habitat': ['bathroom', 'kitchen']}
pet['weight'] = 2000
print(pet)
# Output: {'species': 'Tub', 'age': 5, 'habitat': ['bathroom', 'kitchen'], 'weight': 2000}


pet = {'species': 'Tub', 'age': 5, 'habitat': ['bathroom', 'kitchen']}
pet.update({'weight': 1000, 'name': 'Fluffy', 'age': 6})
print(pet)
# Output: {'species': 'Tub', 'age': 6, 'habitat': ['bathroom', 'kitchen'], 'weight': 1000, 'name': 'Fluffy'}




species = {'species': 'Tub', 'age': 5, 'habitat': ['bathroom', 'kitchen']}
del species['age']
print(species)
# Output: {'species': 'Tub', 'habitat': ['bathroom', 'kitchen']}



species = {'species': 'Tub', 'age': 5, 'habitat': ['bathroom', 'kitchen']}
species.pop('age')
print(species)
# Output: {'species': 'Tub', 'habitat': ['bathroom', 'kitchen']}

age = species.pop('age')
print(species)
print(age)
# Output: {'species': 'Tub', 'habitat': ['bathroom', 'kitchen']}
# Output: 5


species = {'species': 'Tub', 'age': 5, 'habitat': ['bathroom', 'kitchen']}
print(len(species))
# Output: 3

print(species.keys())
# Output: dict_keys(['species', 'age', 'habitat'])

print(species.values())
# Output: dict_values(['Tub', 5, ['bathroom', 'kitchen']])

print(species.items())
# Output: dict_items([('species', 'Tub'), ('age', 5), ('habitat', ['bathroom', 'kitchen'])])















