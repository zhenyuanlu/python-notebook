# Magic(dunder) Methods

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


barkalot = PetEmployee('Barkalot', 3, 'Dog', 3)
furrytail = PetEmployee('Furrytail', 2, 'Cat', 5)

# Before we define __repr__ and __str__
# print(barkalot)
# Output: <__main__.PetEmployee object at 0x0000020E0F6F6F98>
# This is not that useful

# difference between __repr__ and __str__
# __repr__ is used for debugging and logging
# __str__ is used for displaying to the end user
print(repr(barkalot))
print(str(barkalot))
# Output: "PetEmployee('Barkalot', 3, 'Dog', 3)"
# Output: Barkalot Dog

