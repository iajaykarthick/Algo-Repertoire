'''
Add one to a list of numbers that each number is considered as digits of decimal

For eg, [1, 2, 3] + 1 = [1, 2, 4]

'''

from typing import  List

def plusOne(digits: List[int]) -> List[int]:
    to_add = 1
    for i in range(len(digits)-1, -1, -1):
        sum = digits[i] + to_add
        to_add = sum // 10 if sum > 9 else 0
        digits[i] = sum % 10 if sum > 9 else sum
    if to_add > 0:
        digits = [to_add] + digits 
    return digits


result = plusOne([9, 9, 9])
print(result)