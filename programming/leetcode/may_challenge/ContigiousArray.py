from typing import List


# 0,1,0,1,0,1
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum, max_length = 0, 0
        x = {}

        for i in range(0, len(nums)):
            if nums[i] is 0:
                sum += -1
            else:
                sum += 1

            if sum is 0:
                if i+1 > max_length:
                    max_length = i+1
            elif sum in x.keys():
                if max_length < i - x[sum]:
                    max_length = i-x[sum]
            else:
                x[sum] = i

        return max_length

print(Solution().findMaxLength([0,0,1,0,0,0,1,1]))
