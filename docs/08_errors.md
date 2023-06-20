# 8. Error Handling and Exceptions

## 8.1. Motivation

Exception handling is a process of responding to the occurrence, during computation, of exceptions – anomalous or exceptional conditions requiring special processing – often changing the normal flow of program execution. It is provided by the software to handle an exception.

Imagine this: you're feeling great, confidently coding away, when suddenly, you hit an error. You see a terrifying red message on your console: `[Errno 2] No such file or directory: 'test_.txt'`. Your code has crashed, and your app came to a screeching halt. This is the nightmare we all strive to avoid.

Here's the offending line of code that brought upon this digital disaster:

```python title="Input"
f = open('test_.txt')
```

```python title="Output"
[Errno 2] No such file or directory: 'test_.txt'
```

Seems innocent enough, right? You're just trying to open a file named `test_.txt`. But there lies the problem: What if the file doesn't exist? 

Well, that's exactly what's happened here. The file `test_.txt` doesn't exist in the directory, and Python, ever so literal, freaks out. It raises an error and stops the entire program.

This situation can be quite distressing, especially if your code is running a mission-critical application. What if you're running an app that controls a hospital's life support systems, or an app that provides real-time navigation for drivers? An unexpected crash could have serious consequences. 
 
That's why error handling is so vital in programming. In Python, we have a powerful tool to catch and handle these errors: the `try/except` block. 

## 8.2. Try/Except Blocks

Our seatbelt in this situation is the `try/except` block:

```python title="Input"
try:
    f = open('test_.txt')  # We are trying to open the file here
    var = not_exist_file  # Oops, this variable doesn't exist!
except Exception:
    print('Sorry. Wrong File Name')  # If an error happens in the try block, we catch it here and print a friendly message.
```
```python title="Output"
Sorry. Wrong File Name
```

When our code hits the `try` block, it attempts to execute the code inside. If everything goes smoothly, it continues to run the rest of the code. But if it hits an error (like trying to access a non-existent file or variable), it jumps straight to the `except` block. The `Exception` keyword catches all types of errors, so no matter what went wrong in the `try` block, the `except` block will handle it gracefully.

In our case, since the file 'test_.txt' doesn't exist and the variable `not_exist_file` is not defined, an error occurs. But rather than crashing our program, it triggers the `except` block, and we see the output: `'Sorry. Wrong File Name'`. The magic of try/except saves our day (or code)!

Keep in mind that handling errors gracefully is an essential part of writing robust, production-ready code. With Python's try/except blocks, you're well-equipped to handle any bumps along the way. 

## 8.3. Catching Specific Errors

However, our `except` block was a bit too general. It catches all kinds of errors, not just the one we're anticipating (`FileNotFoundError`). 

We can specify which error our `except` block should catch. To do this, we simply follow the `except` keyword with the name of the error we're expecting. In our case, `FileNotFoundError`. If this specific error occurs, our `except` block will be executed:

```python title="Input"
try:
    f = open('test.txt')
    var = not_exist_file # this will throw an Nameerror.
except FileNotFoundError:
    print('Sorry. Wrong File Name')
```
```python title="Output"
NameError: name 'not_exist_file' is not defined
```

But wait! There's more! If we run the code now, we're greeted with another error: `NameError: name 'not_exist_file' is not defined`. Our `try` block contains another error that we didn't catch. Remember, Python stops executing the `try` block as soon as it encounters an error. 

The plot thickens. Let's add another `except` block to catch this second error. Each `except` block will catch its specified error:

```python title="Input"
try:
    f = open('test.txt')
    var = not_exist_file # this will throw an error.
except FileNotFoundError:
    print('Sorry. Wrong File Name')
except NameError:
    print('Name not found in current scope.')
```
```python title="Output"
Name not found in current scope.
```

Now our program runs without crashing, handling both errors gracefully, and our world is back in balance. So remember folks, always keep your exceptions specific. It's like inviting guests to a party. 


So far, we've seen how to catch specific errors using multiple `except` blocks. Now let's learn how to catch the error message itself.

When an error occurs, Python creates an `exception object` that contains specific information about the error. We can grab this object and print its content to get a detailed error message. 

To do this, we'll add an `as e` after our exception in the `except` block. The `e` is just a variable name; you could call it anything, but `e` is common. This variable now holds the exception object. When we print `e`, we get the specific error message:

```python title="Input"
try:
    f = open('test.txt')
    var = not_exist_file # this will throw an error.
except FileNotFoundError as e:
    print(e)
except NameError as e:
    print(e)
```
```python title="Output"
name 'not_exist_file' is not defined
```

This block of code will print: `name 'not_exist_file' is not defined` if the `NameError` is encountered. So instead of a vague "Oops, something went wrong", you get a detailed report of the error that occurred. 

This technique helps us debug our code by providing more specific information about what went wrong. 

## 8.4. `else` and `finally` Blocks

Now that we've gotten comfortable with using `try` and `except` to catch and handle exceptions, let's introduce two new blocks that can be used within the `try/except` structure: `else` and `finally`.

**The `else` block:** 

The `else` block in `try/except` is used to specify a block of code to be executed if no exceptions were raised in the `try` block. In other words, if everything in the `try` block goes smoothly, the `else` block runs. It's kind of like saying, "If there are no issues, then let's do this too!" 

Here's how we used it in the code you provided:

```python title="Input"
try:
    f = open('test.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
```
```python title="Output"
test!
```

In this code snippet, we attempt to open a file named 'test.txt'. If the file does not exist, a `FileNotFoundError` is raised and handled. If any other type of exception is raised, it's also caught and handled. If no exceptions are raised (meaning the file opens successfully), the `else` block is executed, and the file is read and then closed.

**The `finally` block:**

The `finally` block in `try/except` is a place to put any code that MUST execute, whether an exception was raised or not. It's like a safety net that catches any code you absolutely want to run, no matter what happens.

Take a look at how we used it in the code:

```python title="Input"
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
```
```python title="Output"
test!
Executing Finally...
```

After trying to open the file, whether it succeeds or an exception occurs, 'Executing Finally...' is printed. This is because the `finally` block always executes, regardless of whether an exception occurred in the `try` block. 

`finally` can be useful in many scenarios. For example, you might use it for cleanup tasks, such as closing files or network connections, regardless of the success or failure of the earlier operations. 

With the addition of `else` and `finally`, we now have a lot of control over how our program handles exceptions and ensures certain code always runs.


## 8.5. Raising Exceptions

In the above code, you used the `raise` keyword. The `raise` keyword is used to trigger an exception explicitly. We can also pass a custom message or another exception class with the `raise` keyword. Let's take a closer look at how you've used it:

```python title="Input"
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
```
```python title="Output"
[Errno 2] No such file or directory: 'corrupt_.txt'
Executing Finally...
```


In this case, you're attempting to open a file named `corrupt_.txt`. You then check if the file's name is `corrupt.txt`. If it is, you raise an Exception. If a `FileNotFoundError` occurs (i.e., if the file doesn't exist), it gets caught and you print out the error. If the raised Exception occurs, it also gets caught and you print out 'Error!'.

In your specific case, the file `corrupt_.txt` does not exist. So, the `FileNotFoundError` is raised first and caught by the first `except` block. The error message is printed, and then the `finally` block is executed, printing 'Executing Finally...'.


If the file had existed and its name was `corrupt.txt`, the `Exception` would be raised, 'Error!' would be printed, and the `finally` block would be executed.

Let's say we want to raise an exception with a custom error message when the file name is 'corrupt.txt'. We can do this by passing a string to the `Exception` class, like so:

```python title="Input"
try:
    f = open('corrupt.txt')
    if f.name == 'corrupt.txt':
        raise Exception('This is a corrupt file!')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('Error!')
else:
    print(f.read())
    f.close()
finally:
    print('Executing Finally...')
```
```python title="Output"
Error!
Executing Finally...
```

In this scenario, if the file `corrupt.txt` is found and opened successfully, an `Exception` is raised with the message 'Error!'. This exception is then caught by the second `except` block and the custom error message is printed. After that, the `finally` block is executed.

Raising exceptions can be very useful when you want to enforce certain conditions in your code, and halt the execution if these conditions are not met.

That wraps up this guide on Python's error handling and exceptions. By using `try/except` blocks, raising exceptions, and leveraging `else` and `finally` blocks, you can make your code more robust and able to handle unexpected errors more gracefully. 