
try:
    f = open('test.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print('Executing Finally...')
# Output: test!
# Output: Executing Finally...
