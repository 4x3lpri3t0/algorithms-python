# algorithms-python
A repository for algorithms and competitive programming problems with solutions implemented in Python.

# Techniques & Tricks

## Strings
```python
# Sum of all digits
sum(map(lambda x: int(x)**2, str(n)))

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
# for ... in ...:
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)
    
# range
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

# Techniques & Tricks
