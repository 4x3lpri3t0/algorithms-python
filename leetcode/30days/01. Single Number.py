# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3283/
class Solution:
    def single_number(self, nums) -> int:
        from functools import reduce
        return reduce(lambda x, y: x ^ y, nums)

# class Solution:
#     def single_number(self, nums) -> int:
#         set = []
#         for num in nums:
#             if num in set:
#                 set.remove(num)
#             else:
#                 set.append(num)
#         return set.pop()


s = Solution()
print(s.single_number([2, 2, 1]))  # 1
print(s.single_number([4, 1, 2, 1, 2]))  # 4
