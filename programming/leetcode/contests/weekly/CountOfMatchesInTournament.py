import math
class Solution:
    def numberOfMatches(self, n: int) -> int:
        count = 0
        while n > 1:
            temp = n//2
            count += temp
            n = math.ceil(n/2)
        return count


print(Solution().numberOfMatches(7))
