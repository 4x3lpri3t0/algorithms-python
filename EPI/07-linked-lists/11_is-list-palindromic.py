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


def reverse_list(L: ListNode) -> Optional[ListNode]:
    dummy_head = sublist_head = ListNode(0, L)
    sublist_iter = sublist_head.next
    while sublist_iter and sublist_iter.next:
        temp = sublist_iter.next

        sublist_iter.next, temp.next, sublist_head.next = (
            temp.next,
            sublist_head.next,
            sublist_iter.next,
        )

    return dummy_head.next


# l1 = ListNode(2)
# l2 = ListNode(7, l1)
# l3 = ListNode(5, l2)
# l4 = ListNode(3, l3)
# l5 = ListNode(11, l4)

# print_list(l5)
# print_list(reverse_list(l5))


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    # Finds the second half of L.
    slow = fast = L
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next

    # Compares the FIRST half and the REVERSED SECOND half lists.
    first_half_iter, second_half_iter = L, reverse_list(slow)
    while second_half_iter and first_half_iter:
        if second_half_iter.data != first_half_iter.data:
            return False
        second_half_iter, first_half_iter = (
            second_half_iter.next,
            first_half_iter.next,
        )

    return True


l1 = ListNode(2)
l2 = ListNode(9, l1)
l3 = ListNode(9, l2)
l4 = ListNode(2, l3)
print_list(l4)
print(is_linked_list_a_palindrome(l4))  # True

l1 = ListNode(1)
l2 = ListNode(4, l1)
l3 = ListNode(2, l2)
print_list(l3)
print(is_linked_list_a_palindrome(l3))  # False
