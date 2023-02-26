def insertion_sort(arr):
    
    for j in range(1, len(arr)):
        
        key = arr[j]
        
        # insert arr[j] into the sorted sequence arr[1:j]
        
        i = j-1

        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i = i - 1
        
        arr[i+1] = key
        
    return arr
        
print(insertion_sort([6,5,4,3,2,1,0]))