# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    # Optimized for runtime (use dictionary)
    def middleNode(self, head: ListNode) -> ListNode:
        if not head:
            return None

        curr = head
        count = 0
        index = {}
        while curr:
            index[count] = curr
            curr = curr.next
            count += 1

        mid = count//2

        return index[mid]

    # Optimized for space (iterate twice)
    def middle_node(self, head: ListNode) -> ListNode:
        list_len = 0
        cur = head
        while cur:
            list_len += 1
            cur = cur.next

        mid = list_len // 2
        cur = head
        while mid > 0:
            cur = cur.next
            mid -= 1
        return cur
