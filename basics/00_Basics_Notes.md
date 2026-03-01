# Python Basics

## 00: Documentation:

- Documentation is reference, not story book.

- You only read:

    - When stuck
    - When exploring new module
    - When debugging
    - When learning best practices

- Think like dictionary, not novel.

### 1. How to read Python built-in method docs
- Main official site: https://docs.python.org/3/
- Python Standard Library Reference and Builtins: https://docs.python.org/3/library/index.html

### 2. Use Python itself as documentation (PRO way): type(), help(), dir()

- Inside Python terminal or Jupyter:
```python

help(list)
# For specific method:
help(list.append)

# dir() → See available functions
nums = [1,2,3]
print(dir(nums))


# Shows all methods available.
print(type(nums))

```
### 3. How senior developers explore unknown module

- Example: json module

- __Step 1:__

```python
# inside interpreter or inside py file
import json
dir(json) # inside interprepter
print(dir(json)) # in file

print(help(json.loads))
```


### 4. Reading third-party library docs (VERY IMPORTANT)

- Example:

    - requests
    - pandas
    - pyspark
    - numpy

- Golden rule: Never open full documentation first. Instead Google directly

- Example:
    - pandas read csv
    - pyspark dataframe select
    - requests get example
-  How to read third-party docs fast
- When page opens, read only:
    - Syntax section: pandas.read_csv(filepath)
    - Parameters table: Don’t read all, Read only needed ones.
    - Example section (most important): Copy → run → understand.
    - Skip everything else initially.

### 5. GitHub documentation (real world skill)

- Many libraries have docs in GitHub.

- Example: `pyspark github`
- Open `README.md`
- Read only:
    - Installation
    - Basic example
    - API usage
    - Skip long theory.

### 6. Best trick senior developers use

- When learning new module:

- Pattern:

1. Google simple example
2. Run it
3. Then read docs
4. Then experiment
- Never reverse.
---

## 01: How python compile and run?


---




### Strings:

- Strings are sequences of characters, using the syntax of either single  quotes or double quotes:

```python
'hello'
"Hello"
" I don't do that "

```

- Because strings are **ordered sequences** it means we can using **indexing** and **slicing** to grab sub-sections of the string.
- Indexing notation uses [ ] notation after the string (or variable assigned the string).
- Indexing allows you to grab a single character from the string

````
These actions use [ ] square brackets and a number index to indicate positions of what you wish to grab.
Character :     h     e     l    l    o
    Index :     0     1     2    3    4
Reverse Index:  0    -4    -3   -2    -1

````

#### Slicing:

- Slicing allows you to grab a subsection of multiple characters, a “slice” of the string.
- This has the following syntax:
- `[start:stop:step]`
- **start** is a numerical index for the slice start
- **stop** is the index you will go up to (but not include)
- **step** is the size of the “jump” you take


````python
index0 = "Hello"[0]
indexNeg = "World"[-2]
print(index0)
print(type(index0))
print(indexNeg)

greet = "Hey There!"

print("greet", greet)
print(type(greet))
print(greet[4])

print("greet= ", greet)
print("slice: [0:3] ", greet[0:3]) # 0,1,2
print("slice: [0:7] ", greet[0:7]) # 0,1,2,3,4,5,6
print("slice: [0:7:2] ", greet[0:7:2]) # 0,2,4,6
````


#### Strings Methods 

````python
# Properties & Methods of Strings
# Strings are immutable
print("greet.upper(): ", greet.upper())  # convert to uppercase
print("greet.lower(): ", greet.lower())  # convert to lowercase
print("greet", greet)  # original string remains unchanged

# split string into list
print("greet.split(): ", greet.split())  # default split by space
print("greet.split(e): ", greet.split('e'))  # split by 'e'



````

#### Strings Formatting:

````python

# formatting
name = "John"
age = 30
print("My name is {} and I am {} years old".format(name, age))
print("My name is {1} and I am {0} years old".format(age, name))  # positional arguments
print("My name is {n} and I am {a} years old".format(n=name, a=age))  # keyword arguments
print("My name is {n} and I am {a} years old".format(a=age, n=name))  # order doesn't matter
print("My name is {:s} and I am {:d} years old".format(name, age))  # type specifiers
print("My name is {:10s} and I am {:5d} years old".format(name, age))  # width

print(f"My name is {name} and I am {age} years old")  # f-string (Python 3.6+)
print("My name is %s and I am %d years old" % (name, age))  # old style
# %s - string, %d - integer, %f - float

````



---





---

## 05: Indentation
- In Python, we need to group the statements by using indentation.
- Why indentation
- Indentation keeps separate the group of statements.
- The recommended indentation is 4 spaces.
- We must follow the order of indentation otherwise we will get IndentationError


---


## 06: Operators

- Arithmatic Operators
- Logical Operators: and, or, not
- Membership Operators: in, not in

---


## 07: flow control: conditionals: if,elif,else

---

## 08: Loops: while, for


---

## 09: functions:

- A function can contain mainly two parts,
    - Defining function
    - Calling function
### 1. Defining a function
- `def` keyword is used to define function.
- After def keyword we should write name of the function.
    - After function name, we should write parenthesis `()`
    - After parenthesis we should write colon `:`
- This parenthesis may contain parameters.
    - Parameters are just like variables which receives the values.
    - If function having parameters, then we need to provide the values while calling.
- Function body.
    - Perform the operations.
- Before closing the function, function may contain `return` type.
-  Syntax
```python

def function_name(parameters) :
""" doc string"""
Body of the function to perform operation
return value (if required)
```

### Functions are first class objects
- Functions are considered as first-class objects.
- When we create a function, the python interpreter internally creates an object.
- In python, below things are possible to,
    - Assign function to variables 
    - Pass function as a parameter to another function
    - Define one function inside another function
    - Function can return another function


### Formal and actual arguments
- When a function is defined it may have some parameters.
- These parameters receive the values. Parameters are called as `formal arguments`
- When we call the function, we should pass values or data to the function, these values are called as `actual arguments`

- Example:

```python
def sum(a, b):
c = a + b
print(c)
# call the function
x = 10
y = 15
sum(x, y)

# a,b formal args
# x,y actual args
```

### Types of arguments
In python there are 4 types of actual arguments are existing,
1. positional arguments
2. keyword arguments
3. default arguments
4. variable length arguments

#### 1. Positional arguments
- These are the arguments passed to a function in correct positional order.
- The number of arguments and position of arguments should be matched,
otherwise we will get error

- Example:

```python
def sub(x, y):
print(x-y)
# calling function
sub(10, 20)
```
- If we change the number of arguments, then we will get error.
- This function accepts only two arguments then if we are trying to provide three
values then we will get error.

#### 2. Keyword arguments
- Keyword arguments are arguments that recognize the parameters by the name of
the parameters.
- Example: Name of the function is `cart()` and parameters are `item` and `price` can be written as:
```python
def cart(item, price)
```
- At the time of calling this function, we must pass two values and we can write
which value is for what by using name of the parameter.
- `item` and `price` are called as keywords in this scenario.
- Here we can change the order of arguments.
- Example

```python
def cart(item, price):
    print(item, "cost is: ",price)
# calling function
cart(item="bangles",price=20000)
cart(price=100000, item="shirt")
```

- We can use both positional and keyword arguments simultaneously.
- But first we must take positional arguments and then keyword arguments,
otherwise we will get syntax error.

```python
cart("dhoti",price=20000)
```

#### 3. Default arguments
- We can provide some default values for the function parameters in the definition.
- Let's take the function name as `cart(item, price=40.0)` (Example: In few shops
any item is 10 rupees)
- In above example item have no default value, so we should provide.
- price have default value as 40, Still if we provide the value at time of calling then default values will be override with passing value.

- Example:

```python
def cart(item, price = 40.0):
    print(item, "cost is: ",price)
# calling function
cart(item="pen")
cart(item="handbag", price=10000)
```

- While defining a function, after default arguments we should not take non-default arguments


#### 4. Variable length arguments
- Sometimes, the programmer does not know how many values need to pass to
function.
- In that case, the programmer cannot decide how many arguments to be given in
the function definition.
    - `totalcost(item1_cost, item2_cost)` => totalcost(1, 2) # valid
    - `totalcost(item1_cost, item2_cost)` => totalcost(1, 2, 3) # Invalid
- To accept number of arguments, we need to use variable length argument.
- The variable length argument is an argument that can accept any number of
values.
- The variable length argument is written with a (one star) before variable in
function definition.
- Syntax
```python
def nameofthefunction(x, *y):
    #body of the function
```
- `x` is formal argument
- `*y` is variable length argument
- Now we can pass any number of values to this `*y`.
- Internally the provided values will be represented in `tuple`.

- Example:

```python
def totalcost(x, *y):
    sum=0
    for i in y:
        sum+=i
    print(x + sum)

#calling function
totalcost(100, 200) # valid
totalcost(110, 226, 311) # valid
totalcost(11,) # valid
```

#### keyword variable length argument (`**variable`)

```python
def m1(**x):
    #body of the function
```

- `**x` represents as keyword variable argument
- Internally it represents like a `dictionary` object
- `dictionary` stores the data in the form of key value pairs.

```python
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(id=1, name="Nireekshan", qualification="MCA")

```

### Function vs Module vs Library:
- A group of lines with some name is called a function
- A group of functions saved to a file, is called Module
- A group of Modules is nothing but Library

### Anonymous functions or Lambdas
- A function without a name is called as anonymous function.
- Generally, to define normal function we need to use `def` keyword.
- To define anonymous function, we need to use `lambda` keyword.

- Syntax:
```python
# lambda argument_list: expression
s = lambda a: a*a
x=s(4)
print(x)

add=lambda x, y: x+y
result = add(1, 2)
print("sum of the value: ", result)
```

- Where lambda function fits exactly?
- Sometimes we can pass function as argument to another function. In such
cases lambda functions are best choice.
- We can use lambda functions very commonly with `filter()`, `map()` and `reduce()` functions, these functions expect function as argument.

#### filter() function
- Based on some condition we can filter values from sequence of values.
- Where function argument is responsible to perform conditional check, sequence
can be `list` or `tuple` or `string`.
- Syntax
```python
# filter(function, sequence)
#Program example by using filter function
items_cost = [999, 888, 1100, 1200, 1300, 777]
gt_thousand = filter(lambda x : x>1000, items_cost)
x=list(gt_thousand)
print("Eligible for discount: ",x)
```
#### map() function
- The `map()` function can apply the condition on every element which is available in the sequence of elements.
- After applying map function can generate new group of values
- Syntax
```python
# map(function, sequence)
# Program Find square by using map function
without_gst_cost = [100, 200, 300, 400]
with_gst_cost = map(lambda x: x+10, without_gst_cost)
x=list(with_gst_cost)
print("Without GST items costs: ",without_gst_cost)
print("With GST items costs: ",x)
```

#### reduce() function
- `reduce()` function reduces sequence of elements into a __single element__ by applying the specific condition or logic.
- `reduce()` function present in `functools` module. So, to work with reduce we need to `import functools` module.

- Syntax
```python
# reduce(function, sequence)
# Program reduce function

from functools import reduce
each_items_costs = [111, 222, 333, 444]
total_cost = reduce(lambda x, y: x+y, each_items_costs)
print(total_cost)
```

---

## 10: Modules:

---


## 11: Packages:

