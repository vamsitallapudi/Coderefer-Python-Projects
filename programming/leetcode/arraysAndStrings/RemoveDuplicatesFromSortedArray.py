from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start, end = 1, len(nums) - 1
        if not nums:
            return 0
        else:
            prev = nums[0]
            while start <= end:
                current = nums[start]
                if current != prev:
                    prev = current
                    start += 1
                elif current == prev:
                    self.moveLeft(nums, start + 1, end)
                    end -= 1
            return start

    def moveLeft(self, nums, start, end):
        for i in range(start, end + 1):
            nums[i - 1] = nums[i]


print(Solution().removeDuplicates([]))
