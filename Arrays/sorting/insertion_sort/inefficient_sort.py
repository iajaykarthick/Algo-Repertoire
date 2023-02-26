def sort(arr):
    for j in range(len(arr)-1):
        min_idx = j
        for i in range(j+1, len(arr)):
            if arr[i] < arr[min_idx]:
                min_idx = i
        arr[min_idx],  arr[j] = arr[j], arr[min_idx]
    return arr
        
print(sort([6,5,4,3,2,1,0]))