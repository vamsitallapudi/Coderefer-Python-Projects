from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(list(i ** 2 for i in A))


print(Solution().sortedSquares([-3, -1, 0, 2, 3]))
