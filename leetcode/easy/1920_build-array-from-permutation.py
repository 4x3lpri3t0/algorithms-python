# https://leetcode.com/problems/build-array-from-permutation/
class Solution:
    def build_array(self, nums: list[int]) -> list[int]:
        ans = [0] * len(nums)
        for i in range(len(nums)):
            ans[i] = nums[nums[i]]
        return ans
