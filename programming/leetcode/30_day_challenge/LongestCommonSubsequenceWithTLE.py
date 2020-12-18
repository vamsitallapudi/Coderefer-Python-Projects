import functools

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        arr1 = list(text1)
        arr2 = list(text2)

        @functools.lru_cache(None)
        def helper(i, j):
            if i == len(arr1) or j == len(arr2):
                return 0
            elif arr1[i] == arr2[j]:
                return 1 + helper(i + 1, j + 1)
            else:
                return max(helper(i+1, j), helper(i, j+1))
        return helper(0, 0)

print(Solution().longestCommonSubsequence("bd", "abcd"))