class Solution:
    def cleanStr(self, str) -> str:
        while '#' in str:
            for i in range(0, len(str)):
                if str[i] == '#':
                    if i==0 and len(str)>1:
                        return self.cleanStr(str[i+1:])
                    elif i==0:
                        return self.cleanStr(str.replace('#',''))
                    else:
                        return self.cleanStr(str[:i-1] + str[i+1:])
        return str

    def backspaceCompare(self, S: str, T: str) -> bool:
        if self.cleanStr(S) == self.cleanStr(T):
            return True
        else:
            return False


print(Solution().backspaceCompare("a##c","#a#c"))
