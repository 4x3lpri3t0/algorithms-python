def sock_merchant(n, arr):
    dict = {}
    for num in arr:
        if num not in dict:
            dict[num] = 0
        dict[num] += 1
    total = 0
    for _, v in dict.items():
        total += int(v / 2)
    return total


# arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]
# print(sock_merchant(len(arr), arr))
arr = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]
print(sock_merchant(len(arr), arr))
