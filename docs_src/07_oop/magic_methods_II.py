# Magic(dunder) Methods
# https://docs.python.org/3/reference/datamodel.html
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

    def __repr__(self):
        return "PetEmployee('{}', {}, '{}', {})".format(self.name, self.age, self.species, self.level)

    def __str__(self):
        return '{}, {}'.format(self.fullname(), self.species)

    def __add__(self, other):
        return self.level + other.level

    def __len__(self):
        return len(self.species)


barkalot = PetEmployee('Barkalot', 3, 'Dog', 3)
furrytail = PetEmployee('Furrytail', 2, 'Cat', 5)

print(barkalot + furrytail)
# print(barkalot.__add__(furrytail))
# Output: 8

print(len(barkalot))
# print(barkalot.__len__())
# Output: 3