'''
Given two binary strings a and b, return their sum as a binary string.
'''

def addBinary(a: str, b: str) -> str:
    result = ''
    i = len(a) - 1
    j = len(b) - 1
    carry_forward = 0
    while i > -1 or j >-1:
        first_digit = int(a[i]) if i > -1 else 0
        second_digit = int(b[j]) if j > -1 else 0
        to_add = first_digit ^ second_digit ^ carry_forward
        carry_forward = first_digit | second_digit if carry_forward else first_digit & second_digit
        print(first_digit, second_digit, (1-first_digit & 1-second_digit), to_add, carry_forward)
        result = str(to_add) + result
        i -= 1
        j -= 1
    if carry_forward:
        result = str(carry_forward) + result
    return result

print(addBinary(a="1010", b = "1011"))