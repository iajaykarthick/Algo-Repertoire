from typing import List

def reverse_an_array(arr: List[int]) -> List[int]:
    start, end = 0, len(arr)-1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr


n = int(input())
arr = list(map(int, input().split()))
print(reverse_an_array(arr))