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

    @fullname.deleter
    def fullname(self):
        print('Delete Pet Name!')
        self.name = None
        self.species = None


barkalot = PetEmployee('Barkalot', 'Dog', 3)
del barkalot.fullname
print(barkalot.name)
print(barkalot.fullname)
print(barkalot.email)


# None
# None None
# None.None@gmail.com