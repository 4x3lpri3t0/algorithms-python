class Solution:
    def backspace_compare(self, S: str, T: str) -> bool:
        def finalStr(s: str):
            stack = []
            for char in s:
                if stack and char == "#":
                    stack.pop()
                elif char != "#":
                    stack.append(char)
            return stack

        return finalStr(S) == finalStr(T)
