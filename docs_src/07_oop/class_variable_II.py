
# What if we want to change the promotion rate?
# We don't want to change the promotion rate for each instance mannually.
# We can use class variable to do this.

# Small revision to add a class variable

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

barkalot = PetEmployee('Barkalot', 3, 'Dog', 3)
furrytail = PetEmployee('Furrytail', 2, 'Cat', 5)
# How to understand this?
# Here we print out the promotion rate of the class and the instance.
# The promotion rate of the instance is the same as the class.
print(PetEmployee.promotion_rate)
print(barkalot.promotion_rate)
print(furrytail.promotion_rate)
# Output: 1
# Output: 1
# Output: 1

# When we access the attribute of an instance, it will first check if the instance has the attribute.
# If not, it will check if the class has the attribute.
# If not, it will check if the parent class has the attribute.
# Here, the instance doesn't have the promotion_rate attribute, so it will check the class.
# The class has the promotion_rate attribute, so it will use the class attribute.


print(barkalot.__dict__)
# Output: {'name': 'Barkalot', 'age': 3, 'species': 'Dog', 'email': 'Barkalot.Dog@gmail.com', 'level': 3}
print(PetEmployee.__dict__)
# The output contains the attribute promotion_rate

PetEmployee.promotion_rate = 2
print(PetEmployee.promotion_rate)
print(barkalot.promotion_rate)
print(furrytail.promotion_rate)
# Output: 2
# Output: 2
# Output: 2

# Now we only change the promotion rate of the instance.
barkalot.promotion_rate = 3
print(PetEmployee.promotion_rate)
print(barkalot.promotion_rate)
print(furrytail.promotion_rate)
# Output: 2
# Output: 3
# Output: 2
print(barkalot.__dict__)
# Output: {'name': 'Barkalot', 'age': 3, 'species': 'Dog', 'email': 'Barkalot.Dog@gmail.com', 'level': 3, 'promotion_rate': 3}
# Here you can see the attribute promotion_rate only exists in the barkalot instance.

