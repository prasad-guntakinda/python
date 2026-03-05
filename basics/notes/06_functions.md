# Functions

- A function is a block of code which performs the specific task.
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

- __Example-1:__ 

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
- Variables defined inside a function have a local scope and are not accessible from outside the function. 
- Variables defined outside all functions have a global scope and can be accessed (but not directly modified without the global keyword) from within functions. 


---


## Parameters Vs Arguments:

- A __parameter__ is the variable listed inside the parentheses in the function definition.

- An __argument__ is the actual value that is sent to the function when it is called.

### Argument types: 

        1. Positional-Only Arguments:
        2. Keyword-Only Arguments
        3. Default (Optional) Arguments
        4. Arbitrary Positional Arguments
        5. Arbitrary Keyword Arguments


### 1. Positional-Only Arguments:
- These must be passed in order and cannot be called by name. In documentation, these appear before a forward slash ``/``.
- Example: ``abs(x)`` or ``pow(x, y, /)``

### 2. Keyword-Only Arguments
- These must be called by name (e.g., key=value). In documentation, these appear after an asterisk ``*``
- Example: ``print(*objects, sep=' ', end='\n')``

### 3. Default (Optional) Arguments:

- Parameters that have a value assigned in the definition. If the user doesn't provide one, Python uses the default.
1. __Positional Arguments__: Values are assigned based on their order in the function call.
2. __Keyword Arguments__: Arguments are passed using the parameter name, allowing them to be out of order.
3. __Default Arguments__: Parameters can have a preset value if no argument is provided during the call.
4. __Arbitrary Positional Arguments: (*args)__: Used to pass a variable number of non-keyworded arguments, which are wrapped into a tuple inside the function.
5. __Arbitrary Keyword Arguments: (**kwargs)__: Used to pass a variable number of keyworded arguments, which are wrapped into a dictionary inside the function.




def fullname(first_name, last_name):
    return first_name + " " + last_name

f_name = fullname("John", "Abr")

print("fullname = ", f_name)


print("With keyword", fullname("Bhanu", last_name="c"))

# Argument Types:

def only_pos_args(fname, lname, /):
    return fname + lname


# only_pos_args(fname="Ram", lname="Hari")
print(" Position only: ", only_pos_args("Ram", "Hari")) 


for num in range(10):
    print(num, end=" ")

print("======================== Keyword Only Argument===============================")

def function_name(*, first_name, last_name):
    return first_name + " " + last_name


def fullname_keywordOnly(*, first_name, last_name):
    return first_name + " " + last_name

print("Keyword Only: ", fullname_keywordOnly(first_name= "Ram", last_name = "Sam"))


def mix(a, b, /, c, *, d,e): # a,b are position-only args, c= anything, d,e are keyword only args
    return a+b+c+d+e

print("mix", mix(1, 2,c= 3,d=4,e=5) ) 

# Position-Only Argument:  we have to pass values directly which are left side of /
# Keyword Only Arguments: We have to pass with key=vaue which are right side of *

## Arbitrary Arguments (*args and **kwargs)


print("========================  Arbitrary Arguments (*args and **kwargs) ===============================")
def total(*nums): # we can pass zero or more arguements position-only args
    print(nums)
    print(type(nums))
    sum = 0
    for num in nums:
        sum = sum+num
    print("sum=", sum)
    
total()
total(5, 4,6,7)

# total(nums=(1,2,3,4))


def display(**kwargs): # we can pass zero or more keyword args.it should keyword-only args
    print(kwargs)
    #print(type(kwargs))
    
    if kwargs.get("id") : # None, False, 
        print("id=", kwargs["id"])
    
display()

display(first_name="Ram", last_name="sam", id=12345)

print("========================  Default Arguments  ===============================")



def gst(prices, gst=5):
    
    return (prices*gst)/100

print(gst(1000,10))



# 1. Position-Only Argument:  we have to pass values directly which are left side of /
# 2. Keyword Only Arguments: We have to pass values with keyword=vaue which are right side of * 
# 3. Arbitrary Arguments (*args and **kwargs)
#   3.1: *args: Position-Only Args, we can pass zero or more elements. all values are stored into tuple
#   3.2: **kwargs: Keyword-ONly Args, we can pass zero or more keyword args.all values are stored into dictionary
# 4. Default Arguments: it makes argument is optional, if we pass value then it is considered otherwise default value is considered  








