
# Python's Data Structures and Utilities Part 1

## Introduction
 
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
In Python, the comparison between arrays and vectors in STL is more aptly represented by comparing Python's list and array (from the array module).

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

**example**

```python 
# Creating and initializing a list
myList = [10, 20, 30]

# Adding elements
myList.append(40) # [10, 20, 30, 40]

# Insert 15 at index 1
myList.insert(1, 15)  # [10, 15, 20, 30, 40]

# Accessing and modifying elements
print("Element at index 2:", myList[2])
myList[2] = 25 # [10, 15, 25, 30, 40]
print("Element at index 2 after updating:", myList[2])

# Iterating over a list
for element in myList:
    print(element, end= " ") # 10 15 25 30 40

print() # printing new line

# Removing elements
removedElement = myList.pop(2)
print("Removed element:", removedElement)

# List length
print("List length:", len(myList))

# Slicing

# Get items from index 1 to 3
subset = myList[1:4]  # Outputs: [15, 30, 40]
print("Subset list from index 1 to index 3:",subset)

# Get every second item from the list
every_second = myList[::2]  # Outputs: [10, 30]
print("Every second item from list:", every_second)

# Reverse the list
reversed_list = myList[::-1]  # Outputs: [40, 30, 15, 10]
print("Reverse list:", reversed_list)

# Clearing the list
myList.clear()

```

In this Python example, a list is used similarly to a vector in C++, showcasing various operations like element addition, access, modification, removal, reversing, and iteration.

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

```python 
from collections import deque

# Creating a deque
myDeque = deque([1, 2, 3])

# Adding elements

# Add to the right end
myDeque.append(4)

# Add to the left end
myDeque.appendleft(0)

# Accessing elements
print("Rightmost element:", myDeque[-1]) #4
print("Leftmost element:", myDeque[0]) # 0

# Removing elements

# Remove from the right end
rightElem = myDeque.pop()

# Remove from the left end
leftElem = myDeque.popleft()

# Iterating over deque
print("Elements in the deque:")
for elem in myDeque:
    print(elem, end=" ")

print() #print new line

# Other operations

# Extend right end
myDeque.extend([5, 6, 7])

# Extend left end
myDeque.extendleft([-1, -2])

# Rotate to the right
myDeque.rotate(2)

print("Elements in the deque after extend and rotate operations:")
for elem in myDeque:
    print(elem, end=" ")

```

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

**example**

```python
# Creating and initializing a list
myList = [1, 2, 3]

# Adding elements
myList.append(4)
myList.insert(1, 1.5)  # Insert 1.5 at index 1

# Accessing and removing elements
print("Element at index 2:", myList[2])
removedElement = myList.pop(2)
print("Removed element:", removedElement)

# Iterating over a list
for element in myList:
    print(element)
```
### Python collections.deque Features and Operations

**Creation:**  
A deque (double-ended queue) can be created empty or with initial elements.

```python
from collections import deque
dequeName = deque([initial_elements])
```

**Adding and Removing Elements:**

- `append(element)`: Adds an element to the right end.
- `appendleft(element)`: Adds an element to the left end.
- `pop()`: Removes and returns an element from the right end.
- `popleft()`: Removes and returns an element from the left end.

**Other Operations:**

- `rotate(n)`: Rotate the deque n steps to the right.
- `maxlen`: Optional argument to limit the maximum size of the deque.

**example**

```python
from collections import deque

# Creating a deque
myDeque = deque([1, 2, 3])

# Adding elements
myDeque.append(4)       # Add to the right end
myDeque.appendleft(0)   # Add to the left end

# Removing elements
rightElem = myDeque.pop()       # Remove from the right end
leftElem = myDeque.popleft()    # Remove from the left end

# Iterating over deque
print("Elements in the deque:")
for elem in myDeque:
    print(elem)
```

The choice between `list` and `deque` depends on the specific requirements of your program, particularly where and how often elements are added and removed.



## Stack

Stacks are data structures that follow the Last-In-First-Out (LIFO) principle, where the last element added to the stack is the first one to be removed.

Using a Python list

Utilizing the `collections.deque` class

### Using a Python list

Python's built-in list is naturally suited for stack operations, using append() to push an element onto the stack and pop() to remove the top element.

This approach is simple and direct but does not enforce the stack discipline explicitly since lists can be accessed at any index.

The following code demonstrates a stack implementation using a list by pushing elements 'a', 'b', and 'c', and then popping each one, which results in an empty stack.

**example**

```python
stack = []
stack.append('a')
stack.append('b')
stack.append('c')
print("Stack after pushing elements:")
print(stack)
print("\nElements popped from the stack:")
print(stack.pop())
print(stack.pop())
print(stack.pop())
print("\nStack after popping elements:")
print(stack)
```

### Using collections.deque

The deque class from the collections module is another popular way to implement a stack in Python. It is optimized for fast appends and pops from both ends.

Using deque for a stack ensures O(1) time complexity for both push and pop operations, unlike lists which can have varying performance for pop operations depending on the size of the list.

This implementation uses append() for push and pop() for the standard pop operation, maintaining stack behavior.

The code below demonstrates using a deque to manage a stack, adding and then removing the same elements 'a', 'b', and 'c', resulting in an empty stack.

***example*** 

```python
from collections import deque
stack = deque()
stack.append('a')
stack.append('b')
stack.append('c')
print("Stack after pushing elements:")
print(stack)
print("\nElements popped from the stack:")
print(stack.pop())
print(stack.pop())
print(stack.pop())
print("\nStack after popping elements:")
print(stack)
```
## Queue

### Implement a Queue in Python

There are multiple approaches to implement a queue in Python:

- Using a Python list
- Utilizing the collections.deque class
- Employing the queue.Queue module

**Using Python List** 

Python's built-in list can function as a queue, using append() for enqueue and pop() for dequeue.

However, lists can be slow for queue operations due to the need to shift elements, resulting in O(n) time complexity.

The code demonstrates queue simulation with a Python list, adding 'a', 'b', and 'c' elements and then dequeuing them, leaving an empty queue

***example*** 

```python 
queue = []
queue.append('a')
queue.append('b')
queue.append('c')
print("Initial queue")
print(queue)
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print("\nQueue after removing elements")
print(queue)
```

**Using collections.deque:**

To implement a queue in Python, the deque class from the collections module can be employed.

Deque is a better choice than a list when fast append and pop operations are required from both ends of the container.

Deque offers O(1) time complexity for these operations, while lists have O(n) complexity.

Instead of enqueue and dequeue, append() and popleft() functions are used.

The code utilizes a deque from the collections module to create a queue.

It adds 'a', 'b', and 'c' elements to the queue and dequeues them using q.popleft(), resulting in an empty queue.

Note that attempting to dequeue from an empty queue with q.popleft() would raise an IndexError.

The code demonstrates queue operations and handles the scenario of an empty queue. 

***example***

```python 
from collections import deque
q = deque()
q.append('a')
q.append('b')
q.append('c')
print("Initial queue")
print(q)
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())

print("\nQueue after removing elements")
print(q)
```

**Using queue.Queue:**

Python includes a built-in module called "queue" for implementing queues.

The queue.Queue(maxsize) function initializes a queue with a maximum size of maxsize.

If maxsize is set to zero (0), it creates an infinite queue.

This queue follows the First-In-First-Out (FIFO) rule.

The module provides several functions:

maxsize: Indicates the maximum number of items allowed in the queue.

empty(): Returns True if the queue is empty, otherwise False.

full(): Returns True if the queue contains maxsize items. If maxsize was set to zero (the default), full() never returns True.

get(): Removes and returns an item from the queue. If the queue is empty, it waits until an item becomes available.

get_nowait(): Returns an item immediately if one is available, otherwise raises QueueEmpty.

put(item): Adds an item to the queue. If the queue is full, it waits until a free slot becomes available before adding the item.

put_nowait(item): Adds an item to the queue without blocking. If no free slot is immediately available, it raises QueueFull.

qsize(): Returns the number of items in the queue.

***example***

The provided code demonstrates the use of the Queue class from the queue module.

It starts with an empty queue, adds 'a', 'b', and 'c' to it, dequeues the items, making the queue empty again, and finally adds '1'.

Despite being empty earlier, the queue remains full because the maximum size is set to 3.

This code illustrates various queue operations, including checking for fullness and emptiness.

```python 
from queue import Queue
q = Queue(maxsize = 3)
print(q.qsize()) 
q.put('a')
q.put('b')
q.put('c')
print("\nFull: ", q.full()) 
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())
print("\nEmpty: ", q.empty())
q.put(1)
print("\nEmpty: ", q.empty()) 
print("Full: ", q.full())
```

## Priority Queue in Python

In Python, a priority queue is a container for elements arranged in a specific priority order.

By default, the highest-priority element is at the front of the queue.

Priority queues are often implemented as binary heaps, which offer efficient operations to maintain the highest-priority element at the top.

### Max Heap or Max Priority Queue in Python

```python
import queue

maxHeap = queue.PriorityQueue()

# Push elements into the max heap priority queue
maxHeap.put(30)  # maxHeap = {30}
maxHeap.put(10)  # maxHeap = {30, 10}
maxHeap.put(50)  # maxHeap = {50, 30, 10}
maxHeap.put(20)  # maxHeap = {50, 30, 20, 10}

# Print the top element (element with the highest priority) without removing it
print("Top element:", maxHeap.queue[0])  # 50

# Pop the top element
maxHeap.get()

# Get the size of the max heap priority queue
print("Size of the priority queue:", maxHeap.qsize())  # 3

# Check if the priority queue is empty
if maxHeap.empty():
    print("The priority queue is empty.")
else:
    print("The priority queue is not empty.")  # Not empty

# Create a second max heap priority queue
maxHeap2 = queue.PriorityQueue()

# Swap the content of the first max heap priority queue with the second one
maxHeap2.queue = maxHeap.queue.copy()

print("After swapping, the first priority queue size:", maxHeap.qsize())  # 0
print("After swapping, the second priority queue size:", maxHeap2.qsize())  # 3 
```

queue.PriorityQueue(): Declare a max-heap priority queue named maxHeap for storing elements.

maxHeap.put(): Push elements into the max-heap priority queue.

maxHeap.queue[0]: Print the top element (with the highest priority) without removing it.

maxHeap.get(): Remove the top element from the max-heap priority queue.

maxHeap.qsize(): Get the size of the max-heap priority queue.

maxHeap.empty(): Check if the max-heap priority queue is empty.

queue.PriorityQueue(): Create a second max-heap priority queue.

maxHeap2.queue = maxHeap.queue.copy(): Swap the content of the first max-heap priority queue with the second one by copying all elements from maxHeap to maxHeap2.

### Min Heap or Min Priority Queue in Python 

```python 
import queue

minHeap = queue.PriorityQueue()

# Push elements into the min heap priority queue
minHeap.put(30)  # minHeap = {30}
minHeap.put(10)  # minHeap = {10, 30}
minHeap.put(50)  # minHeap = {10, 30, 50}
minHeap.put(20)  # minHeap = {10, 20, 30, 50}

# Print the top element (element with the lowest priority) without removing it
print("Top element:", minHeap.queue[0])  # 10

# Pop the top element
minHeap.get()

# Get the size of the min heap priority queue
print("Size of the priority queue:", minHeap.qsize())  # 3

# Check if the priority queue is empty
if minHeap.empty():
    print("The priority queue is empty.")
else:
    print("The priority queue is not empty.")  # Not empty

# Create a second min heap priority queue
minHeap2 = queue.PriorityQueue()

# Swap the content of the first min heap priority queue with the second one
minHeap2.queue = minHeap.queue.copy()

print("After swapping, the first priority queue size:", minHeap.qsize())  # 0
print("After swapping, the second priority queue size:", minHeap2.qsize())  # 3
```

queue.PriorityQueue(): Declare a min-heap priority queue named minHeap for storing elements.

minHeap.put(): Push elements into the min-heap priority queue.

minHeap.queue[0]: Print the top element (with the lowest priority) without removing it.

minHeap.get(): Remove the top element from the min-heap priority queue.

minHeap.qsize(): Get the size of the min-heap priority queue.

minHeap.empty(): Check if the min-heap priority queue is empty.

queue.PriorityQueue(): Create a second min-heap priority queue.

minHeap2.queue = minHeap.queue.copy(): Swap the content of the first min-heap priority queue with the second one by copying all elements from minHeap to minHeap2.


## Ordered Set in Python

An Ordered Set is a container in Python that simulates the behavior of a set while maintaining the order of elements as they were inserted. It does not allow duplicate values.

### Properties 

Sorted: Partially, the elements are stored in the order they were added.
Unique: Yes, it allows only unique elements.

### Basic Operations 

```python 
from collections import OrderedDict

class OrderedSet:
    def __init__(self):
        self._data = OrderedDict()

    def add(self, item):
        self._data[item] = None

    def remove(self, item):
        del self._data[item]

    def discard(self, item):
        self._data.pop(item, None)

    def __contains__(self, item):
        return item in self._data

    def __iter__(self):
        return iter(self._data)

    def __repr__(self):
        return '{' + ', '.join(map(str, self._data)) + '}'

# Create an ordered set and insert elements
s = OrderedSet()
s.add(1)  # {1}
s.add(3)  # {1, 3}
s.add(5)  # {1, 3, 5}
s.add(7)  # {1, 3, 5, 7}
s.add(3)  # {1, 3, 5, 7} --> 3 doesn't get inserted

print(s)

# Erase elements from the ordered set
s.remove(3)  # Erase element '3'
s.discard(7)  # Erase element '7' using discard (won't raise an error if the element is not present)

print(s)

for i in [2, 4, 6, 8, 10]:
    s.add(i)

print(s)

count8 = 1 if 8 in s else 0
count5 = 1 if 5 in s else 0
print("Count of 8 in the set:", count8)  # 1
print("Count of 5 in the set:", count5)  # 0
```

OrderedSet(): Create an empty ordered set.

s.add(): Insert elements into the ordered set.

s.remove(): Erase elements from the ordered set by value.

s.discard(): Erase elements from the ordered set using the discard method.

element in s: Check if specific value (element) exists in the ordered set.


## Multi-Set in Python

A Multi-Set in Python, also known as a Bag, is a container that allows you to store multiple values of the same type in a sorted order.

Unlike a Set, it can contain duplicate elements.

### Properties 

Sorted: Yes, the elements are stored in sorted order.
Unique: No, it allows duplicate elements.

### Basic Operations 

```python 
from collections import Counter

# Create a Multi-Set using Counter
multi_set = Counter()

# Insert elements into the Multi-Set
multi_set.update([5])  # {5}
multi_set.update([2])  # {2, 5}
multi_set.update([5])  # {2, 5, 5}
multi_set.update([8])  # {2, 5, 5, 8}
multi_set.update([2])  # {2, 2, 5, 5, 8}
multi_set.update([5])  # {2, 2, 5, 5, 5, 8}
multi_set.update([9])  # {2, 2, 5, 5, 5, 8, 9}

# Erase elements from the Multi-Set
multi_set.subtract([5])  # {2, 2, 8, 9}

# Find
if 2 in multi_set:
    print("Found:", 2)  # Found

# Count
count = multi_set[2]
print("Count of 2:", count)  # 2
```

Counter(): Create a Multi-Set using Python's Counter class, which allows duplicate elements and maintains sorted order.

multi_set.update(): Insert elements into the multi_set using the update method.

multi_set.subtract(): Erase elements from the multi_set using the subtract method.

if element in multi_set:: Use this condition to check if a specific element exists in the multi_set.

multi_set[element]: Access the count of occurrences of a specific element in the multi_set.

## Unordered Set in Python

An Unordered Set in Python can be represented by the set data structure.

It is a container that stores a collection of unique elements in a way that allows for fast retrieval, but it does not maintain a specific order among the elements.

### Properties 

Sorted: No, the elements are stored in a random order.

Unique: It allows only unique elements.

### Basic Operations 

```python 
# Creating an unordered set
my_set = set()

# Insert operation
my_set.add(3)
my_set.add(4)
my_set.add(2)
my_set.add(0)
my_set.add(3) # Already exists, doesn't get added
my_set.add(2) # Already exists, doesn't get added
my_set.add(3) # Already exists, doesn't get added
# my_set = {0, 2, 3, 4} -> random order and just an example
print(my_set)
# Erase operation
my_set.remove(2)
print(my_set)
# Find operation
if 3 in my_set:
    print("Found 3")  # Found 3
else:
    print("Not found")

# Count operation
count = sum(1 for element in my_set if element == 0)
print("Count of 0:", count)  # 1
```

set(): Create an empty unordered set.

my_set.add(): Insert elements into the my_set using the add method.

my_set.remove(): Remove elements from the my_set using the remove method.

if element in my_set: Use the in operator to check if a specific value exists in the my_set.

Count operation: You can count the occurrences of a specific element using a generator expression.

In Python, the set provides average constant-time complexity for basic operations, and it uses hash-based indexing for efficient retrieval. However, the order of elements is not guaranteed to be maintained.

---

# Python's Data Structures and Utilities Part 3

## Map in Python

In Python, a map is not a built-in data structure like it is in C++. Instead, the closest equivalent is a dictionary (dict), which stores key-value pairs.

Like maps in C++, Python dictionaries allow efficient retrieval, insertion, and deletion of elements, but they are inherently unordered prior to Python 3.7 and do not sort keys automatically.

### Syntax

```python
new_dict = {'key1': 'value1', 'key2': 'value2'}
```

### Real-Life Use Cases

A common real-life use case for a dictionary in Python could be storing product IDs as keys and their details or prices as values.

This allows quick access to product information based on its ID.

### Key-Value Pair

In Python, a key-value pair is stored in a dictionary. Each key is associated with a value, and the keys in a dictionary are unique.

### Types of Declarations 

You can declare a dictionary in Python with various data types as keys and values. Common examples include:

dict[int, int]: Dictionary with integer keys and integer values.

dict[int, tuple[int, int]]: Dictionary with integer keys and a tuple of integers as values.

dict[tuple[int, int], int]: Dictionary with a tuple of integers as keys and integer values.

dict[str, str]: Dictionary with string keys and string values.

### Implementation Example

```python
# Sample Python code demonstrating dictionary usage
my_dict = {1: 3, 2: 5, 3: 8}

my_dict[4] = 9  # Adding a new key-value pair
my_dict[3] = 7  # Updating the value associated with key 3

for key, value in my_dict.items():
    print(key, value)

print(my_dict.get(4))  # Returns 9
print(my_dict.get(10, "Not Found"))  # Returns 'Not Found' as 10 is not a key in the dictionary

# Checking if a key exists in the dictionary
if 2 in my_dict:
    print("Found:", my_dict[2])
```

#### Explanation

dict: The Python dictionary (dict) is a built-in data type that stores key-value pairs.

my_dict[key] = value: Adds a new key-value pair to the dictionary or updates the value if the key already exists.

my_dict.get(key, default): Returns the value for the key if the key is in the dictionary, else default.

if key in my_dict: Checks if a key is in the dictionary.

## MultiMap in Python

In Python, a direct equivalent of a MultiMap as seen in C++ or Java isn't part of the standard library.

However, similar functionality can be achieved using a dictionary with lists as values, or by using the defaultdict class from the collections module. This allows storing multiple values for the same key.

### Syntax (Using defaultdict) 

```python
from collections import defaultdict
multi_map = defaultdict(list)
```

### Properties 

Uniqueness: No, Python's MultiMap equivalent allows for multiple values to be associated with a single key.

Unsorted: By default, the order of keys in a Python dictionary is not sorted. However, from Python 3.7 onwards, dictionaries maintain the order of insertion.

### Real-Life Use Cases

A MultiMap-like structure in Python can be used in scenarios such as grouping data by a certain attribute.

For instance, grouping students' names by their grades, where the grade is the key, and the students' names are the values.

### Implementation Example 

```python 
from collections import defaultdict

# Creating a MultiMap-like structure
multi_map = defaultdict(list)

# Adding values
multi_map['apple'].append(1)
multi_map['apple'].append(2)
multi_map['banana'].append(3)

# Iterating over the MultiMap
for key, values in multi_map.items():
    print(key, values)

# Checking if a key exists
if 'apple' in multi_map:
    print("Apples:", multi_map['apple'])

# Adding more values
multi_map['apple'].extend([3, 4])
```
#### Explanation 

defaultdict(list): Creates a dictionary-like object where each key is associated with a list of values.

multi_map['key'].append(value): Adds a value to the list associated with 'key'.

for key, values in multi_map.items(): Iterates over the MultiMap, retrieving each key and its list of values.

if 'key' in multi_map: Checks if 'key' exists in the MultiMap.

multi_map['key'].extend([value1, value2]): Adds multiple values to the list associated with 'key'.

## Algorithms in Python

Python offers a variety of built-in functions and libraries that can be used to perform the same algorithms as C++. Here's how you can achieve similar functionalities in Python:

### Sorting 

In Python, you can use the sorted() function or the .sort() method on lists.

```python 
#Sorting an Array
a = [13, 5, 17, 9, 70, 43, 15]
a.sort()  # Sorts the list in ascending order in place
print(a)

#Sorting an Subarray
a = [13, 5, 17, 9, 70, 43, 15]
a[2:5] = sorted(a[2:5])  # Sorts the sublist from index 2 to 4
print(a)

#Sorting an Array in Reverse Order
a = [13, 5, 17, 9, 70, 43, 15]
a.sort(reverse=True)  # Sorts the list in descending order
print(a)

#Sorting an Array using Custom Sorting
arr = [(8, 4), (5, 2), (8, 6)]
arr.sort(key=lambda x: (x[0], -x[1]))  # Custom sorting using a lambda function
print(arr)
```

### Counting Set Bits 

Python uses the bin() function to get the binary representation of a number, which can then be used to count set bits.

```python 
i = 5
print(bin(i).count('1'))

j = 987654321444333
print(bin(j).count('1'))
```
### Generating Permutations 

Python's itertools library provides a method to generate permutations. 

```python 
import itertools

str = "bac"
# Sorting the string first
str = ''.join(sorted(str))

for perm in itertools.permutations(str):
    print(''.join(perm))
```

### Finding the Maximum Element

```python 
max_element = max(a)
print(max_element)
```
