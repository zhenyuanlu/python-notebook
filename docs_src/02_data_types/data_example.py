# Example: Virtual Pet Management System

# Variables and Data Types
name = "Fluffy"
species = "Tub"
age = 3
weight = 4.2

# Strings
formatted_name = name.capitalize()
formatted_species = species.capitalize()

# Numbers
next_year_age = age + 1
weight_in_grams = weight * 1000

# Lists and Tuples
pets = [("Fluffy", "Tub", 3, 4.2), ("Buddy", "Furrytail", 5, 7.8)]
pet_1 = {'species': 'Tub', 'age': 5, 'habitat': ['bathroom', 'kitchen']}
pet_2 = ['Bumblefluff ', 'Whiskerfloof']
pet = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
# Dictionaries
pet_dict = {
    "name": "Fluffy",
    "species": "Tub",
    "age": 3,
    "weight": 4.2
}

# Print the formatted pet information
print(f"{formatted_name} is a {formatted_species} and is {age} years old. Next year, {name} will be {next_year_age} years old.")
print(f"{formatted_name} weighs {weight} kg, which is {weight_in_grams} grams.")
print("List of pets:", pets)
print("Pet dictionary:", pet_dict)
