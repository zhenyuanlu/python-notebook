
try:
    f = open('test.txt')
    var = not_exist_file # this will throw an error.
except FileNotFoundError as e:
    print(e)
except NameError as e:
    print(e)
# Output: name 'not_exist_file' is not defined
