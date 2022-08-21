from typing import List


def search_entry_equal_to_its_index(A: List[int], k: int) -> int:
    left, right = 0, len(A) - 1
    while left <= right:
        mid = (left + right) // 2
        difference = A[mid] - mid
        # A[mid] == mid if and only if difference == 0.
        if difference == 0:
            return mid
        elif difference > 0:
            right = mid - 1
        else: # difference < 0.
            left = mid + 1
    return -1

# TODO: Validate + Review
