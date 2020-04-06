# https://www.interviewcake.com/question/python3/reverse-string-in-place
def reverse(list):
    left = 0
    right = len(list) - 1

    while left < right:
        # Swap characters
        list[left], list[right] = list[right], list[left]
        # Move towards middle
        left += 1
        right -= 1


list = ['a', 'b', 'c']
reverse(list)
print(list)
list = [1, 2, 3]
reverse(list)
print(list)
