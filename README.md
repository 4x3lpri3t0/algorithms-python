# algorithms-python

A repository for algorithms and competitive programming problems with solutions implemented in Python.

# How to read input in Python in Online Judges

If you have to read numbers a b c d...

## Method 1a: Using a list comprehension

```python
a, b, c, d = [int(x) for x in input().split()]
```

## Method 1b: Using the map function

```python
a, b, c, d = map(int, input().split())
```

A faster way is to use stdin and stdout:

## Method 2a: List comprehension with stdin and stdout

```python
from sys import stdin, stdout
a, b, c, d = [int(x) for x in stdin.readline().rstrip().split()]
stdout.write( str(a*b*c\*d) + "\n" )
```

## Method 2b: Map with stdin and stdout

```python
from sys import stdin, stdout
a, b, c, d = map( int, stdin.readline().rstrip().split() )
stdout.write( str(a*b*c*d) + "\n" )
```

Note that you have to convert the output a*b*c\*d to a string when passing it to the function stdout.write(…).

# To Review

## Old

- [ ] is_first_come_first_served -> Easy but tricky logic
- [ ] sherlock-and-anagrams -> Combinations
- [ ] highest-product-of-3 -> Greedy
- [ ] get_rotation_point_index -> BS
- [ ] find_repeat -> BS (Space)[Pigeonhole principle]
- [ ] is_balanced -> BT, DFS, inf -inf and tuples
- [ ] is_binary_search_tree -> BST, DFS, inf -inf and triplets
- [ ] find_second_largest -> BST, edge cases ### PEP 8 ###
- [ ] color_graph -> Graph, set
- [ ] get_path -> Graph, BFS

## 2022

### Arrays

- [ ] 09-buy_and_sell_stock_twice -> First one was easy, second one requires an extra twist

# Language syntax

## Strings

```python
# Count char appearances in string (Linear)
astring = "Hello world!"
astring.count("l") # 3

# Slice
astring[3:4] # l

# Step (1: all of them, 2: even...) [start:stop:step]
astring[0:5:1] # Hello
astring[0:5:2] # Hlo

# Reverse string
astring[::-1]

# startswith / endswith
astring = "Hello world!"
print(astring.startswith("Hello")) # True
print(astring.endswith("asdfasdfasdf")) # False

# split
words = astring.split(" ") # ['Hello', 'world!']
```

## Conditions

```python
# if ... in
name = "John"
list = ["John", "Rick"]
if name in list:
    print("Name is either John or Rick.")

# if ... is
if statement is True:

# ==
if x == 2:

# The 'is' operator
# Unlike the double equals operator "==", the "is" operator does not match the values of the variables, but the instances themselves
x = [1,2,3]
y = [1,2,3]
print(x == y) # True
print(x is y) # False

# not
not False # True

# not equal
!=

# None
none_var = None
if not none_var: # True
```

## Loops

```python
for index, value in enumerate(values):
for index, value in enumerate(values, start=1):
for value in values:
for i in range(n): # 0, 1 ... n
for i in range(1, n): # 1, 2 ... n

# range with step
for x in range(3, 8, 2):
    print(x) # 3, 5 ,7

# while
while True:

# break, continue
```

## Classes and Objects

```python
# Stack with constant getMin() time
class MinStack:
    def __init__(self):
        # Each element in the stack will be a tuple, (x, y). x is value, y is min value at the time.
        self.stack = []

    def push(self, x: int) -> None:
        if self.stack:
            self.stack.append((x, min(x, self.stack[-1][1])))
        else:
            self.stack.append((x, x))

    def pop(self) -> None:
        if not self.stack:
            return None

        popped = self.stack.pop()
        return popped

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1][0]

    def getMin(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1][1]


# MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# top_value = obj.top()
# min_value = obj.getMin()
```

## Dictionary

```python
phonebook = {}
phonebook["John"] = 666
print(phonebook) # {'John': 666}

phonebook = {
    "John" : 666
}
print(phonebook) # {'John': 666}

# Iterating - .items() .keys() .values()
for key, value in dictionary.items():

# del or pop(key)
# If you do not wish to use the returned value, then  del list[1]  is a better choice as
# it gives the programmer instant impression that this value is being discarded and not popped into some other variable.
del phonebook["John"]
phonebook.pop("John")

# in, not in dictionary
if key in dictionary:
if key not in dictionary:
```

## Lists

```python
# Reverse
a = [1,2,4,5,1000]
a.sort(reverse=True) # [1000,5,4,2,1]

# List traversal
range(start, stop, hop)
range(n) # [0,1,...,n-1]
range(1,n) # [1,...,n-1]
range(1,n,2) # [1,3,5,...,n-1] if n is even, or [1,3,5,...,n-2] if n is odd
range(n,-1,-1) # [n,n-1,n-2,...,0]
range(len(arr)) # Provides indices of an array arr
range(len(arr)-1,-1,-1) # Provides indices of arr backwards

# List slicing
arr[w:s] # Wait w elements, start copy (:), stop before reaching index s
arr = [1,2,3,4]
arr[1:] = [2,3,4]
arr[:2] = [1,2]

#List manipulation
arr = [1,2,3]
[str(x) for x in arr] # Output: ['1','2','3']
map(lambda x: str(x), arr) # Output: ['1','2','3']
[str(x) for x in arr if x%2] # Output: ['1','3']

# collections.deque -> All ops k time
append(x)
appendleft(x)
clear()
extend(iterable)
extendleft(iterable)
pop()
popleft()

remove(value)
    Removed the first occurrence of value. If not found, raises a ValueError. New in version 2.5.

rotate(n)
    Rotate the deque n steps to the right. If n is negative, rotate to the left. Rotating one step to the right is equivalent to: "d.appendleft(d.pop())".

# List as stack
arr = [1,2,3]
arr.append(x) #stack.push(x)
arr.pop() # stack.pop()
arr[-1] # stack.peek()
```

## List Comprehensions

Create a new list based on another list.

```python
sentence = "Hello to the world"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
print(words)
print(word_lengths) # [5, 2, 5]

numbers = [34.6, -203.4, 44.9, -12.2]
newlist = [num for num in numbers if num > 0]
print(newlist) # [34.6, 44.9]
```

## Sets

```python
empty_set = set()

# .split()
set("my name is Axel and Axel is my name".split()) # {'my', 'and', 'is', 'name', 'Axel'}

a = set(["Jake", "John", "Jake"])
print(a) # {'Jake', 'John'}

# .intersection()
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])
a.intersection(b) # {'John'}
b.intersection(a) # {'John'}

# .symmetric_difference()
a = set(["Jake", "John"])
b = set(["John", "Jill"])
print(a.symmetric_difference(b)) # {'Jill', 'Jake'}
print(b.symmetric_difference(a)) # {'Jake', 'Jill'}

# Members of one but not the other:
# .difference()
a = set(["Jake", "John"])
b = set(["John", "Jill"])
a.difference(b) # {'Jake'}
b.difference(a) # {'Jill'}

# .union()
a = set(["Jake", "John"])
b = set(["John", "Jill"])
a.union(b) # {'Jake', 'John', 'Jill'}

# Set containing all the participants from event A which did not attend event B.
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])
a.difference(b) #  {'Jake', 'Eric'}
```

# Techniques & Tricks

```python
# max and min w/ inf
max = float("-inf")
min = float("inf")

# max() and min()
max("abcDEF") # find largest item in the string ('c')
max([2, 1, 4, 3]) # 4
max(("one", "two", "three")) # find largest item in the tuple ('two')

# Sum of all digits
sum(map(lambda x: int(x)**2, str(n)))

# If the number of arguments is unknown, we can add a * before the parameter name.
def combined_varargs(*args, **kwargs):
    print(args)
    print(kwargs)

combined_varargs(1, 2, 3, a="hi")
# Output:
(1, 2, 3)
{'a': 'hi'}
```

# Python Input Methods for CP: https://www.geeksforgeeks.org/python-input-methods-competitive-programming/

# Python3 for CP: https://codeforces.com/blog/entry/69801

# Fast input:

```python
import sys
inp = [a.strip()
       fo a in sys.stdin.readlines()]  #inp is an array of input lines.
```

# Matrix:

```python
import sys
M = [list(map(int, a.strip().split())) for a in sys.stdin.readlines()]
# Then ^Z for exiting input mode when debugging.
```
