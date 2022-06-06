# https://leetcode.com/problems/contains-duplicate-ii/
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = {}  # value, index
        for i in range(len(nums)):
            value = nums[i]
            if value in seen and i - seen[value] <= k:
                return True
            seen[value] = i
        return False


sol = Solution()
assert sol.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) == False
