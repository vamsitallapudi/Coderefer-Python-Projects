from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k <= arr[0]-1:
            return k
        k -= arr[0] - 1

        for i in range(len(arr) - 1):
            missingNos = (arr[i + 1] - arr[i] - 1)
            if k <= missingNos:
                return arr[i] + k

            k -= missingNos

        return arr[-1] + k


print(Solution().findKthPositive([1,7,11,14,29,31,40,44], 20))
