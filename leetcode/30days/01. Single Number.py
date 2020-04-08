# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3283/


class Solution:
    def single_number(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)
        return seen.pop()


def singleNumber(self, nums):  # Binary XOR(^)
    if not nums:
        return
    res = nums[0]
    for i in range(1, len(nums)):
        res = res ^ nums[i]
    return res


def singleNumber_lambda(self, nums):  # Binary XOR(^) optimized w/ reduce+lambda
    from functools import reduce
    return reduce(lambda x, y: x ^ y, nums)


s = Solution()
print(s.single_number([2, 2, 1]))  # 1
print(s.single_number([4, 1, 2, 1, 2]))  # 4
