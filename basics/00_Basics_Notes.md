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





### Functions are first class objects
- Functions are considered as first-class objects.
- When we create a function, the python interpreter internally creates an object.
- In python, below things are possible to,
    - Assign function to variables 
    - Pass function as a parameter to another function
    - Define one function inside another function
    - Function can return another function



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


