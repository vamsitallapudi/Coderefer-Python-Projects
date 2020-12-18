#algo to determine if a string has all unique chars
import collections


class IsUnique:
    def checkUnique(self, myStr) -> bool:
        x = {}
        for i in myStr:
            if i in x.keys():
                return False
            else:
                x[i] = 1
        return True

print(IsUnique().checkUnique("testing"))