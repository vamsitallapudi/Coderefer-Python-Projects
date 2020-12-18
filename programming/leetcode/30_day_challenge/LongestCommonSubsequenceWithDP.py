class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        b, a = len(text1), len(text2)

        arr = [[0] * (a + 1) for _ in range(b + 1)]
        for i in range(b):
            for j in range(a):
                if text1[i] == text2[j]:
                    arr[i + 1][j + 1] = 1 + arr[i][j]
                else:
                    arr[i + 1][j + 1] = max(arr[i + 1][j], arr[i][j + 1])
        return arr[-1][-1]


print(Solution().longestCommonSubsequence("bd", "abcd"))
