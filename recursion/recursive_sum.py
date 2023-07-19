def summ(arr):
    if len(arr) == 0:
        return 0
    else:
        first = arr[0]
        arr.pop(0)
        return first+summ(arr)
    
a = [1,2,3,4,5,6,7]
print(summ(a))    

""""The process:
First Check if the array is empty;if it is return 0
If its not empty then save its first element in a variable.
Then remove it from the array.
Then recursively add the first element and pop it off everytime until the array doesnt exist."""