def maximum(arr):
    if arr == []:
        return 0
    else:
        first = arr[0]
        if first > arr[0]:
            first = arr[0]
            arr.pop(0)    
            return maximum(arr)
        return first
       

a = [1,2,3,4,5,6,7]
print(maximum(a))    