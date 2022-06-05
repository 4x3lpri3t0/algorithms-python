def next_permutation(A: list[int]) -> list[int]:
    # Find the FIRST entry from the RIGHT that is smaller than the entry
    # immediately after it.
    inversion_point = len(A) - 2
    while inversion_point >= 0 and A[inversion_point] >= A[inversion_point + 1]:
        inversion_point -= 1
    if inversion_point == -1:
        return []  # perm is the last permutation.

    # Swap the smallest entry after index inversion_point that is greater than
    # perm[inversion_point]. Since entries in perm are decreasing after
    # inversion_point, if we search in reverse order, the first entry that is
    # greater than perm[inversion_point] is the entry to swap with.
    for i in reversed(range(inversion_point + 1, len(A))):
        if A[i] > A[inversion_point]:
            A[inversion_point], A[i] = A[i], A[inversion_point]
            break

    # Entries in perm must appear in decreasing order after inversion_point,
    # so we simply REVERSE these entries to get the SMALLEST dictionary order.
    A[inversion_point + 1 :] = reversed(A[inversion_point + 1 :])
    return A


# Key insight: We want to increase the input array by as little as possible.

A = [0, 1]
assert next_permutation(A) == [1, 0]

A = [1, 2, 3, 1]
assert next_permutation(A) == [1, 3, 1, 2]
