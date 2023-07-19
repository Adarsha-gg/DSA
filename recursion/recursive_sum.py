def summ(arr):
    if len(arr) == 0:
        return 0
    else:
        first = arr[0]
        arr.pop(0)
        return first+summ(arr)
    
a = [1,2,3,4,5,6,7]
print(summ(a))    