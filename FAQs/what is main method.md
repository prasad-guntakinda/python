# What is a Module in Python?

A **module** in Python is a file containing Python code (functions, classes, or variables) that can be imported and reused in other Python programs. Modules help organize code into manageable and reusable components.

### Example of a Module:

Suppose we have a file named `math_utils.py`:

```python
# math_utils.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

You can import and use this module in another Python file:

```python
# main.py
import math_utils

result = math_utils.add(5, 3)
print(result)  # Output: 8
```

Python provides many built-in modules, such as `math`, `os`, and `sys`, which can be imported and used directly.

---

# Does Python Have a `main` Method Like Java?

In Python, there is no strict concept of a `main` method like in Java. However, Python uses a special construct to define the entry point of a program. This is done using the `if __name__ == "__main__":` block.

### Explanation:
- When a Python file is run directly, the `__name__` variable is set to `"__main__"`.
- When a Python file is imported as a module, the `__name__` variable is set to the module's name.

This allows you to write code that only executes when the file is run directly, not when it is imported.

### Example:

```python
# example.py
def greet():
    print("Hello, World!")

if __name__ == "__main__":
    greet()
```

- If you run `example.py` directly, the output will be:
  ```
  Hello, World!
  ```
- If you import `example.py` in another file, the `greet()` function will not execute automatically.

### Why Use `if __name__ == "__main__":`?
- It helps distinguish between code meant for execution and code meant for reuse.
- It makes your code modular and reusable.

---

### Comparison with Java:
In Java, the `main` method serves as the entry point for program execution:

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

In Python, the `if __name__ == "__main__":` block serves a similar purpose, but it is more flexible since Python does not enforce a specific structure for the entry point.