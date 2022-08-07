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


def add_two_numbers(L1: ListNode, L2: ListNode) -> Optional[ListNode]:
    place_iter = dummy_head = ListNode()
    carry = 0
    while L1 or L2 or carry:
        val = carry + (L1.data if L1 else 0) + (L2.data if L2 else 0)
        L1 = L1.next if L1 else None
        L2 = L2.next if L2 else None
        place_iter.next = ListNode(val % 10)
        carry, place_iter = val // 10, place_iter.next
    return dummy_head.next


# TODO: Validate
