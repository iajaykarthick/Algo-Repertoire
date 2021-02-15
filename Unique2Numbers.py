'''
You are given an array of integers. The special property of the array is that exactly two different elements occur once while other elements occur twice.

You are required to determine those two elements.

Input format

First line: Integer N denoting the number of elements in the array
Second line: N space-separated integers denoting the values in the array

'''

N = int(input())
nums = list(map(int, input().split()))
sums = 0
for num in nums:
    sums = sums ^ num
sums = (sums & -sums)
sum1 = 0
sum2 = 0

for num in nums:
    if (num & sums) > 0:
        sum1 = sum1 ^ num 
    else:
        sum2 = sum2 ^ num
print(sum1, sum2)