from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        hm = {x[0]: x for x in pieces}
        result = []

        for i in arr:
            result += hm.get(i, [])

        return result == arr


print(Solution().canFormArray([91, 4, 64, 78], [[78], [4, 64], [91]]))
