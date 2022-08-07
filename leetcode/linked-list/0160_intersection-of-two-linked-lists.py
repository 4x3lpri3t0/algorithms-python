# https://leetcode.com/problems/intersection-of-two-linked-lists/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        # Get length of both lists
        lenA = lenB = 0
        itA = headA
        itB = headB

        while itA or itB:
            if itA:
                lenA += 1
                itA = itA.next
            if itB:
                lenB += 1
                itB = itB.next

        # Force A to be the longest
        if lenB > lenA:
            headA, headB = headB, headA
            lenA, lenB = lenB, lenA

        # Get diff between lenA - lenB
        diff = lenA - lenB

        itA = headA
        itB = headB
        # Skip the diff in longest list
        while diff > 0:
            itA = itA.next
            diff -= 1

        # One of those N nodes in same lists length has to be the intersection
        while itA:
            if itA == itB:
                return itA
            itA = itA.next
            itB = itB.next

        return None
