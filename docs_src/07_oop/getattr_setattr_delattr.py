class PetEmployee:
    def __init__(self, name, species, level):
        self.name = name
        self.species = species
        self.level = level


barkalot = PetEmployee('Barkalot', 'Dog', 3)
# Using getattr()
print(getattr(barkalot, 'name'))  # Output: Barkalot


# Using setattr()
setattr(barkalot, 'name', 'Furrytail')
print(barkalot.name)  # Output: Furrytail


# Using delattr()
delattr(barkalot, 'name')

# Now trying to access the name attribute will raise an AttributeError
print(barkalot.name)  # Output: AttributeError: 'PetEmployee' object has no attribute 'name'
