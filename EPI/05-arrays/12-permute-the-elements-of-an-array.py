def apply_permutation(A: list[int], P: list[int]) -> list[int]:
    # Replace P forward
    for i in range(len(A)):
        while P[i] != i:
            # Swap
            p = P[i]
            A[p], A[i] = A[i], A[p]
            P[p], P[i] = p, P[p]

    return A


A = [0, 1, 2, 3]
P = [2, 0, 1, 3]

assert apply_permutation(A, P) == [1, 2, 0, 3]

A = [0, 1]
P = [1, 0]

assert apply_permutation(A, P) == [1, 0]
