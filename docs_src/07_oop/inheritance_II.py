# Inheritance

class PetEmployee:
    promotion_rate = 1

    def __init__(self, name, age, species, level):
        self.name = name
        self.age = age
        self.species = species
        self.email = name + '.' + species + '@gmail.com'
        self.level = level

    def fullname(self):
        return '{} {}'.format(self.name, self.species)

    def apply_promotion(self):
        self.level = self.level + self.promotion_rate


class PetDataScientist(PetEmployee):
    promotion_rate = 2


barkalot = PetDataScientist('Barkalot', 3, 'Dog', 3)
furrytail = PetDataScientist('Furrytail', 2, 'Cat', 5)

print(barkalot.level)
barkalot.apply_promotion()
print(barkalot.level)
# Output: 3
# Output: 5




