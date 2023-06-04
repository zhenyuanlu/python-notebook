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

## 7.5. Special Methods

## 7.6. Decorators

## 7.7. Getters, Setters, and Deleters
