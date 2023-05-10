
# Function Basics
def hello_tub():
    pass

print(hello_tub)
# Output: <function hello_world at 0x000001E5F1F9B790>
print(hello_tub())
# Output: None


def hello_tub():
    print('Hello Tub')
hello_tub()
# Output: Hello Tub

# The advantage of functions
print('Hello Tub')
print('Hello Tub')

# What if we want to change both `Tub'
def hello_tub():
    print('Hello Barkalot')
hello_tub()
hello_tub()
# Output: Hello Barkalot


def hello_tub():
    return 'Hello Tub'
print(hello_tub())
# Output: Hello Tub

print(hello_tub().lower())
# Output: hello tub


def hello_tub(name):
    return 'Hello ' + name
print(hello_tub('Tub'))
# Output: Hello Tub

def hello_tub(name):
    return 'Hello {}'.format(name)
print(hello_tub('Tub'))
# Output: Hello Tub

def hello_tub(greeting, name = 'Tub'):
    return '{}, {}'.format(greeting, name)
print(hello_tub('Hello'))
# Output: Hello, Tub

print(hello_tub('Hello', 'Barkalot'))
# Output: Hello, Barkalot


# Positional Arguments
# def hello_tub(greeting = 'Hello', name):
#     return '{}, {}'.format(greeting, name)
# SyntaxError: non-default argument follows default argument


# *args and **kwargs
def pet_info(*args, **kwargs):
    print(args)
    print(kwargs)
pet_info('Tub', 'Barkalot', 'Furrytail', pet1 = 'Tub', pet2 = 'Barkalot', pet3 = 'Furrytail')
# Output: ('Tub', 'Barkalot', 'Furrytail')
# Output: {'pet1': 'Tub', 'pet2': 'Barkalot', 'pet3': 'Furrytail'}

def pet_info(*args, **kwargs):
    print(args)
    print(kwargs)

favorite_food = ['Carrot', 'Brocolli', 'Ice Cream']
info = {'name': 'Tub', 'age': 25}
pet_info(favorite_food, info)
# (['Carrot', 'Brocolli', 'Ice Cream'], {'name': 'Tub', 'age': 25})
# {}
pet_info(*favorite_food, **info)
# ('Carrot', 'Brocolli', 'Ice Cream')
# {'name': 'Tub', 'age': 25}


# Credits: python standard library, and Corey Schafer
# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """
    Return True for leap years, False for non-leap years.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """
    Return number of days in that month in that year.
    """
    # year 2017
    # month 2
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(is_leap(2017))
# Output: False
print(days_in_month(2017, 2))

