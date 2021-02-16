'''
find the number of unordered pairs of distinct integers from 1 to N whose bit-wise XOR does not exceed N.
'''

for _ in range(int(input())):
    n = int(input())
    count = 0
    for current_element in range(1, n+1):
        for next_element in range(current_element+1, n+1):
            if current_element ^ next_element < n+1:
                count += 1
        
    print(count)