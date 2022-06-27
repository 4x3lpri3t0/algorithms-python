# https://leetcode.com/problems/first-unique-character-in-a-string/
import string


class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = {}
        for char in s:
            if char not in map:
                map[char] = 0
            map[char] += 1
        for i in range(len(s)):
            if map[s[i]] == 1:
                return i
        return -1
