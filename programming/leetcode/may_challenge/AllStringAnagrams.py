from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        anaList = []
        if len(s) < len(p):
            return anaList
        for i in range(0, len(s)):
            if self.isAnagram(p, s[i:i+len(p)]):
                anaList.append(i)
        return anaList

    def isAnagram(self, originalStr, str):
        if sorted(originalStr) == sorted(str):
            return True
        else:
            return False


print(Solution().findAnagrams("cbaebabacd", "abc"))