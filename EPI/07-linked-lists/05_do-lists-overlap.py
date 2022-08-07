from typing import Optional

lib03 = __import__("03_is-list-cyclic")
lib04 = __import__("04_do-terminated-lists-overlap")


class ListNode(object):
    def __init__(self, x=None, next=None):
        self.data = x
        self.next = next


def print_list(L: Optional[ListNode]) -> None:
    while L:
        print(L.data, end=" ")
        L = L.next
    print()


def overlapping_lists(l0: ListNode, l1: ListNode) -> Optional[ListNode]:
    # Store the START of CYCLE, if any.
    root0, root1 = lib03.has_cycle(l0), lib03.has_cycle(l1)

    if not root0 and not root1:
        # Both lists don't have cycles.
        return lib04.overlapping_no_cycle_lists(l0, l1)
    elif (root0 and not root1) or (not root0 and root1):
        # One list has cycle, one has no cycle.
        return None

    # Both lists have cycles.
    temp = root1
    while temp:
        temp = temp.next
        if temp is root0 or temp is root1:
            break

    return root1 if temp is root0 else None


# TODO: Validate
