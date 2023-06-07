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

!!! note "Which Pet Employee Species Do We Have the Most Of?"

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
manager_barkalot = PetLeader('Whiskers', 5, 'Cat', 5)

pets = [emp_barkalot, ds_furrytail, manager_whiskers]

for pet in pets:
    pet_daily_duty(pet)

```python title="Output"
Work! Work! Work!
Importing data, analyzing data, and drinking coffee
Lead team and setting goals
```

The `daily_duty()` method has different implementations in the `PetEmployee`, `PetDataScientist`, and `PetLeader` classes. When we call `daily_duty()` on an object, the appropriate method is selected based on the object's class, not the type of the variable that is used to call the method. This is a classic example of polymorphism.

!!! note "`raise` keyword"
    In Python, `raise` is a keyword that's used to generate exceptions. By invoking `raise`, you're signaling to Python that an error has occurred, and you're asking Python to stop the normal execution of your program and instead, to "throw" an error that needs to be caught and handled.

    Now, let's talk about `NotImplementedError`. This is a special type of exception that we raise when we have a method or function that is supposed to be implemented by a subclass. It's effectively a way of saying, "Hey, if you're seeing this error, it means you've forgotten to implement this method in your subclass."

    So when we define a method as follows in the PetEmployee class:

    ```python title="PetEmployee class"
    def daily_duty(self):
        raise NotImplementedError("Implement this abstract method in a subclass")
    ```

    It's like we're putting up a big neon sign saying "Hey, this method needs to be implemented in any subclass that uses it".

    The difference between `NotImplementedError` and other types of exceptions is really just about semantics and when they're used. We raise a `NotImplementedError` when we're creating a method that is supposed to be overridden by a subclass.


## 7.6. Special Methods

## 7.7. Decorators

## 7.8. Getters, Setters, and Deleters
