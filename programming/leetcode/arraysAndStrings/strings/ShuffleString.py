from typing import List
import collections


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        x = [char for char in s]
        dct = dict(zip(indices, x))
        sortedDict = collections.OrderedDict(sorted(dct.items()))
        totalStr = ""
        for i in sortedDict.values():
            totalStr += i
        return totalStr




if __name__ == '__main__':
    print(Solution().restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))
