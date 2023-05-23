# Example for an iterator class

class NumIter:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        else:
            return_val = self.current
            self.current += 1
            return return_val


nums = NumIter(1, 5)
for num in nums:
    print(num)
# Output: 1
# Output: 2
# Output: 3
# Output: 4


# Here NumIter is an iterator, and it is also an iterable.

print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
# Output: 1
# Output: 2
# Output: 3