# Check if a partially filled matrix has any conflicts.
import collections
import math


def is_valid_sudoku(partial_assignment: list[list[int]]) -> bool:
    # Return True if subarray
    # partial_assignment[start_row:end_row][start_col:end_col] contains any
    # duplicates in (1, 2, ..., len(partial_assignment)); otherwise return
    # False.
    def has_duplicate(block):
        block = list(filter(lambda x: x != 0, block))
        return len(block) != len(set(block))

    n = len(partial_assignment)
    # Check row and column constraints.
    if any(
        has_duplicate([partial_assignment[i][j] for j in range(n)])
        or has_duplicate([partial_assignment[j][i] for j in range(n)])
        for i in range(n)
    ):
        return False

    # Check region constraints.
    region_size = int(math.sqrt(n))
    return all(
        not has_duplicate(
            [
                partial_assignment[a][b]
                for a in range(region_size * I, region_size * (I + 1))
                for b in range(region_size * J, region_size * (J + 1))
            ]
        )
        for I in range(region_size)
        for J in range(region_size)
    )


# Pythonic solution that exploits the power of list comprehension.
def is_valid_sudoku_pythonic(partial_assignment):
    region_size = int(math.sqrt(len(partial_assignment)))
    return (
        max(
            collections.Counter(
                k
                for i, row in enumerate(partial_assignment)
                for j, c in enumerate(row)
                if c != 0
                for k in (
                    (i, str(c)),
                    (str(c), j),
                    (i, j, str(c)),
                )  # i: region_size, j: region_size
            ).values(),
            default=0,
        )
        <= 1
    )


partial_assignment = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

assert is_valid_sudoku(partial_assignment) == True

assert is_valid_sudoku_pythonic(partial_assignment) == True

# (Duplicated digit)
partial_assignment[0][0] = 4

assert is_valid_sudoku_pythonic(partial_assignment) == False
