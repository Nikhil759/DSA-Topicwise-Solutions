def lr(arr):
    temp=arr[0]
    for i in range(1,len(arr)):
        arr[i-1]=arr[i]
    arr[len(arr)-1]=temp
    return arr

print(lr([1,2,3,4,5]))
print(lr([30,5,20]))

