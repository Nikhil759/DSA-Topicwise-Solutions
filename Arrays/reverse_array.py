def reverse(arr):
    i=0
    j=len(arr)-1
    while j>i:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    return arr

print(reverse([1,2,3,4,5]))
print(reverse([5,5,4,2,3]))