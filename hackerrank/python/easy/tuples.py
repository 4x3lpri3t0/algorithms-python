n = int(input())
integer_list = map(int, input().split())

tuple = tuple(integer_list)

print(hash(tuple))