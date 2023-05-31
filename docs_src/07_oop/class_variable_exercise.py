class PetEmployee:
    # Class variable
    num_of_pet_employees = 0
    species_count = {}
    promotion_rate = 1

    def __init__(self, name, age, species, level):
        self.name = name
        self.age = age
        self.species = species
        self.email = name + '.' + species + '@gmail.com'
        self.level = level

        PetEmployee.num_of_pet_employees += 1

        # Updating species count
        if species in PetEmployee.species_count:
            PetEmployee.species_count[species] += 1
        else:
            PetEmployee.species_count[species] = 1

    def fullname(self):
        return '{} {}'.format(self.name, self.species)

    def apply_promotion(self):
        # We need to use the class name to access the class variable
        # This can be either self or PetEmployee
        self.level = self.level + self.promotion_rate

barkalot = PetEmployee('Barkalot', 3, 'Dog', 3)
furrytail = PetEmployee('Furrytail', 2, 'Cat', 5)
mewton = PetEmployee('Mewton', 4, 'Cat', 7)

print(PetEmployee.species_count)
# Output: {'Dog': 1, 'Cat': 2}
