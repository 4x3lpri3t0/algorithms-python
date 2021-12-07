N = int(input())
list = []

for i in range(N):
    raw_input = input().split(" ")
    operation = raw_input[0]

    if operation == "print":
        print(list)
    elif operation == "reverse":
        list.reverse()
    elif operation == "sort":
        list.sort()
    elif operation == "append":
        n = int(raw_input[1])
        list.append(n)
    elif operation == "remove":
        n = int(raw_input[1])
        list.remove(n)
    elif operation == "pop":
        list.pop()
    elif operation == "insert":
        pos = int(raw_input[1])
        n = int(raw_input[2])
        list.insert(pos, n)