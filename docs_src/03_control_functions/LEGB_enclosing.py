
# Enclosing


x = 'global variable x'
def outer():
    x = 'local-outer variable x'

    def inner():
        x = 'local-inner variable x'
        print(x) # 1st print

    inner() # 1st call for 1st print
    print(x) # 2nd print


outer() # 2nd call for 1st print and 2nd print
print(x) # 3rd print

# Output: local-inner variable x
# Output: local-outer variable x
# Output: global variable x


x = 'global variable x'
def outer():
    x = 'local-outer variable x'

    def inner():
        nonlocal x # Make our local-inner variable x to be the enclosing variable x
        x = 'local-inner variable x'
        print(x)

    inner()
    print(x)

outer()
print(x)

# Output: local-inner variable x
# Output: local-inner variable x
# Output: global variable x