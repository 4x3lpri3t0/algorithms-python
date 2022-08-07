from typing import Optional


class ListNode(object):
    def __init__(self, x=None, next=None):
        self.data = x
        self.next = next


def print_list(L: Optional[ListNode]) -> None:
    while L:
        print(L.data, end=" ")
        L = L.next
    print()


def merge_two_sorted_lists(
    L1: Optional[ListNode], L2: Optional[ListNode]
) -> Optional[ListNode]:
    # Placeholder for result.
    dummy_head = tail = ListNode()

    while L1 and L2:
        if L1.data <= L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next

    # Append remaining nodes of L1 or L2.
    tail.next = L1 or L2
    return dummy_head.next


# Validating the solution:

l1 = ListNode(3)
l2 = ListNode(1, l1)

j1 = ListNode(4)
j2 = ListNode(2, j1)

print_list(l2)
print_list(j2)
print_list(merge_two_sorted_lists(l2, j2))
