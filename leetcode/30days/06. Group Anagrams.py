# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3288/
from collections import defaultdict


class Solution:
    def group_anagrams(self, words):
        ana = defaultdict(list)
        for word in words:
            sorted_word = ''.join(sorted(word))
            ana[sorted_word].append(word)
        return [value for value in ana.values()]


s = Solution()
print(s.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
