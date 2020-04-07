# algorithms-python
A repository for algorithms and competitive programming problems with solutions implemented in Python.

# To Review
- [ ] sherlock-and-anagrams &rarr; Combinations

# Language

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
for i, num in enumerate(nums):
for i, num in enumerate(nums, start=1):
for num in nums:
for i in range(1, n):
    
# range with step
for x in range(3, 8, 2):
    print(x) # 3,5,7

# while
while True:

# break, continue
```

## Loops
```python
def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]

def build_sentence(benefit):
    return benefit + " is a benefit of functions!"

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()
```

## Classes and Objects
```python
# define the Vehicle class
class Vehicle:
    kind = "car"
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# define objects
car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.value = 60000.00
car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.value = 10000.00

print(car1.description())
print(car2.description())
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

# List as queue
arr = [1,2,3]
arr.append(x) # queue.push(x)
arr.pop(0) #queue.pop()
arr[0] #queue.peek()

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
# Sum of all digits
sum(map(lambda x: int(x)**2, str(n)))
```
