# Advanced Formatting


#
# sentence = 'My name is ' + species_1['species'] + ' and I am ' + str(species_1['age']) + ' years old.'
# print(sentence)
#
#
# sentence_1 = 'My name is {} and I am {} years old.'.format(species_1['species'], species_1['age'])
# print(sentence_1)
#
# sentence_2 = 'My name is {0} and I am {1} years old.'.format(species_1['species'], species_1['age'])
# print(sentence_2)

# tag = 'p'
# text = 'This is a paragraph'
# sentence = '<{0}>{1}</{0}>'.format(tag, text)
# print(sentence)

# species_1 = {'species': 'Tub', 'age': 5}
#
# # sentence = 'My name is {0} and I am {1} years old. My friend Barkalot is also {1} years old.'\
# #     .format(species_1['species'], species_1['age'])
#
# sentence = 'My name is {0[species]} and I am {0[age]} years old.'\
#     .format(species_1)
# print(sentence)

# species = ['Tub', 'Cat', 'Dog']
# sentence = 'I am {0[1]} and my friend is {0[2]}'.format(species)
# print(sentence)

class Species:
    def __init__(self, species, age):
        self.species = species
        self.age = age

    def concat_str(self):
        return self.species + str(self.age)


species_name = Species('Jerry', 88)
print(species_name.species)
print(species_name.age)

sentence = 'My name is {0.species} and I am {0.age} years old.'.format(species_name)
print(sentence)
print(species_name.concat_str())