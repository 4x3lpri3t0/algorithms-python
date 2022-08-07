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


def remove_duplicates(L: ListNode) -> Optional[ListNode]:
    it = L
    while it:
        # Use next_distinc to find the next distinct value.
        next_distinct = it.next
        while next_distinct and next_distinct.data == it.data:
            next_distinct = next_distinct.next
        it.next = next_distinct
        it = next_distinct
    return L


# TODO: Validate
