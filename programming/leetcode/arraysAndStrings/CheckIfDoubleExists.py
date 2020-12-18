from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if not arr:
            return False
        a = []
        for i in range(0, len(arr)):
            if arr[i] * 2 in a or arr[i] % 2 == 0 and arr[i] / 2 in a:
                return True
            a.append(arr[i])
        return False


print(Solution().checkIfExist([1, 2]))
