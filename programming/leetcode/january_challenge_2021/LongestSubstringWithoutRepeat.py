class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        charSet = set()
        i, j = 0, 0
        count = 0
        while i < n and j < n:
            if not s[j] in charSet:
                charSet.add(s[j])
                j += 1
                count = max(count, j - i)
            else:
                charSet.remove(s[i])
                i += 1

        return count


print(Solution().lengthOfLongestSubstring("pwwkew"))
