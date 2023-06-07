# Getters, Setters, and Deleters

class PetEmployee:

    def __init__(self, name, species, level):
        self.name = name
        self.species = species
        self.email = name + '.' + species + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.name, self.species)


barkalot = PetEmployee('Barkalot', 'Dog', 3)

barkalot.name = 'Furrytail'
print(barkalot.name)
print(barkalot.fullname())
print(barkalot.email)

# Furrytail
# Furrytail Dog
# Barkalot.Dog@gmail.com