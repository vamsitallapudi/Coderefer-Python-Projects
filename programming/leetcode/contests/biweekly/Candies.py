from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        x = max(candies)
        y = []
        for i in candies:
            if i + extraCandies >= x:
                y.append(True)
            else:
                y.append(False)
        return y


print(Solution().kidsWithCandies([2,3,5,1,3], 3))