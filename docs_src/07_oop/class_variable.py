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
furrytail = PetEmployee('Furrytail', 2, 'Cat', 11)


