from xmlrpc.client import boolean


def can_reach_end(A: list[int]) -> bool:
    max_pos = 0
    for cur_pos in range(len(A)):
        if cur_pos > max_pos:
            return False
        max_pos = max(max_pos, cur_pos + A[cur_pos])

    return True


A = [3, 3, 1, 0, 2, 0, 1]
assert can_reach_end(A) == True

A = [3, 2, 0, 0, 2, 0, 1]
assert can_reach_end(A) == False

A = [0]
assert can_reach_end(A) == True  # (We're already at last position)

A = [0, 0]
assert can_reach_end(A) == False
