# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3285/
class Solution:
    def max_sub_array(self, nums) -> int:
        global_max = nums[0]
        current_sum = nums[0]
        for num in nums[1::]:
            current_sum = max(num, current_sum + num)
            global_max = max(global_max, current_sum)
        return global_max
