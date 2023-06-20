# 7. Object-oriented programming
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
Here, barkalot and furrytail are instances of the PetEmployee class. When we print them, we'll see the memory address where these objects are stored in wer machine's memory:

```python title="Output"
<__main__.Pet object at 0x0000020E4F6F4E80>
<__main__.Pet object at 0x0000020E4F6F4F10>
```
The output `<__main__.Pet object at 0x0000020E4F6F4E80>` is telling we that `barkalot` is an object of type `PetEmployee`, and it's at the memory location `0x0000020E4F6F4E80`. The specific memory address we see will be different every time we run the program.

These objects don't have any attributes or methods yet, but since they're different instances, they're not identical – they exist independently of each other in different parts of memory.

### 7.1.1. Attributes and __init__ method

The initial snippet shows us how we can add attributes to instances of a class. Here, we're manually adding attributes such as `name`, `age`, `species`, `email`, and `level` to the instances barkalot and furrytail of the PetEmployee class. These attributes are just variables that are associated with each instance of the class.

```python title="Input"
barkalot.name = "Barkalot"
barkalot.age = 3
barkalot.species = "Dog"
barkalot.email = 'barkalot.dog@gmail.com'
barkalot.level = 5

furrytail.name = "Furrytail"
furrytail.age = 2
furrytail.species = "Cat"
furrytail.email = 'furrytail.cat@gmail.com'
furrytail.level = 11

print(barkalot.name)
print(furrytail.name)
```

```python title="Output"
Barkalot
Furrytail
```

However, this is not the most efficient way to set up our class. It's manual, repetitive, and prone to error (we might forget to initialize an attribute, or make a typo in the attribute name).


**`__init__` method**

The `__init__` method in Python is similar to constructors in other programming languages. It gets called when we create a new instance of a class. we can use it to set up attributes that every instance of the class should have when it gets created.

```python title="Input"
class PetEmployee:
    # Of course, we can use other names instead of self. But it is a convention to use self.
    def __init__(self, name, age, species, level):
        self.name = name
        self.age = age
        self.species = species
        self.email = name + '.' + species + '@gmail.com'
        self.level = level
```
Here, `self` represents the instance of the class. By using the `self` keyword we can access the attributes and methods of the class in python.

When we create new `PetEmployee` instances, we now pass in the initial values for `name`, `age`, `species`, and `level`:

```python title="Input"
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
    # Of course, we can use other names instead of self. But it is a convention to use self.
    def __init__(self, name, age, species, level):
        self.name = name
        self.age = age
        self.species = species
        self.email = name + '.' + species + '@gmail.com'
        self.level = level

    def fullname(self):
        return '{} {}'.format(self.name, self.species)
```
This `fullname` method returns a string that is a concatenation of the `name` and `species` attributes of a `PetEmployee` instance. To call this method, we would use the following syntax:

```python title="Input"
barkalot = PetEmployee('Barkalot', 3, 'Dog', 5)
# we need the parenthesis here because fullname is a method not a attributes as the above
print(barkalot.fullname())
```
```python title="Output"
Barkalot Dog
```
Note the parentheses after `fullname`. This is because `fullname` is a method, not an attribute. If we forget the parentheses, Python will return the method itself, not the result of the method.

we can also call the method on the class, passing the instance as an argument:

```python title="Input"
print(PetEmployee.fullname(barkalot))
```
```python title="Output"
Barkalot Dog
```
In Python, instance methods need to have `self` as their first parameter so that they can access instance attributes and other instance methods. This is a Python convention. When we call a method on an object, Python automatically passes the object as the first argument. That's why we need to include `self` in the method definition.


**Why we need to put self in the method?**

If we don't put self in the method, we will get an error.

```python title="Input"
class PetEmployee:
    # Of course, we can use other names instead of self. But it is a convention to use self.
    def __init__(self, name, age, species, level):
        self.name = name
        self.age = age
        self.species = species
        self.email = name + '.' + species + '@gmail.com'
        self.level = level

    def fullname():
        return '{} {}'.format(self.name, self.species)

barkalot = PetEmployee('Barkalot', 3, 'Dog', 5)
print(barkalot.fullname())
```
```python title="Output"
TypeError: fullname() takes 0 positional arguments but 1 was given
```

This is because when we call the method, the instance `barkalot` is passed as the first argument to the method.


## 7.2. Class and Instance Variables

Class variables and instance variables are the two types of variables that we can define in a Python class. Both are useful in different scenarios, and understanding them is crucial for effective object-oriented programming in Python.

**Instance Variables**: Instance variables are associated with instances of the class. This means that for each object or instance of a class, the instance variables are different. Instance variables are defined within methods and are prefixed with the self keyword. They are useful when the value of a variable may differ from one instance of a class to another. For example, in a PetEmployee class, each pet will have a unique name, age, and species, so these would be instance variables.

**Class Variables**: Class variables are variables that are shared among all instances of a class. They are not defined inside any methods, and they don't have the self prefix. Class variables are useful when we want a variable to be the same for every instance of a class. For example, if we wanted to apply a uniform promotion increment to all PetEmployee instances, we might define a class variable like promotion_increment = 1.

In summary, class variables are shared by all instances of a class, while instance variables can have different values for each class instance. Knowing when to use class variables versus instance variables is essential for creating efficient and organized code in Python.


### 7.2.1. Instance Variables

Let's add some instance variables to our `PetEmployee` class. We'll add `level` instance variable to the `PetEmployee` class, and we'll set them to the values passed in when the instance is created:

```python title="Input"
class PetEmployee:
    def __init__(self, name, age, species, level):
        self.name = name
        self.age = age
        self.species = species
        self.email = name + '.' + species + '@gmail.com'
        self.level = level

    def fullname(self):
        return '{} {}'.format(self.name, self.species)

    def apply_promotion(self):
        # Apply promotion to the level of the pet employee
        self.level = self.level + 1
```

In this code, a class named `PetEmployee` is created, which has data attributes such as `name`, `age`, `species`, `email`, and `level`. It also includes two methods: `fullname` and `apply_promotion`. 

The `fullname` method returns a formatted string that concatenates the `name` and `species` attributes of the `PetEmployee` instance, as previously explained.

The `apply_promotion` method increases the `level` attribute of the `PetEmployee` instance by 1. In this context, we might consider `level` as an indication of the employee's rank or position - as the `apply_promotion` method is called, the `level` attribute increases, signifying a promotion.

Here's a walkthrough of what happens when the script is run:

1. Two instances of `PetEmployee` are created, `barkalot` and `furrytail`, with the given attributes.

2. The `level` attribute of the `barkalot` instance is printed out, which shows 3 as per the initial data given at instance creation.

3. The `apply_promotion` method is then called on the `barkalot` instance, which increments `barkalot`'s `level` attribute by 1.

4. Printing `barkalot.level` now shows 4, confirming that the `apply_promotion` method has successfully incremented the `level`.

!!! info "`self`"

    Of course, we can use other names instead of `self`. But it is a convention to use `self`.

```python title="Input"
barkalot = PetEmployee('Barkalot', 3, 'Dog', 3)
furrytail = PetEmployee('Furrytail', 2, 'Cat', 5)

print(barkalot.level)
barkalot.apply_promotion()
print(barkalot.level)
```
```python title="Output"
3
4
```


### 7.2.2. Class Variables

What if we want to change the promotion rate? We don't want to change the promotion rate for each instance mannually.


We can use class variable to do this.

```python title="Input"
class PetEmployee:
    # Class variable
    promotion_rate = 1
    def __init__(self, name, age, species, level):
        self.name = name
        self.age = age
        self.species = species
        self.email = name + '.' + species + '@gmail.com'
        self.level = level

    def fullname(self):
        return '{} {}'.format(self.name, self.species)

    def apply_promotion(self):
        # We need to use the class name to access the class variable
        # This can be either self
        # or PetEmployee.promotion_rate
        self.level = self.level + self.promotion_rate 
```

In the revised `PetEmployee` class, a class variable `promotion_rate` is introduced. Class variables are variables that are shared across all instances of the class - unlike instance variables, which can have different values for each instance. 

In this case, `promotion_rate` determines how much an employee's `level` will increase each time the `apply_promotion` method is called. Since it's a class variable, changing `promotion_rate` will affect all instances of `PetEmployee`, not just one.

The `apply_promotion` method is adjusted to use `self.promotion_rate` when increasing the `level` attribute. The `self` keyword ensures that the instance refers to the class variable, not a potential instance variable of the same name. This way, if `promotion_rate` is changed for the `PetEmployee` class, all instances will use the new rate when `apply_promotion` is called.

In this current setting, calling `apply_promotion` on either `barkalot` or `furrytail` will increment their `level` attribute by 1, as the `promotion_rate` is set to 1.



```python title="Input"
barkalot = PetEmployee('Barkalot', 3, 'Dog', 3)
furrytail = PetEmployee('Furrytail', 2, 'Cat', 5)
# How to understand this?
# Here we print out the promotion rate of the class and the instance.
# The promotion rate of the instance is the same as the class.
print(PetEmployee.promotion_rate)
print(barkalot.promotion_rate)
print(furrytail.promotion_rate)
```
```python title="Output"
1
1
1
```


!!! info "The Sequence of Attribute Lookup"

    When we access the attribute of an instance, it will first check if the instance has the attribute.

    If not, it will check if the class has the attribute.

    If not, it will check if the parent class has the attribute.

    Here, the instance doesn't have the promotion_rate attribute, so it will check the class.

    The class has the promotion_rate attribute, so it will use the class attribute.

When we first create the `barkalot` and `furrytail` instances, they don't have an instance variable called `promotion_rate`. So when we try to access `barkalot.promotion_rate` or `furrytail.promotion_rate`, Python doesn't find the attribute in the instance's `__dict__`. In this case, Python falls back to the class (`PetEmployee`) and checks if `PetEmployee` has an attribute `promotion_rate`, which it does.

Now let's lookup the `__dict__` attribute of the class and the instance.

```python title="Input"
print(barkalot.__dict__)
print(PetEmployee.__dict__)
```
```python title="Output"
{'name': 'Barkalot', 'age': 3, 'species': 'Dog', 'email': 'Barkalot.Dog@gmail.com', 'level': 3}
{'__module__': '__main__', 'promotion_rate': 1, '__init__': <function PetEmployee.__init__ at 0x000001B8AD52D940>, ...}
```
The output contains the attribute `promotion_rate` for the class PetEmployee.

When we modify the `promotion_rate` attribute of the `PetEmployee` class, it affects both `barkalot` and `furrytail` because they fall back to the class attribute when their own `promotion_rate` attribute is not found.

```python title="Input"
PetEmployee.promotion_rate = 2
print(PetEmployee.promotion_rate)
print(barkalot.promotion_rate)
print(furrytail.promotion_rate)
```
```python title="Output"
2
2
2
```

However, when we set `barkalot.promotion_rate = 3`, we're creating an instance attribute `promotion_rate` specific to `barkalot`. Now when we try to access `barkalot.promotion_rate`, Python finds it in the `barkalot` instance's `__dict__` and doesn't need to fall back to the class attribute. Therefore, `barkalot.promotion_rate` shows `3`, while `furrytail.promotion_rate` and `PetEmployee.promotion_rate` still show `2`.

```python title="Input"
barkalot.promotion_rate = 3
print(PetEmployee.promotion_rate)
print(barkalot.promotion_rate)
print(furrytail.promotion_rate)
```
```python title="Output"
2
3
2
```
Also check `__dict__` again.

```python title="Input"
print(barkalot.__dict__)
```
```python title="Output"
{'name': 'Barkalot', 'age': 3, 'species': 'Dog', 'email': 'Barkalot.Dog@gmail.com', 'level': 3, 'promotion_rate': 3}
```

This demonstrates how class variables and instance variables in Python work and the difference between them. Class variables are shared among all instances of a class unless specifically overridden within an instance, as we did with `barkalot`.


Here we introduce an extra usage of class variables: counting the number of instances (objects) created for a class. This is handy if we want to keep track of how many pet employees we've hired so far. I can imagine the HR department being pretty grateful for this feature. (I mean, it would be quite embarrassing if they lost track of how many pets they've hired, right?)

### 7.2.3. Example
!!! example "Counting the Number of Instances"

    Here we want to count the number of employees when we create a new emplyee instance.

    ```python title="Input"
    # Here we want to count the number of employees when we create a new emplyee instance.
    class PetEmployee:
        # Class variable
        num_of_pet_employees = 0
        promotion_rate = 1

        def __init__(self, name, age, species, level):
            self.name = name
            self.age = age
            self.species = species
            self.email = name + '.' + species + '@gmail.com'
            self.level = level

            PetEmployee.num_of_pet_employees += 1

        def fullname(self):
            return '{} {}'.format(self.name, self.species)

        def apply_promotion(self):
            # We need to use the class name to access the class variable
            # This can be either self or PetEmployee
            self.level = self.level + self.promotion_rate
    ```
    In this iteration of `PetEmployee`, we introduce a new class variable: `num_of_pet_employees`. This variable is incremented each time a new `PetEmployee` instance is created, thanks to the magic line `PetEmployee.num_of_pet_employees += 1` in the `__init__` method. Remember, `__init__` is called each time we instantiate a new object, making it the perfect place to keep count of our newly employed pets.

    Here's how it works:
    ```python title="Input"
    print(PetEmployee.num_of_pet_employees)
    ```
    ```python title="Output"
    0
    ```
    We haven't created any instances of `PetEmployee` yet, so our pet employee count is a big, fat zero. HR is twiddling their thumbs, waiting for some action.

    ```python title="Input"
    barkalot = PetEmployee('Barkalot', 3, 'Dog', 3)
    furrytail = PetEmployee('Furrytail', 2, 'Cat', 5)
    ```
    Hold onto your hats, HR, we just employed two new pets! `barkalot` and `furrytail` join the team, and `PetEmployee.num_of_pet_employees` is incremented each time, thanks to our handy `__init__` method.
            
    ```python title="Input" 
    print(PetEmployee.num_of_pet_employees)
    ```
    ```python title="Output"
    2
    ```
    Voila! HR breathes a sigh of relief. They didn't have to count on their paws - our class variable did the job for them.

This example showcases how a class variable can be used as a handy counter for all instances of a class. It's one of those Python tricks that makes your life as a developer easier and helps you keep track of the state of your program.

### 7.2.4. Exercise

Let's go one step further and imagine a scenario where HR wants to know which species they've employed most. Here's a little exercise for you: Can you modify our `PetEmployee` class to keep track of how many Dogs and Cats they've hired? (Hint: You might want to use a dictionary as a class variable!) 

!!! tip "Which Pet Employee Species Do We Have the Most Of?"

    === "Skeleton"
        ```python title="Input"
        class PetEmployee:
            num_of_pet_employees = 0
            species_count = {}
            promotion_rate = 1

            def __init__(self, name, age, species, level):
                self.name = name
                self.age = age
                self.species = species
                self.email = name + '.' + species + '@gmail.com'
                self.level = level

                PetEmployee.num_of_pet_employees += 1

                # Updating species count
                # Your code here

            def fullname(self):
                return '{} {}'.format(self.name, self.species)

            def apply_promotion(self):
                self.level = self.level + self.promotion_rate
        ``` 

    === "Solution"
    
        ```python title="Input"
        class PetEmployee:
            num_of_pet_employees = 0
            species_count = {}
            promotion_rate = 1

            def __init__(self, name, age, species, level):
                self.name = name
                self.age = age
                self.species = species
                self.email = name + '.' + species + '@gmail.com'
                self.level = level

                PetEmployee.num_of_pet_employees += 1

                # Updating species count
                if species in PetEmployee.species_count:
                    PetEmployee.species_count[species] += 1
                else:
                    PetEmployee.species_count[species] = 1

            def fullname(self):
                return '{} {}'.format(self.name, self.species)

            def apply_promotion(self):
                self.level = self.level + self.promotion_rate
        ```
        Now, each time a `PetEmployee` is created, `species_count` is updated. Let's create some instances and see how it works:
        ```python title="Input"
        barkalot = PetEmployee('Barkalot', 3, 'Dog', 3)
        furrytail = PetEmployee('Furrytail', 2, 'Cat', 5)
        mewton = PetEmployee('Mewton', 4, 'Cat', 7)
        ```
        ```python title="Input"
        print(PetEmployee.species_count)
        ```
        ```python title="Output"
        {'Dog': 1, 'Cat': 2}
        ```



## 7.3. Classmethods and Staticmethods

Alright, let's dive into the magical world of Python's `classmethods` and `staticmethods`!

In addition to instance methods, which operate on individual objects (or "instances"), Python classes can also have `classmethods` and `staticmethods`. 

We'll kick things off by looking at `classmethods`.

### 7.3.1. Classmethods 

To create a class method in Python, we use the `@classmethod` decorator and the special `cls` parameter, which points to the class, not the instance of the object.

In our example code, we have a class `PetEmployee` with a class variable `promotion_rate`. Let's dive into the details:

```python title="Input"
class PetEmployee:
    # Class variable
    promotion_rate = 1

    def __init__(self, name, age, species, level):
        self.name = name
        self.age = age
        self.species = species
        self.email = name + '.' + species + '@gmail.com'
        self.level = level

    def fullname(self):
        return '{} {}'.format(self.name, self.species)

    def apply_promotion(self):
        # We need to use the class name to access the class variable
        # This can be either self or PetEmployee
        self.level = self.level + self.promotion_rate

    @classmethod
    def set_promotion_rate(cls, rate):
        cls.promotion_rate = rate
```

Here, we have the `set_promotion_rate` class method. This method changes the `promotion_rate` for all instances of the class, not just for one instance. 

So, if we have two pet employees, Barkalot and Furrytail:

```python title="Input"
barkalot = PetEmployee('Barkalot', 3, 'Dog', 3)
furrytail = PetEmployee('Furrytail', 2, 'Cat', 5)
```

And we print their `promotion_rate`, we get `1` for both as the class variable `promotion_rate` is set to `1`:

```python title="Input"
print(PetEmployee.promotion_rate)
print(barkalot.promotion_rate)
print(furrytail.promotion_rate)
```
```python title="Output"
1
1
1
```

But what happens if we change the `promotion_rate` using the `set_promotion_rate` class method? 

```python title="Input"
PetEmployee.set_promotion_rate(2)
```

Boom! The promotion rate changes for both Barkalot and Furrytail. That's the power of class methods:

```python title="Input"
print(PetEmployee.promotion_rate)
print(barkalot.promotion_rate)
print(furrytail.promotion_rate)
```
```python title="Output"
2
2
2
```

**Classmethods as Alternative Constructors**

Classmethods are also commonly used as alternative constructors. This means they can provide additional ways to create objects.

For instance, suppose we have pet employee data as a hyphen-separated string. We can use a class method to parse this string and create a new `PetEmployee` object. 

```python title="Input"
@classmethod
def from_string(cls, emp_str):
    name, age, species, level = emp_str.split('-')
    return cls(name, age, species, level)
```

And we can easily create a new `PetEmployee` using this new class method:

```python title="Input"
barkalot_str = 'Barkalot-3-Dog-3'
furrytail_str = 'Furry

barkalot = PetEmployee.from_string(barkalot_str)
furrytail = PetEmployee.from_string(furrytail_str)

print(barkalot.fullname())
```
```python title="Output"
Barkalot Dog
```

With one line of code, we've turned a string into a full-fledged `PetEmployee` object! Who's a good boy? `classmethod`, you're a good boy!

Now, we've tackled class methods like pros. Let's tease apart static methods, shall we?

### 7.3.2. Staticmethods

Static methods don't access or modify any instance or class data. They're more like handy utility functions we bundle with the class. They're defined using the `@staticmethod` decorator.

```python title="Input"
class PetEmployee:
    # Class variable
    promotion_rate = 1

    def __init__(self, name, age, species, level):
        self.name = name
        self.age = age
        self.species = species
        self.email = name + '.' + species + '@gmail.com'
        self.level = level

    def fullname(self):
        return '{} {}'.format(self.name, self.species)

    def apply_promotion(self):
        # We need to use the class name to access the class variable
        # This can be either self or PetEmployee
        self.level = self.level + self.promotion_rate

    @classmethod
    def set_promotion_rate(cls, rate):
        cls.promotion_rate = rate

    @classmethod
    def from_string(cls, emp_str):
        name, age, species, level = emp_str.split('-')
        return cls(name, age, species, level)

    @staticmethod
    def is_walking_pet_today(day):
        if day.weekday() == 6:
            return 'Yaay! It\'s time to walk the pets!'
        return 'Sorry, you have to get back to work!'
```

Let's update our `PetEmployee` class with a static method that checks if `is_walking_pet_today`:

```python title="Input"
@staticmethod
def is_walking_pet_today(day):
    if day.weekday() == 6:
        return 'Yaay! It\'s time to walk the pets!'
    return 'Sorry, you have to get back to work!'
```

```python title="Input"
barkalot = PetEmployee('Barkalot', 3, 'Dog', 3)
furrytail = PetEmployee('Furrytail', 2, 'Cat', 5)
```

This method doesn't rely on any specific instance or class variable, making it a perfect candidate for a static method. It takes in a date and checks if it's a Sunday (weekday `6`). If so, it returns a cheerful message encouraging pet walks. Otherwise, it sadly informs you to get back to work. No fun!

We can call this static method without any instance, just by using the class name:
```python title="Input"
import datetime
today_date = datetime.date.today()
print(PetEmployee.is_walking_pet_today(today_date))
```
```python title="Output"
Yaay! It's time to walk the pets!
```

This block of code imports the `datetime` module, gets today's date, and then checks if it's a pet walking day according to our `PetEmployee` guidelines. 

One minor correction I'd like to point out is that the output wouldn't be `False`, but rather one of the two strings our method returns: `'Yaay! It's time to walk the pets!'` or `'Sorry, you have to get back to work!'`, depending on the day of the week.



## 7.4. Inheritance
Inheritance allows us to create a new class using details of an existing class without modifying it. This is like saying, "Hey, I like what you've done here. I'll take it, and add a little sprinkle of my own magic."

### 7.4.1. Creating Subclasses

```python title="Initial Class Setup"
class PetEmployee:
    # Class variable
    promotion_rate = 1

    def __init__(self, name, age, species, level):
        self.name = name
        self.age = age
        self.species = species
        self.email = name + '.' + species + '@gmail.com'
        self.level = level

    def fullname(self):
        return '{} {}'.format(self.name, self.species)

    def apply_promotion(self):
        # We need to use the class name to access the class variable
        # This can be either self or PetEmployee
        self.level = self.level + self.promotion_rate
```

In our example, we're creating a new class `PetDataScientist` that inherits from our existing `PetEmployee` class:

```python title="Input"
# Subclass of PetEmployee
class PetDataScientist(PetEmployee):
    pass
```

Here, `pass` is a placeholder because Python expects an indented block for classes. It says, "I don't want to add anything new in this class, just use everything from `PetEmployee`."

So, when we create `PetDataScientist` instances, they have access to the same attributes and methods as `PetEmployee` instances:

```python title="Input"
barkalot = PetDataScientist('Barkalot', 3, 'Dog', 3)
furrytail = PetDataScientist('Furrytail', 2, 'Cat', 5)

print(barkalot.email)
print(furrytail.email)
```

```python title="Output"
Barkalot.Dog@gmail.com
Furrytail.Cat@gmail.com
```

You can see that `barkalot` and `furrytail`, even though they're data scientist pets (probably discussing the latest in machine learning algorithms), have emails formatted the same way as any `PetEmployee`. That's inheritance in action!

One cool feature Python provides is the `help` function. This function displays important details about a class, including its Method Resolution Order (MRO). The MRO is the order in which Python looks for a method in a hierarchy of classes. Here, it tells us that when looking for a method, Python first checks `PetDataScientist`, then `PetEmployee`, and finally the built-in `object` class that every class implicitly inherits from:

```python title="Input"
print(help(PetDataScientist))
```
```python title="Output"
Method resolution order:
 |      PetDataScientist
 |      PetEmployee
 |      builtins.object
```

This is just the tip of the inheritance iceberg, and there's so much more to explore. If you're up for it, why don't we add some unique methods to our `PetDataScientist` class? Maybe a method to analyze data (just pretend data for now) or to present findings? Let your imagination run wild!


Now let's create a functional subclass of `PetEmployee` named `PetDataScientist`:



=== "Child Class - PetDataScientist"
    ```python title="Input"
    class PetDataScientist(PetEmployee):
        promotion_rate = 2
    ```

=== "Parent Class - PetEmployee"
    ```python title="Initial Class Setup"
    class PetEmployee:
        # Class variable
        promotion_rate = 1

        def __init__(self, name, age, species, level):
            self.name = name
            self.age = age
            self.species = species
            self.email = name + '.' + species + '@gmail.com'
            self.level = level

        def fullname(self):
            return '{} {}'.format(self.name, self.species)

        def apply_promotion(self):
            # We need to use the class name to access the class variable
            # This can be either self or PetEmployee
            self.level = self.level + self.promotion_rate
    ```



In this piece of code, we redefine `promotion_rate` for our `PetDataScientist` class, effectively overriding the `promotion_rate` of `PetEmployee` class. You can think of it as saying, "PetEmployee, you did a good job with the promotion rate, but we data scientist pets need it to be a bit faster. So we'll take it from here."

Now when a `PetDataScientist` applies for a promotion:

```python title="Input"
barkalot = PetDataScientist('Barkalot', 3, 'Dog', 3)
print(barkalot.level)
barkalot.apply_promotion()
print(barkalot.level)
```

```python title="Output"
3
5
```


Barkalot, the data scientist dog (which is honestly the cutest mental image), receives a promotion of 2 levels, unlike regular `PetEmployee`s who only advance by 1. The reason is that when `apply_promotion()` is called, it uses `PetDataScientist`'s `promotion_rate`, not `PetEmployee`'s.

This little example shows the power of inheritance. By changing just one line in the subclass, we've changed the behavior of a method inherited from the superclass without having to rewrite the entire method!

### 7.4.2. Overriding Methods

Barkalot and Furrytail are stepping up their game! Not only are they data scientists, but they also have their favorite programming languages now. Let's see how you've accomplished this:


=== "Child Class - PetDataScientist"
    ```python title="Input"
    class PetDataScientist(PetEmployee):
        promotion_rate = 2

        def __init__(self, name, age, species, level, language):
            super().__init__(name, age, species, level)
            self.language = language
    ```

=== "Parent Class - PetEmployee"
    ```python title="Initial Class Setup"
    class PetEmployee:
        # Class variable
        promotion_rate = 1

        def __init__(self, name, age, species, level):
            self.name = name
            self.age = age
            self.species = species
            self.email = name + '.' + species + '@gmail.com'
            self.level = level

        def fullname(self):
            return '{} {}'.format(self.name, self.species)

        def apply_promotion(self):
            # We need to use the class name to access the class variable
            # This can be either self or PetEmployee
            self.level = self.level + self.promotion_rate
    ```

In this code, you have overridden the `__init__` method in the `PetDataScientist` subclass. You've added a new parameter `language` to keep track of the favorite programming language of our data scientist pets.

The magic happens in this line: `super().__init__(name, age, species, level)`. The `super()` function is like a time machine that brings us to the parent class, `PetEmployee` in this case. When we call `super().__init__(name, age, species, level)`, it executes the `__init__` method from `PetEmployee`, initializing the common attributes.

Then we come back to the future (or the `PetDataScientist` class) and add the new attribute `language`.

```python title="Input"
ds_barkalot = PetDataScientist('Barkalot', 3, 'Dog', 3, 'Python')
ds_furrytail = PetDataScientist('Furrytail', 2, 'Cat', 5, 'Mojo')
print(ds_barkalot.language)
```

```python title="Output"
'Python'
```

When we create a `PetDataScientist` instance like `ds_barkalot`, we can now provide a programming language. Barkalot prefers Python, just like us!

Inheritance and overriding allow us to extend and modify behavior without disturbing the existing class. Quite neat, isn't it? 


**One more child class - PetLeader**

Let's dive into the marvelous world of team management.

=== "Child Class - PetLeader"
    ```python title="Input"
    class PetLeader(PetEmployee):
        promotion_rate = 1

        def __init__(self, name, age, species, level, team=None):
            super().__init__(name, age, species, level)
            if team is None:
                self.team = []
            else:
                self.team = team

        def add_team_member(self, employee):
            if employee not in self.team:
                self.team.append(employee)

        def remove_team_member(self, employee):
            if employee in self.team:
                self.team.remove(employee)

        def print_team(self):
            for employee in self.team:
                print(' ', employee.fullname())
    ```

=== "Child Class - PetDataScientist"
    ```python title="Input"
    class PetDataScientist(PetEmployee):
        promotion_rate = 2

        def __init__(self, name, age, species, level, language):
            super().__init__(name, age, species, level)
            self.language = language
    ```

=== "Parent Class - PetEmployee"
    ```python title="Initial Class Setup"
    class PetEmployee:
        # Class variable
        promotion_rate = 1

        def __init__(self, name, age, species, level):
            self.name = name
            self.age = age
            self.species = species
            self.email = name + '.' + species + '@gmail.com'
            self.level = level

        def fullname(self):
            return '{} {}'.format(self.name, self.species)

        def apply_promotion(self):
            # We need to use the class name to access the class variable
            # This can be either self or PetEmployee
            self.level = self.level + self.promotion_rate
    ```

Here, you've introduced a new subclass `PetLeader` that inherits from `PetEmployee`. It includes a new instance variable `team`, which is a list of `PetEmployee` objects. A `PetLeader` has the ability to manage a team, adding and removing team members with the `add_team_member()` and `remove_team_member()` methods, respectively. They can also print their team with the `print_team()` method, showing us the full names of their team members.

Then you've created some instances and made Barkalot a leader:

```python title="Input"
ds_barkalot = PetDataScientist('Barkalot', 3, 'Dog', 3, 'Python')
ds_furrytail = PetDataScientist('Furrytail', 2, 'Cat', 5, 'Mojo')

manager_whiskers = PetLeader('Whiskers', 5, 'Cat', 5, [ds_barkalot])
manager_whiskers.print_team()
```
```python title="Output"
Barkalot Dog
```
Add furrytail to Barkalot's team:

```python title="Input"
manager_barkalot.add_team_member(ds_furrytail)
manager_barkalot.print_team()
```
```python title="Output"
 Barkalot Dog
 Furrytail Cat
```

You've shown us how `isinstance()` and `issubclass()` functions work. `isinstance()` checks if an object is an instance of a class or its subclasses, while `issubclass()` checks if a class is a subclass of another. It's like an identity card for our classes and objects.

```python title="Input"
print(isinstance(manager_whiskers, PetLeader))
print(isinstance(manager_whiskers, PetDataScientist))
```
```python title="Output"
True
False
```

```python title="Input"
print(issubclass(PetLeader, PetEmployee))
print(issubclass(PetDataScientist, PetLeader))
```
```python title="Output"
True
False
```

These tools can be handy when we want to verify the relationships between objects and classes.

Now that we've got a manager, perhaps we could consider a task or project class for the team to work on. What do you think?


## 7.5. Polymorphism

Ah, polymorphism! The magical concept in object-oriented programming that allows objects to take on many forms. It's like our pets morphing into different roles in the company at runtime!

First, we need to understand what polymorphism is. It refers to the ability of an object to behave in multiple ways. This comes from Greek, where 'poly' means 'many', and 'morph' means 'form'. In programming, it's the ability of a function or a method to behave differently based on the object that calls it.

Let's use our `PetEmployee`, `PetDataScientist`, and `PetLeader` classes to illustrate the concept.

```python title="Input"
class PetEmployee:
    promotion_rate = 1

    def __init__(self, name, age, species, level):
        self.name = name
        self.age = age
        self.species = species
        self.email = name + '.' + species + '@gmail.com'
        self.level = level

    def fullname(self):
        return '{} {}'.format(self.name, self.species)

    def apply_promotion(self):
        self.level = self.level + self.promotion_rate

    def daily_duty(self):
        return "Work! Work! Work!"

class PetDataScientist(PetEmployee):
    promotion_rate = 2

    def __init__(self, name, age, species, level, language):
        super().__init__(name, age, species, level)
        self.language = language

    def daily_duty(self):
        return "Importing data, analyzing data, and drinking coffee"

class PetLeader(PetEmployee):
    promotion_rate = 1

    def __init__(self, name, age, species, level, team=None):
        super().__init__(name, age, species, level)
        if team is None:
            self.team = []
        else:
            self.team = team

    def daily_duty(self):
        return "Managing team and setting goals"

def pet_daily_duty(pet):
    print(pet.daily_duty())
```

```python title="Input"
emp_barkalot = PetEmployee('Barkalot', 3, 'Dog', 3)
ds_furrytail = PetDataScientist('Furrytail', 2, 'Cat', 5, 'Python')
manager_whiskers = PetLeader('Whiskers', 5, 'Cat', 5)

pets = [emp_barkalot, ds_furrytail, manager_whiskers]

for pet in pets:
    pet_daily_duty(pet)
```

```python title="Output"
Work! Work! Work!
Importing data, analyzing data, and drinking coffee
Lead team and setting goals
```

The `daily_duty()` method has different implementations in the `PetEmployee`, `PetDataScientist`, and `PetLeader` classes. When we call `daily_duty()` on an object, the appropriate method is selected based on the object's class, not the type of the variable that is used to call the method. This is a classic example of polymorphism.

!!! tip "`raise` keyword"
    In Python, `raise` is a keyword that's used to generate exceptions. By invoking `raise`, you're signaling to Python that an error has occurred, and you're asking Python to stop the normal execution of your program and instead, to "throw" an error that needs to be caught and handled.

    Now, let's talk about `NotImplementedError`. This is a special type of exception that we raise when we have a method or function that is supposed to be implemented by a subclass. It's effectively a way of saying, "Hey, if you're seeing this error, it means you've forgotten to implement this method in your subclass."

    So when we define a method as follows in the PetEmployee class:

    ```python title="PetEmployee class"
    def daily_duty(self):
        raise NotImplementedError("Implement this abstract method in a subclass")
    ```

    It's like we're putting up a big neon sign saying "Hey, this method needs to be implemented in any subclass that uses it".

    The difference between `NotImplementedError` and other types of exceptions is really just about semantics and when they're used. We raise a `NotImplementedError` when we're creating a method that is supposed to be overridden by a subclass.


## 7.6. Magic Methods

### 7.6.1. `__repr__` and `__str__`

We are about to plunge into the wacky world of Magic (or Dunder) Methods in Python. These methods are special functions with double underscores at the start and end of their names (e.g., `__init__`, `__repr__`, `__str__`), hence the nickname "Dunder" (from Double UNDERscore).

Now, let's dissect our code here, which depicts a class `PetEmployee` we created in the previous sections:

```python title="Input"
class PetEmployee:
    promotion_rate = 1

    def __init__(self, name, age, species, level):
        self.name = name
        self.age = age
        self.species = species
        self.email = name + '.' + species + '@gmail.com'
        self.level = level

    def fullname(self):
        return '{} {}'.format(self.name, self.species)

    def apply_promotion(self):
        self.level = self.level + self.promotion_rate

    def __repr__(self):
        return "PetEmployee('{}', {}, '{}', {})".format(self.name, self.age, self.species, self.level)

    def __str__(self):
        return '{}, {}'.format(self.fullname(), self.species)
```

In this class, we've implemented two magic methods, `__repr__` and `__str__`. They are used to represent our objects in different ways.

The `__repr__` method returns a string that represents the exact state of the object. This is super useful for debugging and logging, as it provides a complete representation of the object, which we could use to recreate it. 

The `__str__` method, on the other hand, is more user-friendly. It returns a string that represents the object in a way that is easy to read. This is what is displayed to the end user.

Let's say we create two `PetEmployee` instances:

```python
barkalot = PetEmployee('Barkalot', 3, 'Dog', 3)
furrytail = PetEmployee('Furrytail', 2, 'Cat', 5)
```

Before defining `__repr__` and `__str__`, printing `barkalot` would give something like `<__main__.PetEmployee object at 0x0000020E0F6F6F98>`. Not so informative, right? It's just telling us that `barkalot` is an object of `PetEmployee` class at a specific memory address.

However, after defining these methods:

```python title="Input"
print(repr(barkalot))
print(str(barkalot))
```

The output now becomes much more informative:

```python title="Output"
"PetEmployee('Barkalot', 3, 'Dog', 3)"
"Barkalot Dog"
```

The first one is the `__repr__` output, which provides a complete representation of the `barkalot` object. The second one is the `__str__` output, which is more human-readable and pleasant to the eye. Now we're talking!

Remember, folks, the magic of Dunder methods lies in their ability to let us customize Python class behavior in powerful ways. These methods open the door to a whole new world of possibilities! So go ahead and try using them in your own classes. You'll be amazed at what you can achieve! 

### 7.6.2. `__add__` and `__len__`

Let's go over the code snippet provided:

```python title="Input"
class PetEmployee:
    promotion_rate = 1

    def __init__(self, name, age, species, level):
        self.name = name
        self.age = age
        self.species = species
        self.email = name + '.' + species + '@gmail.com'
        self.level = level

    def fullname(self):
        return '{} {}'.format(self.name, self.species)

    def apply_promotion(self):
        self.level = self.level + self.promotion_rate

    def __repr__(self):
        return "PetEmployee('{}', {}, '{}', {})".format(self.name, self.age, self.species, self.level)

    def __str__(self):
        return '{}, {}'.format(self.fullname(), self.species)

    def __add__(self, other):
        return self.level + other.level

    def __len__(self):
        return len(self.species)
```

```python title="Input"
barkalot = PetEmployee('Barkalot', 3, 'Dog', 3)
furrytail = PetEmployee('Furrytail', 2, 'Cat', 5)

print(barkalot + furrytail)
print(len(barkalot))
```
```python title="Output"
8
3
```

Now, let's untangle this. We've got two new magic methods on our hands: `__add__` and `__len__`.

The `__add__` method allows us to define the behavior for the addition operator `+`. Here, we've chosen to add the levels of two `PetEmployee` instances together. It's like saying, "Hey, Python! When I add two pet employees together, what I really want is to add their levels."

So, if we were to add `barkalot` and `furrytail`:

```python
print(barkalot + furrytail)
# Or print(barkalot.__add__(furrytail))
```

We'd get `8`, because `barkalot`'s level is `3` and `furrytail`'s level is `5`. Quick math, folks!

Similarly, the `__len__` method allows us to define behavior for the `len()` function applied to an instance of our class. Here, it's been defined to return the length of the species name.

So, printing `len(barkalot)`:

```python
print(len(barkalot))
# Or print(barkalot.__len__())
```

Would yield `3`, because the species name 'Dog' has three characters.


## 7.7. Getters, Setters, and Deleters

We're about to delve into the land of Getters, Setters, and Deleters in Python. Picture this, your pet has attributes, like its name, species, and level. These attributes are like the pet's toys. Your pet can fetch these toys, place them somewhere else, or even destroy them (hopefully, they don't do this often). In the coding world, these actions translate to getting, setting, and deleting attributes!

Let's take a peek at the magic Python has tucked up its sleeve:

=== "Getters"

    Getters are like a fetching command for your pet. They fetch the value of a private attribute. Python, being the friendly language that it is, makes getters easy to use with the `@property` decorator. This allows us to access a method as if it were a simple attribute. Here's how it looks:

    ```python
    class Pet:
        def __init__(self, name=None):
            self._name = name

        @property
        def name(self):
            return self._name
    ```

    In this example, `name` is a getter for the private attribute `_name`.

=== "Setters"

    Setters are like telling your pet to place its toy somewhere else. They allow us to set the value of private attributes. We use the `@<attribute>.setter` decorator to create a setter in Python:

    ```python
    class Pet:
        def __init__(self, name=None):
            self._name = name

        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, name):
            self._name = name
    ```

    Here, `@name.setter` allows us to set the value of `_name`.

=== "Deleters"

    Deleters are like your pet destroying its toy. They allow us to delete attributes. We use the `@<attribute>.deleter` decorator to create a deleter in Python:

    ```python
    class Pet:
        def __init__(self, name=None):
            self._name = name

        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, name):
            self._name = name

        @name.deleter
        def name(self):
            del self._name
    ```

    The `@name.deleter` allows us to delete `_name` from our instance.

____________________________________________________________

With these magic methods, we can have full control over our class attributes, just like training your pets to handle their toys responsibly. Don't forget to treat your pets, and your code, with care!

Next up, we'll see how these getters, setters, and deleters play together in a single class. Keep your coding boots on; it's going to be a thrilling ride!

### 7.7.1. Motivation
It's time to introduce getters, setters, and deleters - Python's very own magic carpet ride for navigating the world of object attributes. 

First, let's revisit our initial code:

```python title="Input"
class PetEmployee:

    def __init__(self, name, species, level):
        self.name = name
        self.species = species
        self.email = name + '.' + species + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.name, self.species)


barkalot = PetEmployee('Barkalot', 'Dog', 3)

barkalot.name = 'Furrytail'
print(barkalot.name)
print(barkalot.fullname())
print(barkalot.email)
```

```python title="Output"
Furrytail
Furrytail Dog
Barkalot.Dog@gmail.com
```

Now, upon looking at the output, we can see a big woof-woof. We changed `barkalot`'s name to 'Furrytail', and the full name changes as expected. But the email stays the same! It's like calling a cat a dog and expecting it to bark. Now, we could manually update the email every time we change the name, but who wants to do all that extra work? Certainly not us!

### 7.7.2. Getter

Now we have two ways to fix the above issue:

=== "Define a new instance method"
    ```python title="New instance method"
    class PetEmployee:

        def __init__(self, name, species, level):
            self.name = name
            self.species = species

        def email(self):
            return "{}.{}@gmail.com".format(self.name, self.species)

        def fullname(self):
            return '{} {}'.format(self.name, self.species)
    ```

    ```python title="Input"
    barkalot = PetEmployee('Barkalot', 'Dog', 3)
    barkalot.name = 'Furrytail'

    print(barkalot.name)
    print(barkalot.fullname())
    print(barkalot.email()) # We have to change all instances of email to email()
    ```
    ```python title="Output"
    Furrytail
    Furrytail Dog
    Furrytail.Dog@gmail.com
    ```
    The issue we faced was that every time we changed the name of our `PetEmployee`, we had to manually update the `email`. So, we turned our email attribute into a method that dynamically generates the email based on the current `name` and `species`. Problem solved, right? Well, not exactly. **Our solution created a new problem: we have to change every instance of `email` to `email()`.** Let's check our the other solution.

=== "Use a getter @property"
    ```python title="Getter @property"
    class PetEmployee:

        def __init__(self, name, species, level):
            self.name = name
            self.species = species

        @property
        def email(self):
            return "{}.{}@gmail.com".format(self.name, self.species)

        def fullname(self):
            return '{} {}'.format(self.name, self.species)
    ```

    ```python title="Input"
    barkalot = PetEmployee('Barkalot', 'Dog', 3)
    barkalot.name = 'Furrytail'

    print(barkalot.name)
    print(barkalot.fullname())
    print(barkalot.email) # You don't have to change anything!
    ```
    ```python title="Output"
    Furrytail
    Furrytail Dog
    Furrytail.Dog@gmail.com
    ```
    In this code, we introduced the `@property` decorator before our `email` method. Now we can access it as if it were a simple attribute, no need to write those pesky parentheses. It's just like a self-walking pet; no extra effort required!

    We've not only kept the functionality of our first solution (dynamically updating the email), but also made it much more user-friendly. This is what we call a win-win situation in the coding world!


### 7.7.3. Setter

We're about to dive into the realm of setters. Setters are kind of like giving your pet a new name. You're setting a new value to an attribute. 

In Python, we can disguise methods as attributes using the `@property` decorator. But when we want to set a new value to this "attribute", we need a `setter`. A `setter` allows us to define custom behavior for setting values. You might think of it as a strict pet owner who insists on a specific way to feed their pet. 

Here's the code for our `PetEmployee` class with a `setter`:

```python title="Setter"
class PetEmployee:
    def __init__(self, name, species, level):
        self.name = name
        self.species = species

    @property
    def email(self):
        return "{}.{}@gmail.com".format(self.name, self.species)

    @property
    def fullname(self):
        return '{} {}'.format(self.name, self.species)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.name = first
        self.species = last
```

Let's dissect this piece of beauty:

1. We start by initializing our `PetEmployee` with a `name`, `species`, and `level`.
2. We then create a `@property` for `email`, which takes the `name` and `species` and creates an email-like string. With this, when we call `barkalot.email`, Python calls the `email` method behind the scenes.
3. We do the same for `fullname`, which gives us a concatenated string of `name` and `species`.
4. Then comes the star of our show, the `@fullname.setter` decorator. This turns our `fullname` method into a setter, allowing us to assign a new value to `fullname`. It splits the assigned value into two parts - `first` and `last` - and sets `name` and `species` respectively.

Finally, we test our code:

```python title="Input"
barkalot = PetEmployee('Barkalot', 'Dog', 3)
barkalot.fullname = 'Furrytail Cat'

print(barkalot.name)  
print(barkalot.fullname)  
print(barkalot.email)  
```
```python title="Output"
Furrytail
Furrytail Cat
Furrytail.Cat@gmail.com
```

Our pet Barkalot has now been successfully renamed to Furrytail, a cat, and his email has changed too. 


### 7.7.4. Deleter

The following code is the class `PetEmployee` with a deleter:

```python title="Deleter"
class PetEmployee:
    def __init__(self, name, species, level):
        self.name = name
        self.species = species

    @property
    def email(self):
        return "{}.{}@gmail.com".format(self.name, self.species)

    @property
    def fullname(self):
        return '{} {}'.format(self.name, self.species)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.name = first
        self.species = last

    @fullname.deleter
    def fullname(self):
        print('Delete Pet Name!')
        self.name = None
        self.species = None
```

So, what's going on in here?

1. As before, we initialize our `PetEmployee` with a `name`, `species`, and `level`.
2. Then, we define the `@property` for `email` and `fullname` which return a string representation of email and the full name of the pet respectively.
3. We also have our `@fullname.setter` from earlier which allows us to set a new `name` and `species` for our pet.
4. But here comes the new kid on the block, the `@fullname.deleter`. This piece of magic deletes the `name` and `species` of our pet, effectively sending them into oblivion, and prints a message saying, "Delete Pet Name!".

Let's test it:

```python title="Input"
barkalot = PetEmployee('Barkalot', 'Dog', 3)
del barkalot.fullname

print(barkalot.name) 
print(barkalot.fullname) 
print(barkalot.email)  
```
```python title="Output"
Delete Pet Name!
None
None None
None.None@gmail.com
```


With a wave of our wand (well, the `del` command), we've gone ahead and removed our pet's name. Now, that's a power you'd want to handle carefully!

And just like that, we've completed our trilogy of Python's getters, setters, and deleters! It's like we've just stepped out of a rollercoaster ride of Python object-oriented programming. But worry not, there are plenty more exciting rides in this amusement park. 

In our next adventure, how about we look at Python's built-in `property` function and how it can be used instead of the `@property` decorator? Or perhaps, we could delve into how Python's `getattr`, `setattr`, and `delattr` functions work. They provide another way to get, set, or delete attributes of an object. 

### 7.7.5. Built-in property function

You've seen the `@property` decorator in action, now let's see how its sibling `property()` works its magic. Ready? Let's get coding!

In Python, `property()` is a built-in function that creates and returns a property object. A property object has three methods, getter(), setter(), and deleter() that we can use instead of @property and its associated decorators. 

Let's put this into context with our beloved `PetEmployee` class. Instead of using `@property`, `@fullname.setter`, and `@fullname.deleter` decorators, we'll use the `property()` function:

```python title="Built-in property function"
class PetEmployee:

    def __init__(self, name, species, level):
        self._name = name
        self._species = species

    def get_fullname(self):
        return '{} {}'.format(self._name, self._species)

    def set_fullname(self, name):
        first, last = name.split(' ')
        self._name = first
        self._species = last

    def del_fullname(self):
        print('Delete Pet Name!')
        self._name = None
        self._species = None

    fullname = property(get_fullname, set_fullname, del_fullname, 
                        "I'm the 'fullname' property.")
```

What just happened? Let's dissect this piece by piece:

1. We're defining our `get_fullname`, `set_fullname`, and `del_fullname` methods as usual. But notice that we're now working with `_name` and `_species`. These are called 'private' attributes, and it's a convention in Python to indicate that these attributes should not be accessed directly. They're meant to be manipulated through methods instead.
   
2. Finally, the line `fullname = property(get_fullname, set_fullname, del_fullname, "I'm the 'fullname' property.")` creates the `fullname` property. The `property()` function takes four arguments: fget (getter function), fset (setter function), fdel (deleter function), and doc (docstring). We've set all of these for our `fullname` property.

Now let's test our new and shiny `PetEmployee`:

```python title="Input"
barkalot = PetEmployee('Barkalot', 'Dog', 3)

print(barkalot.fullname)  # Output: Barkalot Dog

barkalot.fullname = 'Furrytail Cat'
print(barkalot.fullname)  # Output: Furrytail Cat

del barkalot.fullname  # Output: Delete Pet Name!
```
```python title="Output"
Barkalot Dog
Furrytail Cat
Delete Pet Name!
```


With `property()`, we've gained another tool to effectively encapsulate data in our Python classes.

In our next thrilling episode, we'll be exploring Python's `getattr()`, `setattr()`, and `delattr()` functions. These handy functions allow us to interact with an object's attributes using their string names! 

### 7.7.6. getattr(), setattr(), and delattr()

The `getattr()` function is used to retrieve the value of a named attribute of an object. If not found, it returns the default value provided to the function.

```python title="Input"
class PetEmployee:
    def __init__(self, name, species, level):
        self.name = name
        self.species = species
        self.level = level

barkalot = PetEmployee('Barkalot', 'Dog', 3)

# Using getattr()
print(getattr(barkalot, 'name'))  # Output: Barkalot
```
```python title="Output"
Barkalot
```


The `setattr()` function is used to set the value of a named attribute of an object. If the attribute does not exist, this function creates a new attribute by the given name.

```python title="Input"
# Using setattr()
setattr(barkalot, 'name', 'Furrytail')
print(barkalot.name)  # Output: Furrytail
```
```python title="Output"
Furrytail
```


The `delattr()` function is used to delete an attribute. If the attribute does not exist, this raises an `AttributeError`.

```python title="Input"
# Using delattr()
delattr(barkalot, 'name')

# Now trying to access the name attribute will raise an AttributeError
print(barkalot.name) 
```
```python title="Output"
AttributeError: 'PetEmployee' object has no attribute 'name'
```

!!! tip "Error Handling"
    Instead of raising an error, we can also use a `try`/`except` block to handle the error gracefully:
    ```python title="Input"
    try:
        print(barkalot.name)
    except AttributeError:
        print("'PetEmployee' object has no attribute 'name'")
    ```
    ```python title="Output"
    'PetEmployee' object has no attribute 'name'
    ```
    
Seeing "object has no attribute 'name'" is Python's way of telling you that you've crossed a boundary and attempted to access something that just doesn't exist. It's like trying to walk through a door that isn't there. You're just going to run into a wall (or in our case, an error).

These methods can be particularly useful in situations where you want to manipulate attributes dynamically, like in large projects or when working with user-defined inputs.


!!! note "Exercise"
    **Objective**: 
    
    Your task is to further enhance the Circle class in Python, making it aware of the unit system used (Metric or Imperial).

    **Requirements**:

    The Circle class currently supports a radius in centimeters (cm). However, we also want to accommodate input in inches for our friends who use the Imperial system. Enhance the Circle class to support initializing the radius in either cm or inches.

    Extend the radius setter method to convert an input radius in inches to cm before storing it in the _radius attribute. The unit attribute should control whether conversion takes place. If unit is 'inch', convert the input to cm (remember that 1 inch equals 2.54 cm). If unit is 'cm', store the input as is.

    Add a new property method, radius_inch, that returns the current radius converted to inches as a sanity check.

    Ensure that the area and circumference properties continue to work as expected, returning the area and circumference of the circle in cm² and cm, respectively.

    === "Code Skeleton"
        ```python title="Input"
        import math

        class Circle:
            def __init__(self, radius, unit='cm'):
                self.unit = unit
                self.radius = radius

            @property
            def area(self):
                pass

            @property
            def circumference(self):
                pass

            @property
            def radius(self):
                pass

            @radius.setter
            def radius(self, radius):
                pass

            @property
            def radius_inch(self):
                pass

        circle_1 = Circle(3)
        print(circle_1.radius) 
        print(circle_1.radius_inch)

        circle_2 = Circle(4, 'inch') 
        print(circle_2.radius)
        print(circle_2.radius_inch)
        ```

    === "Solution"
        ```python title="Input"
        import math

        class Circle:
            def __init__(self, radius, unit='cm'):
                self.unit = unit
                self.radius = radius  # Radius in specified unit

            @property
            def area(self):
                return math.pi * self._radius**2

            @property
            def circumference(self):
                return 2 * math.pi * self._radius

            @property
            def radius(self):
                return self._radius

            @radius.setter
            def radius(self, radius):
                if self.unit == 'inch':
                    self._radius = radius * 2.54  # Convert from inch to cm
                else:
                    self._radius = radius

            @property
            def radius_inch(self):
                return self._radius / 2.54  # Convert from cm to inch

        circle_1 = Circle(3)  # Radius in cm
        print(circle_1.radius)  # Output: 3
        print(circle_1.radius_inch)  # Output: 1.1811 (3 cm in inches)

        circle_2 = Circle(4, 'inch')  # Radius in inches
        print(circle_2.radius)  # Output: 10.16 (4 inches in cm)
        print(circle_2.radius_inch)  # Output: 4
        ```

In Python, we use the `@property` decorator to define `getter` methods. A `getter` method lets us access the value of a private attribute. Here, `radius` is a property of the class `Circle`, and the `radius` method gets the value of `_radius`.

The `@radius.setter` decorator defines the setter method for the `radius` property. A setter method allows us to set or modify the value of a private attribute. In our case, the `radius` setter converts the given `radius` to centimeters if the provided unit is in inches.

The `radius_inch` property allows us to convert and get the `radius` from centimeters to inches.

In the code snippet above, we create two instances of the class `Circle`. For `circle_1`, we define the `radius` in centimeters, and for `circle_2`, we define the `radius` in inches. The code then demonstrates how these concepts can be applied to convert and print the `radius` in different units.