
try:
    f = open('corrupt.txt')
    if f.name == 'corrupt.txt':
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('Error!')
else:
    print(f.read())
    f.close()
finally:
    print('Executing Finally...')
# [Errno 2] No such file or directory: 'corrupt_.txt'
# Executing Finally...

