# 7. OOP
Object-oriented programming (OOP) is a programming paradigm based on the concept of "objects", which can contain data and code: data in the form of fields (often known as attributes), and code, in the form of procedures (often known as methods).

In Python, classes are used to create objects (instances), and each object can have attributes and behaviors. Let's dive into it with a simple example.

## 7.1. Classes and Instances

A Class is like an object constructor, or a "blueprint" for creating objects. In Python, we define a class using the class keyword.

Here when we say data and functions, we mean attributes and methods. The method here is associated with one class.


Let's create a simple class called `PetEmployee`.


```python title="Input"
class PetEmployee:
    pass
```

Python has a keyword pass that is used as a placeholder. It is syntactically needed for the code to be valid Python, but doesn't actually do anything. In this case, we're using it because we're declaring a class but don't want to put anything inside it yet.


The `PetEmployee` class doesn't currently have any attributes or methods. But it's still a valid class, and we can still create instances of it:

```python title="Input"
barkalot = PetEmployee()
furrytail = PetEmployee()
print(barkalot)
print(furrytail)
```
Here, barkalot and furrytail are instances of the PetEmployee class. When you print them, you'll see the memory address where these objects are stored in your machine's memory:

```python title="Output"
<__main__.Pet object at 0x0000020E4F6F4E80>
<__main__.Pet object at 0x0000020E4F6F4F10>
```
The output `<__main__.Pet object at 0x0000020E4F6F4E80>` is telling you that `barkalot` is an object of type `PetEmployee`, and it's at the memory location `0x0000020E4F6F4E80`. The specific memory address you see will be different every time you run the program.

These objects don't have any attributes or methods yet, but since they're different instances, they're not identical – they exist independently of each other in different parts of memory.

### 7.1.1. Attributes and __init__ method

The initial snippet shows us how we can add attributes to instances of a class. Here, we're manually adding attributes such as `name`, `age`, `species`, `email`, and `pay` to the instances barkalot and furrytail of the PetEmployee class. These attributes are just variables that are associated with each instance of the class.

```python title="Input"
barkalot.name = "Barkalot"
barkalot.age = 3
barkalot.species = "Dog"
barkalot.email = 'barkalot.dog@gmail.com'
barkalot.pay = 5

furrytail.name = "Furrytail"
furrytail.age = 2
furrytail.species = "Cat"
furrytail.email = 'furrytail.cat@gmail.com'
furrytail.pay = 11

print(barkalot.name)
print(furrytail.name)
```

```python title="Output"
Barkalot
Furrytail
```

However, this is not the most efficient way to set up our class. It's manual, repetitive, and prone to error (you might forget to initialize an attribute, or make a typo in the attribute name).


**`__init__` method**

The `__init__` method in Python is similar to constructors in other programming languages. It gets called when you create a new instance of a class. You can use it to set up attributes that every instance of the class should have when it gets created.

```python title="Input"
class PetEmployee:
    # Of course, you can use other names instead of self. But it is a convention to use self.
    def __init__(self, name, age, species, pay):
        self.name = name
        self.age = age
        self.species = species
        self.email = name + '.' + species + '@gmail.com'
        self.pay = pay
```
Here, `self` represents the instance of the class. By using the `self` keyword we can access the attributes and methods of the class in python.

When we create new `PetEmployee` instances, we now pass in the initial values for `name`, `age`, `species`, and `pay`:

```python title = "Input"
barkalot = PetEmployee('Barkalot', 3, 'Dog', 5)
furrytail = PetEmployee('Furrytail', 2, 'Cat', 11)
```

We can then access these attributes using dot notation:

```python title="Input"
print(barkalot.name)
print(furrytail.name)
```

```python title="Output"
Barkalot
Furrytail
```

This will print the names of `barkalot` and `furrytail`. The key thing to note here is that the name attribute for `barkalot` and `furrytail` are separate - changing the name attribute for `barkalot` won't affect `furrytail`'s name attribute, and vice versa.


### 7.1.2. Methods

A method is simply a function that is associated with an object. In the context of classes, methods often operate on data attributes of the class instances.


The first few lines show how to manually concatenate the `name` and `species` of a `PetEmployee` instance:

```python title="Input"
print('{} {}'.format(barkalot.name, barkalot.species))
```
```python title="Output"
Barkalot Dog
```

This works, but it would be more elegant and maintainable to define a method within the `PetEmployee` class to do this for us:


```python title="Class"
class PetEmployee:
    # Of course, you can use other names instead of self. But it is a convention to use self.
    def __init__(self, name, age, species, pay):
        self.name = name
        self.age = age
        self.species = species
        self.email = name + '.' + species + '@gmail.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.name, self.species)
```
This `fullname` method returns a string that is a concatenation of the `name` and `species` attributes of a `PetEmployee` instance. To call this method, you would use the following syntax:

```python title="Input"
barkalot = PetEmployee('Barkalot', 3, 'Dog', 5)
# we need the parenthesis here because fullname is a method not a attributes as the above
print(barkalot.fullname())
```
```python title="Output"
Barkalot Dog
```
Note the parentheses after `fullname`. This is because `fullname` is a method, not an attribute. If you forget the parentheses, Python will return the method itself, not the result of the method.

You can also call the method on the class, passing the instance as an argument:

```python title="Input"
print(PetEmployee.fullname(barkalot))
```
```python title="Output"
Barkalot Dog
```
In Python, instance methods need to have `self` as their first parameter so that they can access instance attributes and other instance methods. This is a Python convention. When you call a method on an object, Python automatically passes the object as the first argument. That's why you need to include `self` in the method definition.


**Why we need to put self in the method?**

If we don't put self in the method, we will get an error.

```python title="Input"
class PetEmployee:
    # Of course, you can use other names instead of self. But it is a convention to use self.
    def __init__(self, name, age, species, pay):
        self.name = name
        self.age = age
        self.species = species
        self.email = name + '.' + species + '@gmail.com'
        self.pay = pay

    def fullname():
        return '{} {}'.format(self.name, self.species)

barkalot = PetEmployee('Barkalot', 3, 'Dog', 5)
print(barkalot.fullname())
```
```python title="Output"
TypeError: fullname() takes 0 positional arguments but 1 was given
```

This is because when we call the method, the instance `barkalot` is passed as the first argument to the method.
