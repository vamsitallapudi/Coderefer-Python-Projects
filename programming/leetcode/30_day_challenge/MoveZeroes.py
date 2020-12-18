from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        j= len(nums)-1
        while i<=j:
            if nums[j] == 0:
                j -= 1
                continue
            elif nums[i] == 0:
                for x in range(i,j):
                    nums[x] = nums[x+1]
                nums[j] = 0
                j-=1
            if nums[i] != 0:
                i += 1
        print(nums)
        
Solution().moveZeroes([0,0,1])

