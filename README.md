
# Python's Data Structures and Utilities Part 1

## Introduction

Lists  
Introduction  
Python is known for its comprehensive set of built-in data structures, such as lists, dictionaries, sets, and tuples, which are highly flexible and easy to use.

Additionally, the Python standard library includes modules like collections, heapq, bisect, and itertools that provide specialized data structures and algorithmic tools.

## Fundamental Components in Python

**Containers:**  
Python's built-in container types include lists (similar to vectors in STL), dictionaries (similar to maps), sets, and tuples. The collections module further extends this with specialized container datatypes like namedtuple, deque, Counter, OrderedDict, and more.

**Algorithms:**  
Python doesn't have a dedicated algorithms library like STL. However, many common operations such as sorting (sorted(), .sort()), searching (in keyword, .index()), and more complex manipulations (itertools module) are readily available.

**Iterators:**  
Iterators are a core part of Python, used to iterate over collections. Python's iterator protocol and generator functions (yield) allow for efficient looping over containers.

**Function Objects (Callables):**  
In Python, functions and any objects that can be called (implementing __call__) serve as function objects. Lambda functions and regular functions are often used in conjunction with container methods (like map(), filter(), sorted()) for custom behavior.

## Arrays vs. Lists in Python

| Aspect              | Arrays (from array module)                                               | Lists                                                                         |
|---------------------|--------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| Size Flexibility    | Arrays have a dynamic size but are constrained to storing elements of the same type. | Lists are inherently dynamic, can grow or shrink, and can contain elements of different types. |
| Initialization      | Arrays can be initialized with elements of a fixed type. They are useful for numerical data due to their efficient storage. | Lists can be initialized dynamically and are more flexible for general-purpose use. |
| Functions           | Arrays provide basic operations like adding, removing, and accessing elements but are limited compared to lists. | Lists offer a wide range of built-in methods for various operations, making them versatile for many tasks. |

## Python Lists

Python lists are versatile, allowing for dynamic resizing and supporting a variety of operations similar to C++ vectors.

### Key Features and Methods of Python Lists

**Creation and Initialization:**

Lists can be created empty or with initial elements.

Syntax: `listName = []` or `listName = [element1, element2, ...]`

**Adding Elements:**

- `append(element)`: Adds an element to the end of the list.
- `insert(index, element)`: Inserts an element at a specified index.

**Accessing and Modifying Elements:**

Elements are accessed and modified by their index, e.g., `listName[index]`.

**Removing Elements:**

- `pop()`: Removes and returns the last element.
- `pop(index)`: Removes and returns the element at the specified index.
- `remove(value)`: Removes the first occurrence of the specified value.

**Other Useful Operations:**

- `len(listName)`: Returns the number of elements in the list.
- `listName.clear()`: Removes all elements from the list.
- Iteration, slicing, and more.

---

# Python's Data Structures and Utilities Part 2

## Deque  
## List  
## Stack  
## Queue  
## Priority Queue  
## Ordered Set  
## Multi-Set  
## Unordered Set

## Deque

### Key Features and Methods of Python deque

**Creation:**  
A deque can be created empty or with initial elements.

**Adding Elements:**

- `append(element)`: Add an element to the right end (similar to back in C++).
- `appendleft(element)`: Add an element to the left end (similar to front in C++).

**Accessing Elements:**  
Elements in a deque can be accessed via indexing, e.g., `dequeName[index]`, but this is less efficient than in lists.

**Removing Elements:**

- `pop()`: Remove and return an element from the right end.
- `popleft()`: Remove and return an element from the left end.

**Other Useful Operations:**

- `extend(iterable)`, `extendleft(iterable)`: Add multiple elements at once.
- `rotate(n)`: Rotate the deque n steps to the right.
- `maxlen`: Optional argument to limit the maximum size of the deque.

**Example:**  
In this Python example, a deque is used to demonstrate adding, accessing, and removing elements, as well as other operations like extending and rotating.

The deque class in Python provides a balanced and efficient implementation for frequent insertions and deletions at both ends.

## Python List and collections.deque

### Python List

**Creation and Initialization:**  
Lists can be created empty or with initial elements.

**Adding and Removing Elements:**

- `append(element)`: Adds an element to the end of the list.
- `insert(index, element)`: Inserts an element at the specified index.
- `pop()`: Removes and returns the last element.
- `pop(index)`: Removes and returns the element at the specified index.

**Accessing Elements:**  
Elements are accessed by their index, e.g., `listName[index]`.

**Other Operations:**

- `len(listName)`: Returns the number of elements in the list.
- `listName.clear()`: Removes all elements from the list.
- Iteration, slicing, and more.

### Python collections.deque Features and Operations

**Creation:**  
A deque (double-ended queue) can be created empty or with initial elements.

**Adding and Removing Elements:**

- `append(element)`: Adds an element to the right end.
- `appendleft(element)`: Adds an element to the left end.
- `pop()`: Removes and returns an element from the right end.
- `popleft()`: Removes and returns an element from the left end.

**Other Operations:**

- `rotate(n)`: Rotate the deque n steps to the right.
- `maxlen`: Optional argument to limit the maximum size of the deque.

The choice between list and deque depends on the specific requirements of your program, particularly where and how often elements are added and removed.

## Stack

Stacks are data structures that follow the Last-In-First-Out (LIFO) principle, where the last element added to the stack is the first one to be removed.

### Using a Python list

Python's built-in list is naturally suited for stack operations, using append() to push an element onto the stack and pop() to remove the top element.

This approach is simple and direct but does not enforce the stack discipline explicitly since lists can be accessed at any index.

### Using collections.deque

The deque class from the collections module is another popular way to implement a stack in Python. It is optimized for fast appends and pops from both ends.

Using deque for a stack ensures O(1) time complexity for both push and pop operations, unlike lists which can have varying performance for pop operations depending on the size of the list.

## Queue

### Implement a Queue in Python

There are multiple approaches to implement a queue in Python:

- Using a Python list
- Utilizing the collections.deque class
- Employing the queue.Queue module

**Using collections.deque:**

To implement a queue in Python, the deque class from the collections module can be employed.

Deque is a better choice than a list when fast append and pop operations are required from both ends of the container.

Deque offers O(1) time complexity for these operations, while lists have O(n) complexity.

Instead of enqueue and dequeue, append() and popleft() functions are used.

Note that attempting to dequeue from an empty queue with q.popleft() would raise an IndexError.

## Priority Queue in Python

In Python, a priority queue is a container for elements arranged in a specific priority order.

By default, the highest-priority element is at the front of the queue.

Priority queues are often implemented as binary heaps, which offer efficient operations to maintain the highest-priority element at the top.

## Ordered Set in Python

An Ordered Set is a container in Python that simulates the behavior of a set while maintaining the order of elements as they were inserted. It does not allow duplicate values.

## Multi-Set in Python

A Multi-Set in Python, also known as a Bag, is a container that allows you to store multiple values of the same type in a sorted order.

Unlike a Set, it can contain duplicate elements.

## Unordered Set in Python

An Unordered Set in Python can be represented by the set data structure.

It is a container that stores a collection of unique elements in a way that allows for fast retrieval, but it does not maintain a specific order among the elements.

---

# Python's Data Structures and Utilities Part 3

## Map

In Python, a map is not a built-in data structure like it is in C++. Instead, the closest equivalent is a dictionary (`dict`), which stores key-value pairs.

Like maps in C++, Python dictionaries allow efficient retrieval, insertion, and deletion of elements, but they are inherently unordered prior to Python 3.7 and do not sort keys automatically.

### Syntax

```python
new_dict = {'key1': 'value1', 'key2': 'value2'}
```
### Implementation Example

```python
# Sample Python code demonstrating dictionary usage
my_dict = {1: 3, 2: 5, 3: 8}

my_dict[4] = 9  # Adding a new key-value pair
my_dict[3] = 7  # Updating the value associated with key 3

for key, value in my_dict.items():
    print(key, value)

print(my_dict.get(4))           # Returns 9
print(my_dict.get(10, "Not Found"))  # Returns "Not Found" since key 10 does not exist
```


## Real-Life Use Cases

A common real-life use case for a dictionary in Python could be storing product IDs as keys and their details or prices as values.

This allows quick access to product information based on its ID.

## Key-Value Pair

In Python, a key-value pair is stored in a dictionary. Each key is associated with a value, and the keys in a dictionary are unique.

## Types of Declarations

You can declare a dictionary in Python with various data types as keys and values. Common examples include:

- `dict[int, int]`
- `dict[int, tuple[int, int]]`
- `dict[tuple[int, int], int]`
- `dict[str, str]`

## MultiMap in Python

In Python, a direct equivalent of a MultiMap as seen in C++ or Java isn't part of the standard library.

However, similar functionality can be achieved using a dictionary with lists as values, or by using the defaultdict class from the collections module.

## Algorithms in Python

Python offers a variety of built-in functions and libraries that can be used to perform the same algorithms as C++. Here's how you can achieve similar functionalities in Python:

- **Sorting**
- **Counting Set Bits**
- **Generating Permutations**
- **Finding the Maximum Element**
