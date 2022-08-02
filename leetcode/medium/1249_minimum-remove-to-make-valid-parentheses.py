# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        result = []
        # Remove hanging ) left to right
        open_count = 0
        for i in range(len(s)):
            if s[i] == "(":
                open_count += 1
            elif s[i] == ")":
                if open_count == 0:
                    continue  # Invalid - skip it
                open_count -= 1
            result.append(s[i])

        # Remove hanging ( right to left
        closed_count = 0
        for i in reversed(range(len(result))):
            if result[i] == ")":
                closed_count += 1
            elif result[i] == "(":
                if closed_count == 0:
                    del result[i]  # Invalid - delete it
                else:
                    closed_count -= 1

        return "".join(result)
