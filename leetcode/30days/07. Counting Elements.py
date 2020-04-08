# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3289/
class Solution:
    def count_elements(self, arr):
        arr.sort()
        # Keep count of current repeat nums
        same_num = 1
        total = 0
        n = len(arr)
        for i in range(1, n):
            if arr[i] == arr[i - 1]:
                same_num += 1
            elif arr[i] == arr[i - 1] + 1:
                total += same_num
                same_num = 1
            else:
                same_num = 1
        return total


s = Solution()
arr = [1, 2, 3]
print(s.count_elements(arr))
arr = [1, 1, 3, 3, 5, 5, 7, 7]
print(s.count_elements(arr))
arr = [1, 3, 2, 3, 5, 0]
print(s.count_elements(arr))
arr = [1, 1, 2, 2]
print(s.count_elements(arr))
