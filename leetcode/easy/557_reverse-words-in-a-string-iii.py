"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Input: s = "God Ding"
Output: "doG gniD"
"""

# https://leetcode.com/problems/reverse-words-in-a-string-iii/
class Solution:
    def reverseWords(self, s: str) -> str:
        result = [None] * len(s)
        space_indexes = []
        # First pass, get whitespace indexes
        for i in range(len(s)):
            if s[i] == " ":
                space_indexes.append(i)
                result[i] = " "

        # Add last index as a virtual space
        space_indexes.append(len(s))

        # Second pass, revert words locally
        current_space = 0
        start = 0

        while current_space < len(space_indexes):
            end = space_indexes[current_space]
            mid = start + (end - start) // 2
            i = 0
            while start + i <= mid:
                result[start + i], result[end - 1 - i] = s[end - 1 - i], s[start + i]
                i += 1

            start = end + 1
            current_space += 1

        return "".join(result)


s = Solution()
s.reverseWords("Let's take LeetCode contest")


def reverseWords_oneLiner(self, s: str) -> str:
    # s.split() splits the string into an array words by whitespace
    # word[::-1] reverses the words in the array
    # ' '.join() turns the array of words back into a string and adds a space between them
    return " ".join([word[::-1] for word in s.split()])
