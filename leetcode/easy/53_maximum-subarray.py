# https://leetcode.com/problems/maximum-subarray/
class Solution:
    def max_sub_array(self, nums: list[int]) -> int:
        local_sum = nums[0]
        global_max = nums[0]
        for i in range(1, len(nums)):
            local_sum = max(nums[i], local_sum + nums[i])
            global_max = max(global_max, local_sum)

        return global_max
