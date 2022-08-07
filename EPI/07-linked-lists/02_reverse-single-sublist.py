from typing import List, Optional


class ListNode(object):
    def __init__(self, x=None, next=None):
        self.data = x
        self.next = next


def print_list(L: Optional[ListNode]) -> None:
    while L:
        print(L.data, end=" ")
        L = L.next
    print()


def reverse_sublist(L: ListNode, start: int, finish: int) -> Optional[ListNode]:
    dummy_head = sublist_head = ListNode(0, L)
    for _ in range(1, start):
        sublist_head = sublist_head.next

    # Reverse sublist.
    sublist_iter = sublist_head.next
    for _ in range(finish - start):
        temp = sublist_iter.next

        # TODO: Review this crazy triple swap...
        sublist_iter.next, temp.next, sublist_head.next = (
            temp.next,
            sublist_head.next,
            sublist_iter.next,
        )
        # A <- B
        # B <- C
        # C <- A
        # (3 swaps at the same time)

    return dummy_head.next


# Validating the solution:

l1 = ListNode(2)
l2 = ListNode(7, l1)
l3 = ListNode(5, l2)
l4 = ListNode(3, l3)
l5 = ListNode(11, l4)

# 1st validation:
print("====")
print_list(l5)
print_list(reverse_sublist(l5, 2, 4))  # Revert all except first and last.

# 2nd validation:
print("====")
print_list(l5)
print_list(reverse_sublist(l5, 1, 5))  # Revert all.
