# https://leetcode.com/problems/build-array-from-permutation/
class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans = [] * len(nums)
        for i in range(len(nums)):
            ans[i] = nums[nums[i]]
        return ans
