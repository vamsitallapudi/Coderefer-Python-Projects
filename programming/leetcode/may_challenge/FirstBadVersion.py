class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 0
        r = n-1
        while l <= r:
            mid = int(l + (r-l)/2)
            if self.isBadVersion(mid) is False:
                l = mid+1
            else:
                r = mid-1
        return l

    def isBadVersion(self, n):
        arr = [True, True, True, False, False]
        return arr[n] is True
