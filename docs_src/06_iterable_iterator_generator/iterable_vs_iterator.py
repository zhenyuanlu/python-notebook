# Iterable
# Iterable is an object, which one can iterate over. If one object have __iter__() method, then it is an iterable.
# You can use dir() to check if an object is iterable.

pets = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
for pet in pets:
    print(pet)
# Output: Tub
# Output: Furrytail
# Output: Cat
# Output: Barkalot

# Iterator is an object with state that remembers where it is during iteration.
# This means iterator object is iterable, but it doesn't mean that iterable object is always an iterator.
# The iterator object is initialized using the iter() method. It uses the next() method for iteration.
# Iterator can only go forward, and it cannot go backward.

pets = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
# print(next(pets))
# Output: TypeError: 'list' object is not an iterator
iterator_obj = pets.__iter__()
# Or a better way to do it is:
iterator_obj = iter(pets)
print(iterator_obj)
# Output: <list_iterator object at 0x000001E0F9F4B4C0>
print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj)) # This will raise StopIteration error
# Output: Tub
# Output: Furrytail
# Output: Cat
# Output: Barkalot
# Output: StopIteration

# This is kind of like a for loop, but it is more flexible.
# A similar way to do this is:

pets = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
iterator_obj = iter(pets)
while True:
    try:
        next_obj = next(iterator_obj)
        print(next_obj)
    except StopIteration:
        break

# Why this is important?





