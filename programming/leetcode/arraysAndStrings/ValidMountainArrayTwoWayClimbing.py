from typing import List


class Solution():
    def validMountainArray(self, A: List[int]) -> bool:
        i, j, n = 0, len(A) - 1, len(A)
        while i + 1 < n - 1 and A[i] < A[i + 1]: i += 1
        while j > 0 and A[j - 1] > A[j]: j -= 1
        return 0 < i == j < n - 1


print(Solution().validMountainArray([3, 5, 5]))
