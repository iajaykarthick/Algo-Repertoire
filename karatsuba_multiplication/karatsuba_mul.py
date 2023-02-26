def mul(x, y, n):
    if n == 1:
        return x * y
    a = x//10**(n/2)
    b = x%10**(n/2)
    
    
    c = y//10**(n/2)
    d = y%10**(n/2)
    
    ac = mul(a, c, n/2)
    bd = mul(b, d, n/2)
    
    return 10**n * ac + 10**(n/2) * (mul((a+b), (c + d), n/2) - ac - bd) + bd

print(mul(23456, 51234, 4))

