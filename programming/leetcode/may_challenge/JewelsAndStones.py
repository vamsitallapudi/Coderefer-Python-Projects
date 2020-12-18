class Solution:
    def numJewelsInStones(self, j: str, s: str) -> int:
        count = 0
        for i in s:
            if i in j:
                count += 1
        return count

# print(Solution().numJewelsInStones("aA", "aAAbbbb"))
