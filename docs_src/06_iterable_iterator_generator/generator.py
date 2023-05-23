# Generator
# Generator yields a series of values, but they don't store the values in memory
# It doesn't need __iter__() and __next__() methods

def iter_nums(start, end):
    current = start
    while current < end:
        yield current
        current +=1


nums = iter_nums(1, 5)
print(next(nums))
print(next(nums))
print(next(nums))
# Output: 1
# Output: 2
# Output: 3

# or use for loop
nums = iter_nums(1, 5)
for num in nums:
    print(num)
# Output: 1
# Output: 2
# Output: 3
# Output: 4

# Generator function is more readable than iterator class we created previously


# Another example
numbers = [1, 2, 3, 4, 5]

# Now we have a list of numbers, and we want to double each number in the list
def double_nums(nums):
    output = []
    for num in nums:
        output.append(num*2)
    return output

output_nums = double_nums(numbers)
print(output_nums)
# Output: [2, 4, 6, 8, 10]

# How to convert it to the generator function?
numbers = [1, 2, 3, 4, 5]
def double_nums(nums):
    for num in nums:
        yield num*2

output_nums = double_nums(numbers)
print(output_nums)
# As the generator doesn't store the values in memory
# You will get the generator object
# Output: <generator object double_nums at 0x000001E0F9F4B040>

# To get the values, you can use next() or for loop
# print(next(output_nums))
# ...

# Or output as a list:
print(list(output_nums))
# Output: [2, 4, 6, 8, 10]


# Of course you can also convert it to the list comprehension.
numbers = [1, 2, 3, 4, 5]
output_nums_list = [num*2 for num in numbers]
print(output_nums_list)
# Output: [2, 4, 6, 8, 10]

# If you replace the square brackets with the parentheses, you will get the generator object
output_nums_generator = (num*2 for num in numbers)
print(list(output_nums_generator))



