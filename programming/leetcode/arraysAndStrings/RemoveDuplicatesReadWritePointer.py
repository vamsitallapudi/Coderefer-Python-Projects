from typing import List


class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # 0th position should not be touched as its unique.
        # hence write pointer should be starting from 1.

        writePointer = 1

        for readPointer in range(1, len(nums)):
            if nums[readPointer] != nums[readPointer - 1]:
                nums[writePointer] = nums[readPointer]
                writePointer += 1

        return writePointer
