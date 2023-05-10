# LEBG
# Variable Scope

# Why is it in this order?

# Python searches for a variable in the following order:
# 1. Local
# 2. Enclosing
# 3. Global
# 4. Built-in


# Local

def test():
    y = 'local variable y'
    print(y)

test()
# Output = local variable y



