# Functions

- A function is a block of code which performs a specific task.
- it helps avoiding code repetition.
- it enhances code modularity and reusability
- it only runs when it is called.
- A function can return data as a result.


## Types of function
There are two types of functions.

1. Pre-defined or built-in functions
2. User-defined functions
3. Lambda Functions: Small, anonymous functions defined using the lambda keyword, typically for quick, single-expression tasks


### 1. built-in functions:

- Functions that are part of the standard Python library.
- Examples: print(), len(), type()
- For all built-in functions refer: https://docs.python.org/3/library/functions.html


### 2. User-defined functions:

- The functions which are defined by developer as per the requirement is called as
user defined functions.

- __Syntax:__

- A function is defined using the ``def`` keyword, followed by a ``function_name``, parentheses ``()``, and a colon ``:``. 
- The code block within the function must be __indented__ (typically four spaces). 


````python 
 def function_name(parameter1, parameter2, ...): # parameters are optional
  """this function is to display the names """ # Optional docstring: used for documentation.
   # function body
   return value # optional
````


- Need of functions
  
````python
fruits = ["Apple", "Banana"]
for fruit in fruits:
    print(fruit)

fruits.append("Orange")

for fruit in fruits:
    print(fruit)

del fruits[0]

for fruit in fruits:
    print(fruit)

# here printing fruits list logic is repeated 3 times, instead of that if we can create a display function and call it for 3 times. which avoids code duplication

def display():
    for fruit in fruits:
        print(fruit)

display()

fruits.append("Water Melon")
display()
fruits.pop(1)
display()

fruits2 = ["Mango", "Pine apple", "Strawberry"]
display()
# Task: how fruits are displaying inside the function? 
# If I want to print fruits2 list what are the changes do I need to do?
````

- __Example-1:__ Greet user

````python
def greet(name): # defining
    """This function greets the person with the provided name.""" # Optional docstring
    print(f"Hello, {name}!")

greet("John") # calling
````

- __Example-2:__ Print whether a number is Odd or Even:

````python

def printEvenOdd(num):
    if num%2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")

````

- __Example-3:__ Calculate full_name from first_name and last_name

````python

# Defining Function
def full_name(first_name, last_name): # parameters: first_name, last_name
    return first_name + last_name

# Calling Function
full_name("James", "Smith") # arguments: "James", "Smith"
# If we call the function in n times, then n times function will get execute.
````

#### return statement
- The ``return`` statement is used to exit a function and pass a value (or values) back to the caller. 
- A function with no explicit return statement automatically returns __None__.
- Functions can return multiple values by returning a __tuple__. 
- Returning multiple values from function

````python
def m1(a, b):
    c = a+b
    d = a-b
    return c, d
#calling function
x, y = m1(10, 5)

````

## Variable Scope
- Variables defined inside a function have a __local scope__ and are not accessible from outside the function. 
- Variables defined outside all functions have a __global scope__ and can be accessed (but not directly modified without the global keyword) from within functions. 


---


## Parameters and Arguments:

- A __parameter__ is the variable listed inside the parentheses in the function definition.

- An __argument__ is the actual value that is sent to the function when it is called.

### Argument types: 

        1. Positional-Only Arguments:
        2. Keyword-Only Arguments
        3. Default (Optional) Arguments
        4. Arbitrary Positional Arguments
        5. Arbitrary Keyword Arguments


### 1. Positional-Only Arguments:
- These are the arguments passed to a function in correct positional order.
- By default functions are allowed to call with positional args as well as keyword args. if we want to enforce it to use position-only then we have to use `/` in function defition
- All the params which are left side of `/` should be passed with positional only args, otherwise we will get error.

- Example:

```python
def power1(x,y): # x and y are postion only arguments
    return x**y

print(power1(2,3)) # 8
print(power1(x=3,y=2)) # this still works because we are not enforcing postion only arguments

# enforcing postion only arguments
# x and y are postion only arguments and we are enforcing it by adding / at the end of the arguments 
# / is ignored by the interpreter but it tells us that the arguments before / are postion only arguments
def power_2(x,y, /): 
    return x**y

print(power_2(2,3)) # 8
print(power_2(x=3,y=2)) # this will raise a TypeError because we are enforcing postion only arguments
```
- What is the significance of position only args?
- significant primarily for API design, maintainability, and performance. 
- They allow function authors to enforce a specific calling convention and safely refactor their code. 
- functions where the order of arguments is crucial for the logical meaning, such as the pow(x, y, /) function, positional-only arguments ensure the intended usage.
- Consistency with Built-ins: Many of Python's built-in functions, which are implemented in C, are positional-only. The / syntax (introduced in Python 3.8 via PEP 570) allows pure Python functions to match the behavior and interface of their C-implemented counterparts, improving language consistency.

---

### 2. Keyword-Only Arguments
- Arguments are passed using the parameter name, allowing them to be out of order.
- These must be called by name (e.g., key=value). 
- we define a function with keyword only args by using an asterisk ``*``.
- All the params which are __right side of `*`__ should be passed with keyword only args, otherwise we will get error.
- Syntax:
- In Python, you specify keyword-only arguments by placing them eitehr after a bare `asterisk (*)` or after another parameter that collects arbitrary positional arguments (e.g., `after *args`) in the function signature 

```python
def func_1(a,b,*,c,d):
    print(a,b,c,d)

def func_2(*args,std_name,branch):
    print(args,std_name,branch)

# func_1(1,2) # missing required keyword-only arguments: 'c' and 'd'
func_1(1,2,c=10,d=20) # 1 2 10 20

#func_2(1,2,3) # missing required keyword-only arguments: 'std_name' and 'branch')
func_2(1,2,3,std_name="John",branch="CS") # (1, 2, 3) John CS

```

- Example-2:

```python

def function_name(*, first_name, last_name):
    return first_name + " " + last_name
```
- Example-3:

```python
def mix(a, b, /, c, *, d,e): # a,b are position-only args, c= anything, d,e are keyword only args
    return a+b+c+d+e

print("mix", mix(1, 2,c= 3,d=4,e=5) ) 
```

#### What is the significance of keyword-only args?

- __Improved Readability and Clarity:__ Explicitly naming arguments when calling a function makes the code self-documenting. A reader immediately understands what value is being passed to which parameter without needing to check the function definition or signature 

- __Prevention of Errors:__ It eliminates ambiguity and common mistakes where a user might accidentally pass values in the wrong positional order. This is particularly useful for functions with multiple boolean flags or parameters of the same type

---

### 3. Default (Optional) Arguments:

- Parameters that have a value assigned in the definition. If the user doesn't provide one, Python uses the default.

### 4. Arbitrary (Variable length) arguments:
- In Python, arbitrary arguments (also known as variable-length arguments) allow a function to accept any number of inputs, which is useful when you don't know the exact number of arguments in advance. 
- This is achieved using special syntax in the function definition, which collects the arguments into a single iterable object.


#### 4.1 Arbitrary Positional Arguments: (*args):
 
- Used to pass a variable number of non-keyworded arguments, which are wrapped into a tuple inside the function.
- Syntax: A single asterisk (*) is placed before the parameter name in the function definition (conventionally named `*args`).
- Functionality: All non-keyword arguments passed to the function are collected into a single __tuple__.

- Exammple-1
```python
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

result1 = add_numbers(10, 20, 30, 40) # args becomes (10, 20, 30, 40)
print(result1) # Output: 100

result2 = add_numbers(1, 2, 3)       # args becomes (1, 2, 3)
print(result2) # Output: 6

```

- Example-2:

```python
def gst(*prices, gst=5):
    return (sum(prices)*gst)/100
```

#### 4.2 Arbitrary Keyword Arguments: (**kwargs): 
- Used to pass a variable number of keyworded arguments, which are wrapped into a __dictionary__ inside the function.
- __Syntax:__ A double asterisk (**) is placed before the parameter name (conventionally named **kwargs).
- __Functionality:__ All keyword arguments passed to the function are collected into a single dictionary, where the keys are the argument names and the values are the corresponding values.

- Example:

```python
def user_details(**kwargs):
    print("User Information:")
    for key, value in kwargs.items():
        print(f"- {key}: {value}")

user_details(name="John", city="Mumbai", phone="9123134567")
# kwargs becomes {'name': 'John', 'city': 'Mumbai', 'phone': '9123134567'}

```

### Combining Argument Types
- You can use both types of arbitrary arguments, along with regular arguments, in the same function. The correct order in the function definition is: 

1. Regular positional/keyword arguments
2. `*args`
3. `**kwargs`

- Example of combined usage:
```python
def my_function(title, *args, **kwargs):
    print("Title:", title)
    print("Positional arguments (tuple):", args)
    print("Keyword arguments (dictionary):", kwargs)

my_function("User Info", "Emil", "Tobias", age=25, city="Oslo")
# Output:
# Title: User Info
# Positional arguments (tuple): ('Emil', 'Tobias')
# Keyword arguments (dictionary): {'age': 25, 'city': 'Oslo'}
```
---

### Argument Types Summary:

1. __Position-Only Argument:__  we have to pass values directly which are left side of `/`
2. __Keyword Only Arguments:__ We have to pass values with `keyword=vaue` which are right side of `*` or `*object` 
3. __Default Arguments:__ it makes argument is optional, if we pass value then it is considered otherwise default value is considered
4. __Arbitrary Arguments (*args and **kwargs):__
    4.1: __*args:__ Position-Only Args, we can pass zero or more elements. all values are stored into `tuple`
    4.2: __**kwargs:__ Keyword-Only Args, we can pass zero or more keyword args.all values are stored into `dictionary`

