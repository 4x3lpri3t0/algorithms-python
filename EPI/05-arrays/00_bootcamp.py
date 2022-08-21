# Reorder an array of integers so that the even entries appear first.
def even_odd(A) -> None:
    next_even, next_odd = 0, len(A) - 1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1


A = [1, 2, 3, 4]
even_odd(A)
assert A == [4, 2, 3, 1]

# Time complexity: O(n)
# Space complexity: O(1)
