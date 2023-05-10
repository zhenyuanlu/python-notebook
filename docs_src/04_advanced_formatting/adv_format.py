## 2.8. Advanced Formatting

species_1 = {'species': 'Tub', 'age': 5}
sentence = 'My name is ' + species_1['species'] + ' and I am ' + str(species_1['age']) + ' years old.'
print(sentence)
# Output: My name is Tub and I am 5 years old.

# We can see there are a lot of blank space we have to manually put in the beginning and the end of each string.
# We also have to cast the integer/number into strings.

# A better way to do this
sentence = 'My name is {} and I am {} years old.'.format(species_1['species'], species_1['age'])
print(sentence)
# Output: My name is Tub and I am 5 years old.


sentence = 'My name is {0} and I am {1} years old.'.format(species_1['species'], species_1['age'])
print(sentence)
# Output: My name is Tub and I am 5 years old.


tag = 'p'
text = 'This is a paragraph'
sentence = '<{0}>{1}</{0}>'.format(tag, text)
print(sentence)
# Output: <p>This is a paragraph</p>


# This is very useful when we have a placeholder that you want to reuse.
sentence = 'My name is {0} and I am {1} years old. My friend Barkalot is also {1} years old.'.format(
    species_1['species'], species_1['age'])
print(sentence)
# Output: My name is Tub and I am 5 years old. My friend Barkalot is also Tub years old.

# We can also put the key in the placeholder
sentence = 'My name is {0[species]} and I am {1[age]} years old.'.format(species_1, species_1)
print(sentence)
# Output: My name is Tub and I am 5 years old.

# But this is redundant
sentence = 'My name is {0[species]} and I am {0[age]} years old.'.format(species_1)
print(sentence)
# Output: My name is Tub and I am 5 years old.

# We can also use the index of a list in the placeholder
species = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
sentence = 'I am {0[1]} and my friend is {0[3]}.'.format(species)
print(sentence)


# Output: I am Furrytail and my friend is Barkalot.

# We can also access the attributes of an object in the same way

class Species:

    def __init__(self, species, age):
        self.species = species
        self.age = age


species_new = Species('Jerry', 88)

sentence = 'My name is {0.species} and I am {0.age} years old.'.format(species_new)
print(sentence)
# Output: My name is Jerry and I am 88 years old.

# We can also use the key word arguments
sentence = 'My name is {species} and I am {age} years old.'.format(species='Jerry', age=88)
print(sentence)
# Output: My name is Jerry and I am 88 years old.



# This method is useful when we print out the dictionaries, which is more readable
pet = {'species': 'Tub', 'age': 5}
sentence = 'My name is {species} and I am {age} years old.'.format(**pet)
print(sentence)
# Output: My name is Tub and I am 5 years old.
# why use **species instead of species?


for i in range(1, 6):
    sentence = 'The value is {}'.format(i)
    print(sentence)
# Output:
# The value is 1
# The value is 2
# The value is 3
# The value is 4
# The value is 5


for i in range(1, 6):
    sentence = 'The value is {:02}'.format(i)
    print(sentence)
# Output:
# The value is 01
# The value is 02
# The value is 03
# The value is 04
# The value is 05


# We can use `:03` to pad the number with 0s
for i in range(1, 6):
    sentence = 'The value is {:03}'.format(i)
    print(sentence)
# Output:
# The value is 001
# The value is 002
# The value is 003
# The value is 004
# The value is 005

# We can also use the `:.2f` with two decimal places
e = 2.71828
sentence = 'e is equal to {:.2f}'.format(e)
print(sentence)
# Output: e is equal to 2.72

# We can also use the `,` to separate the thousands
sentence = '1 KM is equal to {:,.2f} meters'.format(1000)
print(sentence)
# Output: 1 KM is equal to 1,000.00 meters


# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
import datetime
today_date = datetime.datetime(2023, 4, 1, 10, 10, 30)
print(today_date)
# Output: 2023-04-01 10:10:30

# We can use the `strftime` method to format the date
import datetime
today_date = datetime.datetime(2023, 4, 1, 10, 10, 30)
today_date = '{:%B %d, %Y}'.format(today_date)
print(today_date)
# Output: April 01, 2023

# We can also use the `strptime` method to parse the string into a date
import datetime
date_str = 'April 01, 2023'
today_date = datetime.datetime.strptime(date_str, '%B %d, %Y')
print(today_date)
# Output: 2023-04-01 00:00:00


import datetime
today_date = datetime.datetime(2023, 4, 1, 10, 10, 30)
sentence = 'Today is {0:%B %d, %Y} on {0:%A}, and {0:%Y} has passed {0:%j} days'.format(today_date)
print(sentence)
# Output: Today is April 01, 2023 on Thursday, and 2023 has passed 091 days

# We can also use the `timetuple` method to remove the 0 in the beginning of 091
sentence = 'Today is {0:%B %d, %Y} on {0:%A}, and {0:%Y} has passed {1:d} days'.format(today_date, today_date.timetuple().tm_yday)
print(sentence)
# Output: Today is April 01, 2023 on Thursday, and 2023 has passed 91 days





