class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        complement_index_map = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in complement_index_map:
                return [complement_index_map[complement], i]
            complement_index_map[nums[i]] = i

        return [0, 0]
