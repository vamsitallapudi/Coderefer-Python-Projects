import collections
from typing import List


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp, m, n = collections.defaultdict(int), len(A), len(B)
        for i in range(m):
            for j in range(n):
                dp[i, j] = max(dp[i - 1, j - 1] + (A[i] == B[j]), dp[i - 1, j], dp[i, j - 1])
        return dp[m - 1, n - 1]


print(Solution().maxUncrossedLines([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2]))
