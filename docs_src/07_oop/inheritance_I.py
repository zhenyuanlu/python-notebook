# Inheritance

class PetEmployee:
    # Class variable
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
        # We need to use the class name to access the class variable
        # This can be either self or PetEmployee
        self.level = self.level + self.promotion_rate


# Subclass of PetEmployee
class PetDataScientist(PetEmployee):
    pass


barkalot = PetDataScientist('Barkalot', 3, 'Dog', 3)
furrytail = PetDataScientist('Furrytail', 2, 'Cat', 5)
print(barkalot.email)
print(furrytail.email)

# Output: Barkalot.Dog@gmail.com
# Output: Furrytail.Cat@gmail.com

# We can use the help function to see the method resolution order (MRO) of the class
print(help(PetDataScientist))
# Method resolution order:
#  |      PetDataScientist
#  |      PetEmployee
#  |      builtins.object






