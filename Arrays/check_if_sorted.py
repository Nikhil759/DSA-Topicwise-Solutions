def checksorted(arr):
    if len(arr)==1:
        return True
    if len(arr)==0:
        return False
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            return False
    return True

print(checksorted([1,2,1,4,5,6]))
print(checksorted([]))