# [-2,1,-3,4,-1,2,1,-5,4]

class Solution(object):
    def maxSubArray(self, nums):
        max_till_now = nums[0]
        max_so_far = nums[0]
        for i in range(1,len(nums)):
            max_till_now = max(max_till_now + nums[i], nums[i])
            max_so_far = max(max_so_far, max_till_now)
        return max_so_far

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

