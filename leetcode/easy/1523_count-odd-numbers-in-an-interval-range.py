# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        total = 0
        if low % 2 == 1:
            total += 1
            low += 1
        if high % 2 == 1:
            total += 1
            high -= 1

        return total + int((high - low) / 2)


# 3, 7
## 4 (1), 6 (2)
## (6 - 4) / 2 = 1


# 8, 10
## (10 - 8) / 2 = 1
