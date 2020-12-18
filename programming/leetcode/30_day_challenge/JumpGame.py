from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_good_position = len(nums) -1

        for i, x in reversed(list(enumerate(nums))):
            if i + nums[i] >= last_good_position:
                last_good_position = i

        return last_good_position == 0


print(Solution().canJump([2,3,1,1,4]))