n = int(input())

counter = 0
add_amount = 1
for i in range(1, n + 1):
    print(counter)
    counter += add_amount
    add_amount += 2
