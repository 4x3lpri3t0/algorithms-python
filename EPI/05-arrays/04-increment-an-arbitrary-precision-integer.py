def plus_one(A: list[int]) -> list[int]:
    # Iterate reversed
    for i in reversed(range(len(A))):
        if A[i] != 9:
            A[i] += 1
            return A
        A[i] = 0

    # If we reached the end, it means the number was composed by only 9 digits. Then add a 1 digit at the front.
    A[0] = 1
    A.append(0)
    return A


A = [1, 2, 9]
plus_one(A)
assert A == [1, 3, 0]

A = [1, 1, 1]
plus_one(A)
assert A == [1, 1, 2]

A = [9, 9]
plus_one(A)
assert A == [1, 0, 0]
