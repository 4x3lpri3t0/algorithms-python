# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3287/
class Solution:
    def max_profit(self, prices) -> int:
        max_profit = 0
        n = len(prices)
        for i in range(1, n):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
        return max_profit


s = Solution()
print(s.max_profit([7, 1, 5, 3, 6, 4]))  # 7
