def linear_search(arr, target):
    for j in range(len(arr)):
        if arr[j] == target:
            return j
        
    return None

print(linear_search([1,2,3,4,5,6,7], 3))