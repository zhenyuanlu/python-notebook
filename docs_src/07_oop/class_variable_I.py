# Class Variable
class PetEmployee:
    # Of course, you can use other names instead of self. But it is a convention to use self.
    def __init__(self, name, age, species, level):
        self.name = name
        self.age = age
        self.species = species
        self.email = name + '.' + species + '@gmail.com'
        self.level = level

    def fullname(self):
        return '{} {}'.format(self.name, self.species)

    def apply_promotion(self):
        # Apply promotion to the level of the pet employee
        self.level = self.level + 1



barkalot = PetEmployee('Barkalot', 3, 'Dog', 3)
furrytail = PetEmployee('Furrytail', 2, 'Cat', 5)

print(barkalot.level)
barkalot.apply_promotion()
print(barkalot.level)
# Output: 3
# Output: 4
