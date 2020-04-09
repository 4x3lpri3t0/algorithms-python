# Every item to the right of our rotation point is always
# alphabetically before the first item in the list.
# So the rotation point is to our left if the current item
# is less than the first item. Else it's to our right.


def get_rotation_point_index(words):
    lo = 0
    hi = len(words) - 1

    while (lo < hi - 1):
        mid = lo + (hi - lo) // 2  # 5, left hi = 5, 2, right lo = 2
        # mid = 2 + (5 - 2) // 2 = 3, right lo = 3, mid = 3 + (5 - 3) // 2 = 4, lo = 4
        # lo is 4 and if lo + 1 == 5 return mid, so we return 5 (rotation index)
        # Compare with first char
        if words[mid] < words[0]:  # Go left
            hi = mid
        else:
            lo = mid

        if lo + 1 == hi:
            return hi


words = [
    'ptolemaic',
    'retrograde',
    'supplant',  # 2
    'undulate',  # 3
    'xenoepist',  # 4
    'asymptote',  # 5 <-- rotates here
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',  # 10
]
print(get_rotation_point_index(words))
