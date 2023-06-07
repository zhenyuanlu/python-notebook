# Getters, Setters, and Deleters

class PetEmployee:

    def __init__(self, name, species, level):
        self.name = name
        self.species = species

    @property
    def email(self):
        return "{}.{}@gmail.com".format(self.name, self.species)

    @property
    def fullname(self):
        return '{} {}'.format(self.name, self.species)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.name = first
        self.species = last


barkalot = PetEmployee('Barkalot', 'Dog', 3)

barkalot.fullname = 'Furrytail Cat'
print(barkalot.name)
print(barkalot.fullname)
print(barkalot.email)

# Furrytail
# Furrytail Dog
# Furrytail.Dog@gmail.com