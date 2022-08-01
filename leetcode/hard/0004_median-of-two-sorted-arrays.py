# https://leetcode.com/problems/median-of-two-sorted-arrays/

"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log(m+n)).

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        mid = (m + n) // 2 + 1
        prev2 = prev1 = None
        i = j = 0
        for _ in range(mid):
            prev2 = prev1
            if j == n or (i != m and nums1[i] <= nums2[j]):
                prev1 = nums1[i]
                i += 1
            else:
                prev1 = nums2[j]
                j += 1

        # Mid if odd length, otherwise sum of two midds
        return prev1 if (m + n) % 2 else (prev1 + prev2) / 2


# sol = Solution()
# assert ...
