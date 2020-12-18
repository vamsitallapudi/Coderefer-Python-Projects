from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.get_pivot(nums, 0, len(nums)-1)

        if pivot == -1:
            return self.binary_search(nums, target, 0, len(nums)-1)
        if target == nums[pivot]:
            return pivot
        elif target >= nums[0]:
            return self.binary_search(nums, target, 0, pivot-1)
        return self.binary_search(nums, target, pivot + 1, len(nums)-1)

    def get_pivot(self, arr, start, end):
        if end < start:
            return -1
        elif end == start:
            return end
        mid = int((start + end) / 2)

        if mid < end and arr[mid] > arr[mid+1]:
            return mid
        if mid > start and arr[mid] < arr[mid-1]:
            return mid-1
        if arr[mid] <= arr[start]:
            return self.get_pivot(arr, start, mid - 1)
        return self.get_pivot(arr, mid + 1, end)

    # standard binary search function
    def binary_search(self, arr, key, start: int, end: int):
        if end < start:
            return -1
        mid = int((start + end) / 2)
        if key < arr[mid]:
            return self.binary_search(arr, key, start, mid - 1)
        elif key > arr[mid]:
            return self.binary_search(arr, key, mid + 1, end)
        else:
            return mid


print(Solution().search([1,3,5], 1))
