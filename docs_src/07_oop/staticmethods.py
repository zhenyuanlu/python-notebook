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

    @staticmethod
    def is_walking_pet_today(day):
        if day.weekday() == 6:
            return 'Yaay! It\'s time to walk the pets!'
        return 'Sorry, you have to get back to work!'


barkalot = PetEmployee('Barkalot', 3, 'Dog', 3)
furrytail = PetEmployee('Furrytail', 2, 'Cat', 5)

# Note: if we don't use any of the class attributes, we can use staticmethod

import datetime
today_date = datetime.date.today()
print(PetEmployee.is_walking_pet_today(today_date))
# Output: False
