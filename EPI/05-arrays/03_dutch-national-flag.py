"""
    Keep the following invariants during partitioning:
    Bottom group -> A[:smaller]
    Middle group -> A[smaller:equal]
    Unclassified group -> A[equal:larger]
    Top group -> A[larger:]
"""


def dutch_flag_partition(pivot_index: int, A: list[int]) -> None:
    smaller, equal, larger = 0, 0, len(A) - 1
    pivot = A[pivot_index]
    while equal <= larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller += 1
            equal += 1
        elif A[equal] > pivot:
            A[larger], A[equal] = A[equal], A[larger]
            larger -= 1
        elif A[equal] == pivot:
            equal += 1


pivot_idx = 1  # (pivot: 2)
A = [3, 2, 1, 2, 6, 2, 1]
dutch_flag_partition(pivot_idx, A)

# Less on the left. Equal on the middle. Greater on the right.
assert A == [1, 1, 2, 2, 2, 6, 3]

# TC: O(n)
# SC: O(1)
