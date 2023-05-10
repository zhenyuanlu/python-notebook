pets = ['Tub', 'Barkalot', 'Furrytail']
for pet in pets:
    print(pet)
# Output: Tub
# Output: Barkalot
# Output: Furrytail

# `break` statement
pets = ['Tub', 'Barkalot', 'Furrytail']
for pet in pets:
    if pet == 'Barkalot':
        print('We got Barkalot!')
        break
    print(pet)
# Output: Tub
# Output: We got Barkalot!

# `continue` statement skip the current iteration and continue with the next.
# Here we skip the `Barkalot` pet and print `We got Barkalot!` instead.
pets = ['Tub', 'Barkalot', 'Furrytail']
for pet in pets:
    if pet == 'Barkalot':
        print('We got Barkalot!')
        continue
    print(pet)
# Output: Tub
# Output: We got Barkalot!
# Output: Furrytail


for pet in pets:
    for letter in 'ab':
        print(letter, pet)
# Output: a Tub
# Output: b Tub
# Output: a Barkalot
# Output: b Barkalot
# Output: a Furrytail
# Output: b Furrytail


for pet in pets:
    for num in range(2):
        print(num, pet)
# Output: 0 Tub
# Output: 1 Tub
# Output: 0 Barkalot
# Output: 1 Barkalot
# Output: 0 Furrytail
# Output: 1 Furrytail


for num in range(0, 5):
    print(num)
# Output: 0
# Output: 1
# Output: 2
# Output: 3
# Output: 4

for num in range(0, 5, 2):
    print(num)
# Output: 0
# Output: 2
# Output: 4


num = 1
while num < 5:
    print(num)
    num += 1
# Output: 1
# Output: 2
# Output: 3
# Output: 4

num = 1
while num < 5:
    if num == 3:
        break
    print(num)
    num += 1
# Output: 1
# Output: 2

# `break` is very useful if you want to stop by certain condition in an infinite loop.
num = 1
while True:
    if num == 3:
        break
    print(num)
    num += 1
# Output: 1
# Output: 2

# Compare to `if` statement
num = 1
if num < 5:
    print(num)
    num += 1
# Output: 1













