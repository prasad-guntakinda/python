# Collection

        1. List
        2. Tuple
        3. Set
        4. Dict
        5. Range function



---

## 5. range() function:

            - Syntax
            - Examples
            - Display Ranges
            - Slicing Ranges
            - Membership Testing
            - Practices
           
- The built-in range() function returns an immutable sequence of numbers, commonly used for looping a specific number of times.
- This set of numbers has its own data type called range.

- The range() function in Python generates an immutable sequence of integers. 
- The arguments ``start``, ``stop``, and ``step`` define where the sequence begins, ends, and the interval between numbers, respectively. 
- Syntax:

````python

n =  range(start, stop, step) # start and step are optional parameters

for num in n:
    print(num) # prints values from 0 to n-1

````

### Parameters
- The range() function accepts up to three integer arguments. 

- ``start (optional):`` The starting integer of the sequence. The number is __inclusive__ in the sequence. If omitted, the default value is ``0``.
- ``stop (required):`` The endpoint of the sequence. The number at the stop value is __exclusive__, meaning it is the limit and is not included in the generated sequence.
- ``step (optional):`` The difference between consecutive numbers in the sequence. The default value is ``1``. This can be a positive or negative integer, but it cannot be zero, as this would raise a ``ValueError``

### Display:

- The range object is a data type that represents an immutable sequence of numbers, and it is not directly displayable.
- Therefore, ranges are often converted to lists for display.

````python
print(list(range(5)))
print(list(range(1, 6)))
print(list(range(5, 20, 3)))
````

### Key Characteristics

- __Integer Only:__ All arguments (start, stop, and step) must be integers. 
- __Memory Efficient:__ range() returns a range object, which is an iterable that generates numbers on the fly, rather than creating a complete list in memory. This makes it efficient for large sequences.

- __Usage:__ It is most commonly used with for loops to iterate a specific number of times. 

- Examples
  
| Syntax                   | Example                | Sequence Generated              |
| ------------------------ | ---------------------- | ------------------------------- |
| range(stop)              | list(range(5))         | [0, 1, 2, 3, 4]                 |
| range(start, stop)       | list(range(2, 6))      | [2, 3, 4, 5]                    |
| range(start, stop, step) | list(range(0, 10, 2))  | [0, 2, 4, 6, 8]                 |
| Negative step            | list(range(10, 0, -1)) | [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] |

- You can use the built-in list() function, as shown above, to display all the numbers in the range object.

### Practices:
- 
---

## Practices:
1. List – Second Largest Number: Given a list of numbers, find second largest without using built-in sort.
2. List – Remove Negative Numbers
3. Find Unique Words
4. Student Average
    ````python
    marks = {
    "Math": 80,
    "Science": 70,
    "English": 90
    }
    ````
5. Tuple –  Swap values without converting to list.
6. 
   