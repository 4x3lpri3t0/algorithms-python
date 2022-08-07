from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list sorted as well.
"""

# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        L = ListNode()
        L.next = head

        it = head
        while it:
            next_distinct = it.next
            while next_distinct and next_distinct.val == it.val:
                next_distinct = next_distinct.next
            it.next = next_distinct
            it = it.next

        return L.next
