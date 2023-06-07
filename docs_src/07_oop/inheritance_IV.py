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


class PetLeader(PetEmployee):
    promotion_rate = 1

    def __init__(self, name, age, species, level, team=None):
        super().__init__(name, age, species, level)
        if team is None:
            self.team = []
        else:
            self.team = team

    def add_team_member(self, employee):
        if employee not in self.team:
            self.team.append(employee)

    def remove_team_member(self, employee):
        if employee in self.team:
            self.team.remove(employee)

    def print_team(self):
        for employee in self.team:
            print(' ', employee.fullname())


ds_barkalot = PetDataScientist('Barkalot', 3, 'Dog', 3, 'Python')
ds_furrytail = PetDataScientist('Furrytail', 2, 'Cat', 5, 'Mojo')

manager_whiskers = PetLeader('Whiskers', 5, 'Cat', 5, [ds_barkalot])

manager_whiskers.print_team()
print("  ============")
manager_whiskers.add_team_member(ds_furrytail)
manager_whiskers.print_team()
# Output: Barkalot Dog
# Output: Furrytail Cat


# isinstance() function returns True if the object is an instance of the class or other classes derived from it.
print(isinstance(manager_whiskers, PetLeader))
# Output: True
print(isinstance(manager_whiskers, PetDataScientist))
# Output: False

# issubclass() function returns True if class is a subclass (direct, indirect or virtual) of classinfo.
print(issubclass(PetLeader, PetEmployee))
# Output: True
print(issubclass(PetDataScientist, PetLeader))
# Output: True

