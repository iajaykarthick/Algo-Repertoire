from typing import List
class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		prevMap = {}
		
		for i, n in enumerate(nums):
			diff = target - n
			if diff in prevMap:
				return [prevMap[diff], i]
			prevMap[n] = i
		return

s = Solution()
arr = list(map(int, input("Enter the array\n").strip().split()))
target = int(input("Enter the target sum\n"))
print(s.twoSum(arr, target))
