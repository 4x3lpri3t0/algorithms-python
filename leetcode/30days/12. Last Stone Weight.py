from typing import List


class Solution:
    def last_stone_weight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            stones.append(stones.pop() - stones.pop())
        return stones[0]
