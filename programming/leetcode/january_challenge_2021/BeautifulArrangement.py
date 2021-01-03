import itertools


class Solution:
    def countArrangement(self, n: int) -> int:
        lst = []
        count = 0
        for i in range(1, n + 1):
            lst.append(i)
        for i in list(itertools.permutations(lst)):
            if self.checkBeautiful(i):
                count += 1
        return count

    def checkBeautiful(self, lst):
        for i in range(0, len(lst)):
            if lst[i] % (i+1) != 0 and (i+1) % lst[i] != 0:
                return False
        return True


print(Solution().countArrangement(2))
