from typing import List


# one-way mountain climbing
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        # edge case
        if len(A) <= 2 or A[0] > A[1]:
            return False
        down = False
        for i in range(2, len(A)):
            if A[i] < A[i - 1]:
                down = True
            elif A[i] == A[i - 1] or down:
                return False
        return down


print(Solution().validMountainArray([0, 3, 2, 1]))
