import itertools


class Solution:
    count = 0

    def countArrangement(self, n: int) -> int:
        visited = [False for _ in range(0, n + 1)]
        self.calculate(n, 1, visited)
        return self.count

    def calculate(self, n, pos: int, visited: list):
        if pos > n:
            self.count += 1
        for i in range(1, n + 1):
            if not visited[i] and (pos % i is 0 or i % pos is 0):
                visited[i] = True
                self.calculate(n, pos+1, visited)
                visited[i] = False


print(Solution().countArrangement(3))
