n = int(input())
arr = list(map(int, input().split()))

max1 = max(arr)

# First, remove all occurrences with value == maximum.
arr = (x for x in arr if x != max1)

# Then print the maximum from the remaining values.
print(max(arr))