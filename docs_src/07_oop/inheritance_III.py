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

    def __init__(self, name, age, species, level, language):
        super().__init__(name, age, species, level)
        self.language = language


ds_barkalot = PetDataScientist('Barkalot', 3, 'Dog', 3, 'Python')
ds_furrytail = PetDataScientist('Furrytail', 2, 'Cat', 5, 'Mojo')

print(ds_barkalot.language)





