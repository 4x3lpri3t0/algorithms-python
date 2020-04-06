# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3284/
class Solution:
    def is_happy(self, n: int) -> bool:
        visited = set()
        while n != 1 and n not in visited:
            visited.add(n)
            n = sum(map(lambda x: int(x)**2, str(n)))
        return n not in visited
