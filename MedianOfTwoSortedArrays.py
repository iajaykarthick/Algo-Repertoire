'''
Median of Two Sorted Arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the merged sorted array of the two sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n)).
'''
from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    merged_arr = merge(nums1, nums2) if len(nums1) > len(nums2) else merge(nums2, nums1)
    mid = len(merged_arr) // 2
    return (merged_arr[mid] + merged_arr[~mid]) / 2
    
def merge(arr1: List[int], arr2: List[int]) -> List[int]:
    for num in arr2:
        start = 0
        end = len(arr1)
        while start < end:
            mid = (start + end) // 2
            if arr1[mid] > num:
                end = mid
            else:
                start = mid+1
        arr1.insert(start, num)
    return arr1



print(findMedianSortedArrays([1,2,4,5], [2,3]))