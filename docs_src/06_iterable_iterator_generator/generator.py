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
