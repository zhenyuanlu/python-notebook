
# Built-in
import builtins
# print(dir(builtins))

minimum = min([1,2,3])
print(minimum)
# Output: 1


# If we overwrite the built-in function min()
def min():
    pass

m = min([1,2,3])
# Output: TypeError: min() takes 0 positional arguments but 1 was given



# So the best way to do this is to use a different name instead of the default name min()
def find_min():
    pass

minimum = min([1,2,3])
print(minimum)
# Output: 1
