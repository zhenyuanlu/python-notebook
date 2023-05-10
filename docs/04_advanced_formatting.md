# 4. Advanced Formatting
In Chapter 2, we have seen the basic string formatting. In this chapter, we will see some more advanced formatting examples upon on that.  

## 4.1. Formatting with placeholders
Let's see the following example first: 
```python title="Input"
species_1 = {'species': 'Tub', 'age': 5}
sentence = 'My name is ' + species_1['species'] + ' and I am ' + str(species_1['age']) + ' years old.'
print(sentence)
```
```title="Output"
My name is Tub and I am 5 years old.
```
We can see there are a lot of blank space we have to manually put in the beginning and the end of each string. 
We also have to cast the integer/number, `species_1['age']`, into strings by using `str()`. 

Of course, there is a better way to do this: 
```python title="Input"
sentence = 'My name is {} and I am {} years old.'.format(species_1['species'], species_1['age'])
print(sentence)
```
```title="Output"
My name is Tub and I am 5 years old.
```
We can see that we don't have to cast the integer/number into strings anymore.

We can also use the index of the placeholder to specify the order of the arguments:
```python title="Input"
sentence = 'My name is {0} and I am {1} years old.'.format(species_1['species'], species_1['age'])
print(sentence)
```
```title="Output"
My name is Tub and I am 5 years old.
```

This is another example using the index of the placeholder with repeated arguments:
```python title="Input"
tag = 'p'
text = 'This is a paragraph'
sentence = '<{0}>{1}</{0}>'.format(tag, text)
print(sentence)
```
```title="Output"
<p>This is a paragraph</p>
```

This is very useful when we have a placeholder that you want to reuse. Let's see another example:
```python title="Input"
sentence = 'My name is {0} and I am {1} years old. My friend Barkalot is also {1} years old.'.format(
    species_1['species'], species_1['age'])
print(sentence)
```
```title="Output"
My name is Tub and I am 5 years old. My friend Barkalot is also 5 years old.
``` 

There is another way to do this by using the key in the placeholder instead of the index:
```python title="Input"
sentence = 'My name is {0[species]} and I am {1[age]} years old.'.format(species_1, species_1)
print(sentence)
```
```title="Output"
My name is Tub and I am 5 years old.
```
Here, we call the value of the key `species` in the dictionary `species_1` by using `{0[species]}`.

But this is redundant because we have to repeat the same argument twice.

We can do the following instead:
```python title="Input"
sentence = 'My name is {0[species]} and I am {0[age]} years old.'.format(species_1)
print(sentence)
```
```title="Output"
My name is Tub and I am 5 years old.
```

We can also use the index of a list in the placeholder:
```python title="Input"
species = ['Tub', 'Furrytail', 'Cat', 'Barkalot']
sentence = 'I am {0[1]} and my friend is {0[3]}.'.format(species)
print(sentence)
```
```title="Output"
I am Furrytail and my friend is Barkalot.
```

We can also access the attributes of an object in the same way. For example, we define a class called `Species` that represents a species with a `species` and an `age`.
The class has an `__init__` method that initializes the instance variables species and age. We then create an instance of the `Species` class called `species_new` with the name 'Jerry' and the age `88`.

You then create an instance of the Species class called species_new with the name 'Jerry' and the age 88.
```python title="Input"
class Species:

    def __init__(self, species, age):
        self.species = species
        self.age = age

species_new = Species('Jerry', 88)
```
Now we can access the attributes of the object `species_new` by using the index of the placeholder:
```python title="Input"
sentence = 'My name is {0.species} and I am {0.age} years old.'.format(species_new)
print(sentence)
```
```title="Output"
My name is Jerry and I am 88 years old.
```
The string contains placeholders `{0.species}` and `{0.age}` which will be replaced by the species and age attributes of the `species_new` object. The `0` in the placeholders refers to the first argument passed to the `.format()` method, which is `species_new`.


This time, we are using keyword arguments to pass the values that will replace the placeholders in the string. The string contains placeholders `{species}` and `{age}`, which will be replaced by the values provided as keyword arguments in the `.format()` method.

```python title="Input"
sentence = 'My name is {species} and I am {age} years old.'.format(species='Jerry', age=88)
print(sentence)
```
```title="Output"
My name is Jerry and I am 88 years old.
```


## 4.2. `**` in `.format()

In the format() method, the ** operator can be used to unpack a dictionary that contains the keyword arguments for the placeholders in the string. This can be a convenient way to format a string using a dictionary that has keys matching the placeholders in the string.

Here's an example:
```python title="Input"
pet = {'species': 'Tub', 'age': 5}
sentence = 'My name is {species} and I am {age} years old.'.format(**pet)
print(sentence)
```
```title="Output"
My name is Tub and I am 5 years old.
```
In this example, we have a dictionary `pet` containing the keys `species` and `age`. We then use the `**` operator to unpack the dictionary when calling the `.format()` method on the string. The values from the dictionary are used to replace the placeholders in the string, resulting in the sentence `"My name is Tub and I am 5 years old."`

This method is useful when we print out the dictionaries, which is more readable.

!!! example "why use `**species` instead of `species`?"
    When you use `**` before a dictionary in a function call, like in the `.format()` method, it is known as dictionary unpacking. It allows you to pass the key-value pairs in the dictionary as named (keyword) arguments to the function.


When a dictionary is passed as a keyword argument in this way, the keys in the dictionary are treated as the parameter names and the corresponding values are passed as the parameter values.

So, in this case, the keys in the `pet` dictionary (`'species'` and `'age'`) are treated as parameter names in the sentence string, and their corresponding values (`'Tub'` and `5`) are passed as parameter values.

If you were to pass the pet dictionary without the double asterisks, like so:

```python title="Input"
sentence = 'My name is {species} and I am {age} years old.'.format(species)
print(sentence)
```
```title="Output"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'species'
```

The `.format()` method would be looking for a single argument that is a dictionary, rather than separate keyword arguments, and would raise a TypeError.


## 4.3. Formatting Numbers 

In this block, we are using the `.format()` method to insert values into a string. The `{}` serves as a placeholder for the value that will be inserted. The output will be a series of strings with the respective values from the loop.

```python title="Input"
for i in range(1, 6):
    sentence = 'The value is {}'.format(i)
    print(sentence)
```
```title="Output"
Output:
The value is 1
The value is 2
The value is 3
The value is 4
The value is 5
```

Padding with zeros (width 2): In this block, we're using the :02 format specifier within the placeholder to pad the value with zeros, ensuring a minimum width of 2 characters. This is useful for maintaining consistent formatting when dealing with numbers of varying lengths.
```python title="Input"
for i in range(1, 6):
    sentence = 'The value is {:02}'.format(i)
    print(sentence)
```
```title="Output"
Output:
The value is 01
The value is 02
The value is 03
The value is 04
The value is 05
```

Padding with zeros (width 3): Similarly, we can use the :03 format specifier to pad the value with zeros, ensuring a minimum width of 3 characters. This results in a more extensive padding for the smaller numbers, keeping the output format consistent.
```python title="Input"
for i in range(1, 6):
    sentence = 'The value is {:03}'.format(i)
    print(sentence)
```
```title="Output"
Output:
The value is 001
The value is 002
The value is 003
The value is 004
The value is 005
```

By using `:.2f` within the placeholder, we can format a floating-point number to display two decimal places.

```python title="Input"
# We can also use the `:.2f` with two decimal places
e = 2.71828
sentence = 'e is equal to {:.2f}'.format(e)
print(sentence)
```
```title="Output"
e is equal to 2.72
```

By using `:,` within the placeholder, we can format a number with a thousands separator, `,`. 
```python title="Input"

sentence = '1 KM is equal to {:,.2f} meters'.format(1000)
print(sentence)
```
```title="Output"
1 KM is equal to 1,000.00 meters
```

## 4.4. Formatting Date and Time with `datetime`
When formatting date and time, we can refer to the [strftime and strptime behavior](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior) for the format codes.

In the following code, we are using Python's `datetime` module to create a `datetime` object representing a specific date and time. We create a `datetime` object for `April 1, 2023, 10:10:30 AM`, and print it.
```python title="Input"
import datetime
today_date = datetime.datetime(2023, 4, 1, 10, 10, 30)
print(today_date)
```
```title="Output"
2023-04-01 10:10:30
```


We can use the `strftime` method to format the date in a more human-readable format. The `strftime` method allows you to create custom date and time formats by using format codes. We can use the `strftime` method to format the date. 

But we have to import the `datetime` module first. 

```python title="Input"
import datetime
today_date = datetime.datetime(2023, 4, 1, 10, 10, 30)
today_date = '{:%B %d, %Y}'.format(today_date)
print(today_date)
```
```title="Output"
April 01, 2023
```
Here, we use the format codes %B, %d, and %Y to display the full month name, the day of the month with a leading zero, and the year with the century, respectively. The resulting formatted date is passed to the format function and printed.


We can also use the `strptime` method to parse the string into a date:
```python title="Input"
import datetime
date_str = 'April 01, 2023'
today_date = datetime.datetime.strptime(date_str, '%B %d, %Y')
print(today_date)
```
```title="Output"
2023-04-01 00:00:00
```
n this example, we have the date string `'April 01, 2023'. The format codes used to parse this string are `%B`, `%d`, and `%Y`, which represent the full month name, the day of the month with a leading zero, and the year with the century, respectively. The strptime method reads the date string and creates a datetime object with the provided date information.
```python title="Input"
import datetime
today_date = datetime.datetime(2023, 4, 1, 10, 10, 30)
sentence = 'Today is {0:%B %d, %Y} on {0:%A}, and {0:%Y} has passed {0:%j} days'.format(today_date)
print(sentence)
```
```title="Output"
Today is April 01, 2023 on Thursday, and 2023 has passed 091 days
```

We can also use the `timetuple` method to remove the `0` in the beginning of `091`:
```python title="Input"
sentence = 'Today is {0:%B %d, %Y} on {0:%A}, and {0:%Y} has passed {1:d} days'.format(today_date, today_date.timetuple().tm_yday)
print(sentence)
```
```title="Output"
Today is April 01, 2023 on Thursday, and 2023 has passed 91 days
```
