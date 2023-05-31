# Classmethods and Staticmethods

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

    @classmethod
    def set_promotion_rate(cls, rate):
        cls.promotion_rate = rate


barkalot = PetEmployee('Barkalot', 3, 'Dog', 3)
furrytail = PetEmployee('Furrytail', 2, 'Cat', 5)

print(PetEmployee.promotion_rate)
print(barkalot.promotion_rate)
print(furrytail.promotion_rate)
# Output: 1
# Output: 1
# Output: 1

PetEmployee.set_promotion_rate(2)
# This is the same as:
PetEmployee.promotion_rate = 2

print(PetEmployee.promotion_rate)
print(barkalot.promotion_rate)
print(furrytail.promotion_rate)
# Output: 2
# Output: 2
# Output: 2

# Use classmethod as an alternative constructor
# If we want to create new pet employees from a string
barkalot_str = 'Barkalot-3-Dog-3'
furrytail_str = 'Furrytail-2-Cat-5'
name, age, species, level = barkalot_str.split('-')
barkalot = PetEmployee(name, age, species, level)
print(barkalot.fullname())
# Output: Barkalot Dog

# This is a lot of work. We can use classmethod to create new pet employees from a string
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

    @classmethod
    def set_promotion_rate(cls, rate):
        cls.promotion_rate = rate

    @classmethod
    def from_string(cls, emp_str):
        name, age, species, level = emp_str.split('-')
        return cls(name, age, species, level)


barkalot_str = 'Barkalot-3-Dog-3'
furrytail_str = 'Furrytail-2-Cat-5'

barkalot = PetEmployee.from_string(barkalot_str)
furrytail = PetEmployee.from_string(furrytail_str)

print(barkalot.fullname())
# Output: Barkalot Dog




