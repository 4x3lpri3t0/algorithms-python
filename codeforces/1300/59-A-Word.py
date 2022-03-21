input = input()

count = 0
for c in input:
    if c.islower():
        count -= 1
    else:
        count += 1

print(input.upper() if count > 0 else input.lower())