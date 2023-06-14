
try:
    f = open('corrupt_.txt')
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
# Output: test!
# Output: Executing Finally...
