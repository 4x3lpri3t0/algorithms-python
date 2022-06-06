import random


def random_sample(A: list[int], k: int) -> list[int]:
    for i in range(k):
        # Generate a random index in [i, len(A) - 1].
        r = random.randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]
    return A[:k]


A = [1, 2, 3, 4, 5, 6]
k = 4
print(random_sample(A, k))
