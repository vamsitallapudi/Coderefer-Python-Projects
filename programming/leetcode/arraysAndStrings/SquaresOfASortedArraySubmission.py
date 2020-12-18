from collections import deque
from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        l, r = 0, len(A) - 1
        a = deque()
        while l <= r:
            left, right = abs(A[l]), abs(A[r])

            if left > right:
                a.appendleft(A[l] ** 2)
                l += 1
            else:
                a.appendleft(A[r] ** 2)
                r -= 1
        return list(a)
