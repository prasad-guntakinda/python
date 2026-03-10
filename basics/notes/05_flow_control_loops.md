# Loops

- Python has two primary types of loops: 
- ``while`` loop: used for __indefinite iteration as long as a condition is true__
- ``for`` loop, used for __definite iteration over a sequence of items__
  
## while Loop

- The ``while`` loop is a condition-based loop. 
- It keeps running as long as a specific boolean condition remains ``True``
- Requires manual initialization and update of the condition variable within the loop body to avoid infinite loops.
- __Best for:__ It is best used when the number of iterations is not known in advance, such as when waiting for user input or monitoring a system status.

### Syntax:

```python
while condition:
    # loop body - statements to execute
    # remember to update a variable in the condition to avoid an infinite loop

```

### Examples: 
1. Greet user until they type 'quit'
2. countdown till 10 (manual increment/decrement)
3. 
#### 1. Greet user until they type 'quit'.

```python
user_name = ""

while user_name != "quit":
    print("Welcome ", user_input)
    user_name = input("Enter name to Greet, type 'quit' to exit")
```




---

## for loop:

- The ``for`` loop is an iterator-based loop. 
- It is used when you want to step through a sequence (like a list, tuple, string, or range).
- Executes a block of code once for each item in the sequence. 
- Iteration and variable management are handled automatically by the loop structure and the iterable (e.g., range()).
- __Best for:__ When you know the number of iterations in advance or need to process every item in a collection

### Syntax:

```python
for temp_var in sequence:
    # loop body - statements to execute for each item

```

### Examples-1: Printing each item in a list

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Current fruit: {fruit}")

```

### Example-2: Using range(): 
- The ``range()`` function is commonly used with for loops to iterate a specific number of times.

```python
for i in range(5):
    # loop runs for i = 0, 1, 2, 3, 4
    print(i)

```


---

## Key Differences

| Parameter | for Loop | while Loop |
| -------- | -------- | ---------- |
| Control |	Controlled by the sequence length. | Controlled by a boolean condition. |
| Iterations | Number of iterations is typically known in advance. | Number of iterations is generally unknown beforehand. |
| Usage | Iterating through lists, dicts, ranges. |	User input, game loops, waiting for data. |
| Efficiency | Generally more efficient when iterating over sequences. | Can be less efficient due to repeated condition checks but more flexible for dynamic conditions. |

---

## Practices:

1. Sum of First N Numbers: Using while loop, calculate sum of numbers from 1 to N.
2. Print Multiplication Table: Using for loop, print table of a given number (1 to 10).
3. Count Vowels in String: Given a string, count number of vowels.
4. Print Numbers Divisible by 3: Print numbers from 1 to 50 divisible by 3.
5. Factorial Using While: Calculate factorial of a number using while loop.
6. Count Digits in Number
````text
    Input: 12345
    Output: 5
````

7. Sum of Elements in List: Given a list, calculate sum using loop (without sum()).
8. print pattern:

````text
*
**
***
****
*****
````

9. 


Basic Questions
- Print Numbers: Write a program that uses a while loop to print numbers from 1 to 10.
- Countdown: Write a program that takes a starting integer from the user and counts down to zero, printing each value.
- Simple Greeting: Use a while loop to print a message (e.g., "Hello, Python!") three times.
- Even Numbers: Write a program to display all even numbers up to a number N provided by the user. 

Intermediate Questions
- Sum of Natural Numbers: Calculate the sum of the first N natural numbers (e.g., if N is 5, the sum is 1+2+3+4+5).
- Multiplication Table: Print the multiplication table of a number entered by the user using a while loop.
- Factorial Calculator: Write a program to find the factorial of a given non-negative integer.
- Sum of Digits: Calculate the sum of the digits of a number (e.g., for 1234, the sum is 1+2+3+4=10).
- Reverse a Number: Reverse a given integer number (e.g., input 1234, output 4321). 

Advanced Questions
Password Checker: Create a program that repeatedly prompts a user for a password until the correct one is entered. You can extend this by adding a maximum number of attempts before locking the user out.
Fibonacci Sequence: Generate and print the Fibonacci sequence up to N terms.
Prime Number Checker: Determine if a given positive integer is a prime number using a while loop.
User Input Loop with Stop Condition: Write a program that keeps taking input from the user until they enter a specific word, like 'STOP' or a negative number.
Average Calculator: Take a series of numbers from the user and return their average. Use an empty input or a specific value (like a negative number) as the stop criterion.   