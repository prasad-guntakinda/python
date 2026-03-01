# Functions:

Python functions are named, reusable blocks of code used to perform specific tasks, which enhance code modularity, reusability, and organization

## 1. Function Definition and Syntax
- A function is defined using the ``def`` keyword, followed by a function name, parentheses ``()``, and a colon ``:``. 
- The code block within the function must be __indented__ (typically four spaces). 

- Syntax:

```python
def function_name(parameter1, parameter2,....):
    """This function does heavy functional logic.""" # Optional docstring
    # function body/ group of statements
    # return value  # optional

```

- Example:
````python
def greet(name):
    """This function greets the person with the provided name.""" # Optional docstring
    print(f"Hello, {name}!")

````

- ``def``: Keyword marking the start of a function definition.
- ``function_name``: A unique identifier (uses __snake_case__ by convention).
- ``()``: Parentheses that may contain parameters.
- ``:``: Marks the end of the function header.
- ``Docstring``: An optional string literal as the first statement, used for documentation.
- ``return``: An optional value to return 

## 2. Calling a Function
To execute the code within a function, you must "call" it using its name followed by parentheses

````python
greet("John")
# Output: Hello, John!
````

---

## 3. Parameters and Arguments

- __Parameters__: Placeholders in the function definition that specify what data the function can accept.
- __Arguments__: The actual values passed to the function when it is called. 

### Python supports various argument types: 

1. __Positional Arguments__: Values are assigned based on their order in the function call.
2. __Keyword Arguments__: Arguments are passed using the parameter name, allowing them to be out of order.
3. __Default Arguments__: Parameters can have a preset value if no argument is provided during the call.
4. __**args__ (Arbitrary Positional Arguments): Used to pass a variable number of non-keyworded arguments, which are wrapped into a tuple inside the function.
- __***kwargs__ (Arbitrary Keyword Arguments): Used to pass a variable number of keyworded arguments, which are wrapped into a dictionary inside the function.


---

## 4. The return Statement
- The ``return`` statement is used to exit a function and pass a value (or values) back to the caller. 
- A function with no explicit return statement automatically returns __None__.
- Functions can return multiple values by returning a __tuple__. 
````python
def add_numbers(a, b):
    return a + b # Returns the sum to the caller

result = add_numbers(5, 3)
print(result) # Output: 8
````
---

## 5. Variable Scope
- Variables defined inside a function have a local scope and are not accessible from outside the function. 
- Variables defined outside all functions have a global scope and can be accessed (but not directly modified without the global keyword) from within functions. 


---

## 6. Types of Functions
- __Built-in Functions__: Functions that are part of the standard Python library (e.g., print(), len(), input()).
- __User-defined Functions__: Functions created by the user to perform specific tasks.
- __Lambda Functions__: Small, anonymous functions defined using the lambda keyword, typically for quick, single-expression tasks


---

# Arguments Types:

## 1. Positional-Only Arguments:
- These must be passed in order and cannot be called by name. In documentation, these appear before a forward slash ``/``.
- Example: ``abs(x)`` or ``pow(x, y, /)``

## 2. Keyword-Only Arguments
- These must be called by name (e.g., key=value). In documentation, these appear after an asterisk ``*``
- Example: ``print(*objects, sep=' ', end='\n')``

## 3. Default (Optional) Arguments:

- Parameters that have a value assigned in the definition. If the user doesn't provide one, Python uses the default.