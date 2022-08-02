# https://leetcode.com/problems/sorting-the-sentence/
class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")
        result_list = list(range(len(words)))
        for word in words:
            pos = int(word[len(word) - 1]) - 1  # Convert to 0-based indexing
            result_list[pos] = word[:-1]
        return " ".join(result_list)


solution = Solution()
solution.sortSentence("is2 sentence4 This1 a3")
