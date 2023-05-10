if True:
    print("It's true!")
# Output: It's true!

if False:
    print("It's true!")
# Output: Nothing

# We don't hardcode the condition to be True or False, we basically assess the condition to be True or False

# We can use comparison operators to compare two values
pet = 'Tub'
if pet == 'Tub':
    print("It's true!")
# Output: It's true!

# Recall the operator we used in the previous chapter. This time, we use it in the condition, beside the `is` keyword.
# Comparison Operators
# Equal: ==
# Not Equal: !=
# Greater Than: >
# Less Than: <
# Greater or Equal: >=
# Less or Equal: <=
# Identity: is

# We can use comparison operators to compare two values, `pet` and `Tub`
pet = 'Tub'
if pet == 'Tub':
    print("Pet is Tub!")
else:
    print("Pet is not Tub!")
# Output: Pet is Tub!

pet = 'Barkalot'
if pet == 'Tub':
    print("Pet is Tub!")
else:
    print("Pet is not Tub!")

# We use `elif` to add more conditions to the `if` statement.
# Here we have two conditions, `pet == 'Tub'` and `pet == 'Barkalot'`
# If the first condition is not met, we move on to the next condition
# If the second condition is not met, we move on to the `else` statement
pet = 'Barkalot'
if pet == 'Tub':
    print("Pet is Tub!")
elif pet == 'Barkalot':
    print("Pet is Barkalot!")
else:
    print("Pet is not Tub!")

# The difference between `is` and `==`
# `is` checks if two variables point to the same object
# `==` checks if the values of two variables are equal
pet_1 = ['Tub', 'Barkalot', 'Furrytail']
pet_2 = ['Tub', 'Barkalot', 'Furrytail']

print(pet_1 == pet_2)
# Output: True
print(pet_1 is pet_2)
# Output: False
# The reason is that `pet_1` and `pet_2` point to different objects in memory.
print(id(pet_1))
# Output: 2398480322752
print(id(pet_2))
# Output: 2398482691520
# You can see that the memory addresses are different.

# But if we assign `pet_2` to `pet_1`, they will point to the same object in memory.
pet_2 = pet_1
print(pet_1 == pet_2)
# Output: True
print(pet_1 is pet_2)
# Output: True


# We can use `and` and `or` to combine conditions
# `and` means both conditions must be met
# `or` means at least one condition must be met
account_name = 'Tub'
account_passcode = True

if account_name == 'Tub' and account_passcode:
    print("Login successful!")
else:
    print("Login failed!")
# Output: Login successful!

account_name = 'Tub'
account_passcode = True

if account_name == 'Tub' or account_passcode:
    print("Name or passcode is correct!")
else:
    print("Name and passcode are incorrect!")
# Output: Name or passcode is correct!

# We can use `not` to negate a condition
# `not` means the condition must not be met
account_name = 'Tub'
account_passcode = True
if not account_passcode:
    print("Please enter your passcode!")
else:
    print("Login successful!")
# Output: Login successful!

# Here, we use `not` to negate the condition `account_passcode == True` to `account_passcode == False`
# Therefore, the condition must not be met, which is `account_passcode == False`, and the `if` statement is executed
# If we remove `not`, the condition must be met, which is `account_passcode == True`, and the `else` statement is executed

# We can use `in` to check if a value is in a list
# `in` means the value must be in the list
pets = ['Tub', 'Barkalot', 'Furrytail']
if 'Tub' in pets:
    print("Tub is in the list!")
else:
    print("Tub is not in the list!")
# Output: Tub is in the list!

pets = ['Tub', 'Barkalot', 'Furrytail']
if 'Tub' not in pets:
    print("Tub is not in the list!")
else:
    print("Tub is in the list!")


# Some false values
# False
# None
# Zero of any numeric type
# Any empty sequence. For example, '', (), [].
# Any empty mapping. For example, {}.

# False is considered as False
account_name = False
if account_name:
    print("Login successful!")
else:
    print("Please enter your account name!")
# Output: Please enter your account name!

# None is considered as False
account_name = None
if account_name:
    print("Login successful!")
else:
    print("Please enter your account name!")
# Output: Please enter your account name!

# Only number 0 is considered as False
account_name = 0
if account_name:
    print("Login successful!")
else:
    print("Please enter your account name!")
# Output: Please enter your account name!

# Empty string is considered as False
account_name = ''
if account_name:
    print("Login successful!")
else:
    print("Please enter your account name!")
# Output: Please enter your account name!

# Empty dictionary is considered as False
account_name = {}
if account_name:
    print("Login successful!")
else:
    print("Please enter your account name!")
# Output: Please enter your account name!



