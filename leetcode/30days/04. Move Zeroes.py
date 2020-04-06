# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3286/
class Solution:
    def move_zeroes(self, nums) -> None:
        write_idx = 0
        for i, el in enumerate(nums):
            if el != 0:
                nums[write_idx], nums[i] = nums[i], nums[write_idx]
                write_idx += 1


s = Solution()
array = [1, 0, 10, 0, 99]  # [1, 10, 99, 0, 0]
s.move_zeroes(array)
print(array)
