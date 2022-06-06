def rearrange(A: list[int]) -> list[int]:
    for i in range(len(A)):
        A[i : i + 2] = sorted(A[i : i + 2], reverse=bool(i % 2))

    return A


assert rearrange([1, 2, 3, 4]) == [1, 3, 2, 4]
assert rearrange([4, 3, 2, 1]) == [3, 4, 1, 2]
