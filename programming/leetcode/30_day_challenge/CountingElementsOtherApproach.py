import collections
from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        C = collections.Counter(arr)
        return sum(C[x] for x in C if x+1 in C)

print(Solution().countElements([1,2,3,4]))