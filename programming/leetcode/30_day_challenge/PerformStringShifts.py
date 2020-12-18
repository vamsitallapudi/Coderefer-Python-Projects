from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for i in shift:
            s = self.perform_shift(s,i)
        return s

    def perform_shift(self, p: str, lst: List[int]) -> str:
        side = bool(lst[0])
        amount = int(lst[1])
        if side:
            return p[len(p) - amount:] + p[0:len(p) - amount]
        else:
            return p[amount:] + p[:amount]

print(Solution().stringShift("abcdefg", [[1,1],[1,1],[0,2],[1,3]]))
