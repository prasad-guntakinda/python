# How to view Python API docs?

### How to Find Built-in Documentation for Python

1. **Official Python Docs Website**  
   - Visit: https://docs.python.org/3/library/  
   - This is the standard library reference, similar to Java API docs.

2. **Using the `help()` Function in Python**  
   - You can use the built-in `help()` function in the Python REPL or scripts:
   ```python
   help(list)         # Shows documentation for the list class
   help(str.upper)    # Shows documentation for the str.upper method
   help('modules')    # Lists all available modules
   ```

3. **Using `dir()` to List Attributes/Methods**  
   - Example:
   ```python
   dir(dict)          # Lists all methods and attributes of dict
   ```

4. **VSCode Intellisense & Hover**  
   - In VSCode, hover over a class or method to see its docstring.
   - Press `Ctrl+Space` for suggestions and quick docs.

5. **Command Line**  
   - Run: `python -m pydoc list`  
     (Replace `list` with any class/module name.)

---

For DSA and interview prep, the official Python docs and the `help()` function are the most direct ways to check built-in class APIs.

