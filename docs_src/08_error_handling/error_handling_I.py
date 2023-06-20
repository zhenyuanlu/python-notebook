# f = open('test_.txt')
# [Errno 2] No such file or directory: 'test_.txt'

try:
    f = open('test_.txt')
    var = not_exist_file # this will throw an error. Then the except block will be executed
except Exception:
    print('Sorry. Wrong File Name')
# Output: Sorry. Wrong File Name

