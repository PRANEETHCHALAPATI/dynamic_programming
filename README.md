# Python's Data Structures and Utilities - Part 1

## 🚀 Introduction

Python offers robust built-in and standard library tools for data handling:

- **Built-in Structures**: Lists, Tuples, Sets, Dictionaries
- **Standard Libraries**: `collections`, `heapq`, `bisect`, `itertools`

---

## 📅 Containers Overview

### Lists vs Arrays

| Aspect           | Arrays (from array module) | Lists                   |
| ---------------- | -------------------------- | ----------------------- |
| Size Flexibility | Fixed-type, efficient      | Fully dynamic, flexible |
| Initialization   | Homogeneous types          | Mixed types allowed     |
| Operations       | Basic                      | Rich set of methods     |

```python
from array import array
arr = array('i', [1, 2, 3])  # int array
lst = [1, "two", 3.0]        # mixed types
```

---

## 🔹 Python Lists

```python
myList = [10, 20, 30]
myList.append(40)
myList.insert(1, 15)
print(myList[2])     # Access
myList[2] = 25       # Modify
print(myList)

for element in myList:
    print(element, end=" ")

removed = myList.pop(2)
print("Removed:", removed)
print("Length:", len(myList))

subset = myList[1:4]
every_second = myList[::2]
reversed_list = myList[::-1]
print(subset, every_second, reversed_list)

myList.clear()
```

---

## 🛋️ Deque (Double-Ended Queue)

```python
from collections import deque
myDeque = deque([1, 2, 3])
myDeque.append(4)
myDeque.appendleft(0)

print("Right:", myDeque[-1])
print("Left:", myDeque[0])

right = myDeque.pop()
left = myDeque.popleft()

for elem in myDeque:
    print(elem, end=" ")

myDeque.extend([5, 6, 7])
myDeque.extendleft([-1, -2])
myDeque.rotate(2)

print("After rotate:", list(myDeque))
```

---

## 🔺 Stack (LIFO)

### Using List

```python
stack = []
stack.append('a')
stack.append('b')
stack.append('c')
print(stack.pop())
print(stack)
```

### Using deque

```python
from collections import deque
stack = deque()
stack.append('a')
stack.append('b')
stack.append('c')
print(stack.pop())
print(stack)
```

---

## 🚗 Queue (FIFO)

### Using List (Not Recommended)

```python
queue = []
queue.append('a')
queue.append('b')
queue.append('c')
print(queue.pop(0))
```

### Using deque

```python
from collections import deque
queue = deque()
queue.append('a')
queue.append('b')
queue.append('c')
print(queue.popleft())
```

### Using queue.Queue

```python
from queue import Queue
q = Queue(maxsize=3)
q.put('a')
q.put('b')
q.put('c')
print(q.get())
print("Empty:", q.empty())
print("Full:", q.full())
```

---

## 📊 Priority Queue

### Min Heap (default)

```python
from queue import PriorityQueue
pq = PriorityQueue()
pq.put(3)
pq.put(1)
pq.put(2)
print(pq.get())  # 1
```

### Max Heap

```python
pq = PriorityQueue()
pq.put((-1, "high"))
pq.put((-3, "urgent"))
pq.put((-2, "medium"))
print(pq.get()[1])  # urgent
```

---

## 📋 Ordered Set

```python
# Simulated using dict
ordered_set = dict.fromkeys([3, 1, 2])
print(list(ordered_set.keys()))
```

---

## 🤝 Multi-Set (Bag)

```python
from collections import Counter
multi_set = Counter([1, 1, 2, 3])
multi_set.update([2, 2])
print(multi_set[2])  # 3
multi_set.subtract([1])
print(multi_set)
```

---

## 🔐 Unordered Set

```python
s = set()
s.add(1)
s.add(2)
s.remove(1)
print(2 in s)
```

---

## ✅ Quick Comparison

| Structure     | Use Case                          |
| ------------- | --------------------------------- |
| List          | General-purpose, dynamic sequence |
| Deque         | Fast front/back ops (queue/stack) |
| Stack (Deque) | LIFO structure                    |
| Queue (Deque) | FIFO structure                    |
| PriorityQueue | Min/Max heap                      |
| Ordered Set   | Unique items with insertion order |
| Multi-Set     | Count duplicates                  |
| Unordered Set | Unique, fast membership checks    |

---

## 🧠 Pro Tip

Use `itertools`, `bisect`, `heapq` for advanced manipulation in Part 2.

## 💼 License

MIT - Free for education, learning, and non-commercial use.

