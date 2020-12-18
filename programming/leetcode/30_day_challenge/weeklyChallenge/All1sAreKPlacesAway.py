from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count = 0
        is_length_apart = True
        for i in range(1, len(nums)):
            if nums[i] == 1:
                if count >= k:
                    is_length_apart = True
                else:
                    is_length_apart = False
                count = 0
            else:
                count += 1
        return is_length_apart


print(Solution().kLengthApart([1, 0, 1, 1, 0, 1, 0], 3))
