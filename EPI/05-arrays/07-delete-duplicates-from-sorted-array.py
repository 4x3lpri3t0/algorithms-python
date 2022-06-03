# Returns the number of valid entries after deletion
def delete_duplicates(A: list[int]) -> int:
    if not A:
        return 0

    last_unique_index = 1
    for i in range(1, len(A)):
        if A[last_unique_index - 1] != A[i]:
            A[last_unique_index] = A[i]
            last_unique_index += 1

    return last_unique_index


A = []
num_valid_entries = delete_duplicates(A)
assert num_valid_entries == 0

A = [1]
num_valid_entries = delete_duplicates(A)
assert num_valid_entries == 1

A = [1, 2, 3]
num_valid_entries = delete_duplicates(A)
assert num_valid_entries == 3

A = [1, 1, 2, 2, 3, 3]
num_valid_entries = delete_duplicates(A)
assert num_valid_entries == 3


A = [1, 5, 5, 5, 5, 5, 5, 6]
num_valid_entries = delete_duplicates(A)
assert num_valid_entries == 3

A = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
num_valid_entries = delete_duplicates(A)
assert num_valid_entries == 4
