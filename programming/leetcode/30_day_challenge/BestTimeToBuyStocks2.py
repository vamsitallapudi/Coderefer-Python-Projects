from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(prices[i]-prices[i-1],0) for i in range(1, len(prices)))

print(Solution().maxProfit([1,2,3,4,5]))