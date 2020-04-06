class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from functools import reduce
        return reduce(lambda x, y: x ^ y, nums)

# class Solution:
#     def singleNumber(self, nums) -> int:
#         set = []
#         for num in nums:
#             if num in set:
#                 set.remove(num)
#             else:
#                 set.append(num)
#         return set.pop()


s = Solution()
print(s.singleNumber([2, 2, 1]))  # 1
print(s.singleNumber([4, 1, 2, 1, 2]))  # 4
