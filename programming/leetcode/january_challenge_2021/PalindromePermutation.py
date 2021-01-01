class Solution:
    def _countCharFreq(self, s: str):
        freq_dict = {}
        for i in s:
            if i in freq_dict.keys():
                freq_dict[i] += 1
            else:
                freq_dict[i] = 1
        return freq_dict

    def canPermutePalindrome(self, s: str) -> bool:
        if not s:
            return False
        oddFound = False
        freqDict = self._countCharFreq(s)

        for i in freqDict.values():
            if i % 2 == 1:
                if oddFound:
                    return False
                else:
                    oddFound = True
        return True


print(Solution().canPermutePalindrome("radar"))
