'''
Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], 
then return 0.
'''

def reverse(x: int) -> int:
    isNegative = True if '-' in str(x) else False
    nums = [num for num in str(x).replace('-', '')]
    reverse_int = int(''.join(nums[::-1]))
    reverse_int = -reverse_int if isNegative else reverse_int
    if reverse_int < -2**31 or reverse_int >= 2**31:
        return 0
    else:
        return reverse_int



print(reverse(123))