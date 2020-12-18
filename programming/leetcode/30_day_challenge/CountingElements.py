from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        dic = {}
        arr.sort()
        count=0
        for i in range(0,len(arr)):
            if dic.get(arr[i]) == None:
                dic[arr[i]] = 1
            else:
                dic[arr[i]]+=1
        for j in dic:
            if dic.get(j) != None and dic.get(j-1) != None:
                count += (dic[j-1])
        return count

print(Solution().countElements([1,2,3,4]))
