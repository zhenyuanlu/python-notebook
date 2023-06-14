try:
    f = open('test.txt')
    var = not_exist_file # this will throw an error.
    # As the except block is specific, it will be executed as NameError
except FileNotFoundError:
    print('Sorry. Wrong File Name')
# OUtput: NameError: name 'not_exist_file' is not defined



try:
    f = open('test.txt')
    var = not_exist_file # this will throw an error.
except FileNotFoundError:
    print('Sorry. Wrong File Name')
except NameError:
    print('Sorry. Wrong File Name')
# Output: Sorry. Wrong File Name