class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        count = 0
        if n >= 2 * m:
            return count
        while m != n:
            n >>= 1
            m >>= 1
            count += 1
        return n << count

print(Solution().rangeBitwiseAnd(1,1))
