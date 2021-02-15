'''
find the smallest number greater than n with exactly 1 bit different from n in binary form

'''

def get_next_great_number_with_one_different_bit(num: int) -> int:
    ones_compliment = ~num
    return ones_compliment^(ones_compliment&ones_compliment-1) | num


for i in range(10):
    result = get_next_great_number_with_one_different_bit(i)
    print(i, bin(i), result, bin(result))