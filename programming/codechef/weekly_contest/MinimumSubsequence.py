from typing import List


class Solution:
    def sum_of_list(self, list1: List[int]):
        total = 0
        for ele in range(0, len(list1)):
            total = total + list1[ele]
        return total

    def minSubsequence(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        else:
            sortedNums = sorted(nums, reverse=True)
            for i in range(0, len(sortedNums)):
                if self.sum_of_list(sortedNums[0:i]) > self.sum_of_list(sortedNums[i:len(sortedNums)]):
                    return sortedNums[0:i]
                elif i == len(sortedNums)-1:
                    return sortedNums

print(Solution().minSubsequence([8,8]))