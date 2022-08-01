# https://leetcode.com/problems/number-of-1-bits/
class Solution:
    def hammingWeight(self, n: int) -> int:
        count_ones = 0
        while n > 0:
            count_ones += n & 1
            n >>= 1
        return count_ones
