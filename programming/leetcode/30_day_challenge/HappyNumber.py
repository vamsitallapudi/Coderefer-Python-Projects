class Solution:
    def isHappy(self, n: int) -> bool:
        result = False
        visited = set()
        while not result and n not in visited:
            visited.add(n)
            p = [int(_) for _ in str(n)]
            n = sum(list(map(lambda a: a ** 2, p)))
            if n == 1:
                result = True
        return result

if(Solution().isHappy(int(input()))):
    print('true')
else:
    print('false')