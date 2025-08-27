# Data Structures:

### Data Structures in Python

#### 1. Lists
- **Definition**: Ordered, mutable, and can contain mixed data types.
- **Syntax**: `list_name = [element1, element2, ...]`
- **Common Operations**:
  - Access: `list_name[index]`
  - Append: `list_name.append(value)`
  - Remove: `list_name.remove(value)`
  - Sort: `list_name.sort()`

**Example**:
```python
# Creating a list
nums = [1, 2, 3, 4, 5]

# Accessing elements
print(nums[0])  # Output: 1

# Adding an element
nums.append(6)

# Removing an element
nums.remove(3)

# Sorting
nums.sort()
```

#### 2. Tuples
- **Definition**: Ordered, immutable, and can contain mixed data types.
- **Syntax**: `tuple_name = (element1, element2, ...)`
- **Use Case**: When data should not be modified.

**Example**:
```python
# Creating a tuple
coordinates = (10, 20)

# Accessing elements
print(coordinates[0])  # Output: 10
```

#### 3. Dictionaries
- **Definition**: Unordered, mutable, and stores key-value pairs.
- **Syntax**: `dict_name = {key1: value1, key2: value2, ...}`
- **Common Operations**:
  - Access: `dict_name[key]`
  - Add/Update: `dict_name[key] = value`
  - Remove: `del dict_name[key]`

**Example**:
```python
# Creating a dictionary
person = {"name": "Alice", "age": 25}

# Accessing values
print(person["name"])  # Output: Alice

# Adding a key-value pair
person["city"] = "New York"

# Removing a key-value pair
del person["age"]
```

#### 4. Sets
- **Definition**: Unordered, mutable, and contains unique elements.
- **Syntax**: `set_name = {element1, element2, ...}`
- **Common Operations**:
  - Add: `set_name.add(value)`
  - Remove: `set_name.remove(value)`
  - Union: `set1 | set2`
  - Intersection: `set1 & set2`

**Example**:
```python
# Creating a set
unique_nums = {1, 2, 3}

# Adding an element
unique_nums.add(4)

# Removing an element
unique_nums.remove(2)

# Union and Intersection
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)  # Union: {1, 2, 3, 4, 5}
print(set1 & set2)  # Intersection: {3}
```

#### 5. Stacks
- **Definition**: Follows Last In, First Out (LIFO) principle.
- **Implementation**: Use a list with `append()` and `pop()`.

**Example**:
```python
stack = []
stack.append(1)
stack.append(2)
stack.pop()  # Removes 2
```

#### 6. Queues
- **Definition**: Follows First In, First Out (FIFO) principle.
- **Implementation**: Use `collections.deque`.

**Example**:
```python
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.popleft()  # Removes 1
```

#### 7. Linked Lists
- **Definition**: A sequence of nodes where each node points to the next.
- **Implementation**: Use custom classes.

**Example**:
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
```

#### 8. Heaps
- **Definition**: A binary tree where the parent node is greater (max-heap) or smaller (min-heap) than its children.
- **Implementation**: Use `heapq` module.

**Example**:
```python
import heapq

nums = [3, 1, 4, 1, 5]
heapq.heapify(nums)  # Min-heap
heapq.heappush(nums, 2)
print(heapq.heappop(nums))  # Removes smallest element
```

#### 9. Graphs
- **Definition**: A set of nodes connected by edges.
- **Implementation**: Use dictionaries or adjacency lists.

**Example**:
```python
# Adjacency list representation
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}
```

#### Tips for DSA Interviews
1. **Understand Time Complexity**: Know the Big-O for operations on each data structure.
2. **Practice Common Problems**: E.g., reversing a linked list, finding the shortest path in a graph.
3. **Use Built-in Libraries**: Python's `collections` and `heapq` modules are efficient.
4. **Write Clean Code**: Use meaningful variable names and comments.

