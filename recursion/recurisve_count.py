def count(arr):
    if arr == []:
        return 0
    else:
        arr.pop()
        return 1+count(arr)
    
a = [1,2,3,4,5,]
print(count(a))    