def minimumAbsoluteDifference(arr):
    # Write your code here
    arr.sort()
    abs_min = float('inf')
    
    if len(arr) != len(set(arr)):
        return 0
    
    for i in range(len(arr)-1):
        current_abs_minimum = abs(arr[i] - arr[i+1])
        print(arr[i], arr[i+1], arr[i] - arr[i+1])
        abs_min = current_abs_minimum if current_abs_minimum < abs_min else abs_min
        if abs_min == 0:
            return 0
    return abs_min

print(minimumAbsoluteDifference([-3, 3, 4, 5, 6]))