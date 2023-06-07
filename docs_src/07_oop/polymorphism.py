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

    def daily_duty(self):
        return "Work! Work! Work!"


class PetDataScientist(PetEmployee):
    promotion_rate = 2

    def __init__(self, name, age, species, level, language):
        super().__init__(name, age, species, level)
        self.language = language

    def daily_duty(self):
        return "Importing data, analyzing data, and drinking coffee"

class PetLeader(PetEmployee):
    promotion_rate = 1

    def __init__(self, name, age, species, level, team=None):
        super().__init__(name, age, species, level)
        if team is None:
            self.team = []
        else:
            self.team = team

    def daily_duty(self):
        return "Lead team and setting goals"


def pet_daily_duty(pet):
    print(pet.daily_duty())

emp_barkalot = PetEmployee('Barkalot', 3, 'Dog', 3)
ds_furrytail = PetDataScientist('Furrytail', 2, 'Cat', 5, 'Python')
manager_barkalot = PetLeader('Whiskers', 5, 'Cat', 5)

pets = [emp_barkalot, ds_furrytail, manager_barkalot]

for pet in pets:
    pet_daily_duty(pet)

# Work! Work! Work!
# Importing data, analyzing data, and drinking coffee
# Lead team and setting goals
