## ! and % in pip install in notebooks


In notebooks like Jupyter or Colab, these symbols tell the environment to step "outside" the Python code:
### ! (Shell Escape)
When to use: For general system commands like checking files (!ls), moving folders (!mv), or checking your OS version.
How it works: It runs the command in the temporary system terminal (shell).
Risk: For installing packages, it might accidentally install them into the wrong Python version if you have multiple environments.
### % (Magic Command)
When to use: Specifically for %pip install or %conda install.
How it works: It is a "Smart" shortcut designed specifically for notebooks.
Benefit: It guarantees the library is installed directly into the current kernel you are using, preventing "Module Not Found" errors.
Summary: Use `!` for system tasks and `%pip` for installing libraries like PySpark to ensure they actually work in your code.

