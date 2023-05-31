# Classes and Instances
# Here when we say data and functions, we mean attributes and methods. The method here is associated with one class.

class PetEmployee:
    pass

barkalot = PetEmployee()
furrytail = PetEmployee()
print(barkalot)
print(furrytail)
# Output: <__main__.Pet object at 0x0000020E4F6F4E80>
# Output: <__main__.Pet object at 0x0000020E4F6F4F10>
# Here we have two different addresses for the two different instances of the class Pet.

# For example we can add attributes to the instances.
barkalot.name = "Barkalot"
barkalot.age = 3
barkalot.species = "Dog"
barkalot.email = 'barkalot.dog@gmail.com'
barkalot.pay = 5

furrytail.name = "Furrytail"
furrytail.age = 2
furrytail.species = "Cat"
furrytail.email = 'furrytail.cat@gmail.com'
furrytail.pay = 11

print(barkalot.name)
print(furrytail.name)
# This is not a good way to take the advantage of classes. We can use __init__ method to initialize the attributes.


# __init__ method
class PetEmployee:
    # Of course, you can use other names instead of self. But it is a convention to use self.
    def __init__(self, name, age, species, pay):
        self.name = name
        self.age = age
        self.species = species
        self.email = name + '.' + species + '@gmail.com'
        self.pay = pay


barkalot = PetEmployee('Barkalot', 3, 'Dog', 5)
furrytail = PetEmployee('Furrytail', 2, 'Cat', 11)

print(barkalot.name)
print(furrytail.name)

# If we want to print out the full name of the pet employee.
print('{} {}'.format(barkalot.name, barkalot.species))

# We can define a method within the class to do this.

class PetEmployee:
    # Of course, you can use other names instead of self. But it is a convention to use self.
    def __init__(self, name, age, species, pay):
        self.name = name
        self.age = age
        self.species = species
        self.email = name + '.' + species + '@gmail.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.name, self.species)

barkalot = PetEmployee('Barkalot', 3, 'Dog', 5)
# we need the parenthesis here because fullname is a method not a attributes as the above
print(barkalot.fullname())
# Output: Barkalot Dog
# One more obvious way is to use the class name to call the method.
print(PetEmployee.fullname(barkalot))
# Output: Barkalot Dog


# Why we need to put self in the method?
# If we don't put self in the method, we will get an error.
class PetEmployee:
    # Of course, you can use other names instead of self. But it is a convention to use self.
    def __init__(self, name, age, species, pay):
        self.name = name
        self.age = age
        self.species = species
        self.email = name + '.' + species + '@gmail.com'
        self.pay = pay

    def fullname():
        return '{} {}'.format(self.name, self.species)

barkalot = PetEmployee('Barkalot', 3, 'Dog', 5)
print(barkalot.fullname())
# Output: TypeError: fullname() takes 0 positional arguments but 1 was given
# This is because when we call the method, the instance barkalot is passed as the first argument to the method.
