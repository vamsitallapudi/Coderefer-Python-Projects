from typing import List
import math


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]


print(Solution().majorityElement([6, 6, 6, 7, 7]))