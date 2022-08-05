"""
You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.

Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.

Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".
"""

# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/
class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        word_freq = {}
        for word in words:
            if word not in word_freq:
                word_freq[word] = 0
            word_freq[word] += 1

        count = 0
        for word in word_freq:
            reversed = word[1] + word[0]

            # aa, aa
            if word == reversed:
                if word_freq[word] > 1:
                    pairs = (word_freq[word] // 2) * 2
                    word_freq[word] -= pairs
                    count += pairs * 2
            # ab, ba
            elif (
                reversed in word_freq
                and word_freq[word] > 0
                and word_freq[reversed] > 0
            ):
                min_pairs = min(word_freq[word], word_freq[reversed])
                word_freq[word] -= min_pairs
                word_freq[reversed] -= min_pairs
                count += min_pairs * 4

        # Center
        for word in word_freq:
            if word[0] == word[1] and word_freq[word] > 0:
                count += 2
                break

        return count


# s = Solution()
# s.longestPalindrome(["lc", "cl", "gg"])

# s = Solution()
# s.longestPalindrome(["ab", "ty", "yt", "lc", "cl", "ab"])  # Expected 8

# s = Solution()
# s.longestPalindrome(
#     ["dd", "aa", "bb", "dd", "aa", "dd", "bb", "dd", "aa", "cc", "bb", "cc", "dd", "cc"]
# )  # Expected 22

s = Solution()
s.longestPalindrome(
    [
        "ll",
        "lb",
        "bb",
        "bx",
        "xx",
        "lx",
        "xx",
        "lx",
        "ll",
        "xb",
        "bx",
        "lb",
        "bb",
        "lb",
        "bl",
        "bb",
        "bx",
        "xl",
        "lb",
        "xx",
    ]
)  # Expected 26
