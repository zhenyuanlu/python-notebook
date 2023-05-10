

# Global
x = 'global variable x'

# Instead of printing out y
def test():
    y = 'local variable y'
    print(x)

test()
print(x)
# Output: global variable x
# Output: global variable x

# print(y)
# Output: NameError: name 'y' is not defined



x = 'global variable x'
def test():
    x = 'local variable x'
    print(x)

test()
print(x)
# Output: local variable x
# Output: global variable x


# What if we want to set a new global x
x = 'global variable x'
def test():
    global x
    x = 'local variable x'
    print(x)

test()
print(x)
# Output: local variable x
# Output: local variable x

# You can also do the following
def test():
    global x
    x = 'local variable x'
    print(x)

test()
print(x)
# Output: local variable x
# Output: local variable x

# However, it's not recommended to use global often.

def test(z):
    print(z)

test('local variable z')
# print(z)
# Output: local variable z
# Output: NameError: name 'z' is not defined
