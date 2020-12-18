from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        totalShift = 0
        for i in range(0,len(shift)):
           if shift[i][0] == 0:
                totalShift += -shift[i][1]
           else:
               totalShift +=shift[i][1]

        totalShift%=len(s)

        if totalShift > 0:
            return s[len(s) - totalShift:] + s[0:len(s) - totalShift]
        else:
            return s[totalShift:] + s[:totalShift]


print(Solution().stringShift("wpdhhcj", [[0,7],[1,7],[1,0],[1,3],[0,3],[0,6],[1,2]]))