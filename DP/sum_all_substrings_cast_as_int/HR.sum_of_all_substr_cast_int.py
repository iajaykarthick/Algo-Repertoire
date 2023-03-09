def substrings(number):
    modulo = int(1e9 + 7)
    sum_substr_ends_at_i = 0
    total = 0
    
    for i in range(len(number)):
        sum_substr_ends_at_i = (sum_substr_ends_at_i * 10 + (i+1) * int(number[i])) % modulo
        total += sum_substr_ends_at_i % modulo
    return total % modulo
