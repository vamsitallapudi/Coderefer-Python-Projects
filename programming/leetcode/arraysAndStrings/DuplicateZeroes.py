from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        zeroes = arr.count(0)  # to count total number of zeroes
        n = len(arr)
        for i in range(n - 1, -1, -1):
            # right shifting the digits
            if i + zeroes < n:
                arr[i + zeroes] = arr[i]
            if arr[i] is 0:
                zeroes -= 1
                if i + zeroes < n:
                    #adding zero at required place
                    arr[i + zeroes] = 0
        print(arr)


Solution().duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0])
