class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        if nums[0] <= nums[n-1]:
            start = 0
            end = n - 1
            step = 1
        else:
            start = n - 1
            end = 0
            step = -1
            
            
        for i in range(start, end, step):
            if nums[i] > nums[i+step]:
                return False
            
        return True
