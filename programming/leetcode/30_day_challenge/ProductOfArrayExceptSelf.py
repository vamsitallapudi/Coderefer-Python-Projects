from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        left = []  # to store left products of all elements in an array
        for i in range(0, len(nums)):
                left.append(p)
                p *= nums[i]

        p = 1
        for i in range(len(nums)-1, - 1, -1):
            left[i] *= p
            p *= nums[i]
        return left

print(Solution().productExceptSelf([1,2,3,4]))

# 1,2,3,4
#
# 1, 1, 2, 6
# 24,12,8,6