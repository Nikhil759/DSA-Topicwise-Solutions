def lr_by1(arr):
    temp=arr[0]
    for i in range(1,len(arr)):
        arr[i-1]=arr[i]
    arr[len(arr)-1]=temp
    return arr

def lr_byD(arr,d):
    for i in range(d):
        arr=lr_by1(arr)
    return arr

#O(nd)

print(lr_byD([1,2,3,4,5],2))

def lr2_byD(arr,d):
    temp = arr[0:d]

    for i in range(d,len(arr)):
        arr[i-d]=arr[i]
    arr[len(arr)-d:len(arr)]=temp
    return arr

print(lr2_byD([1,2,3,4,5,6,7],2))

#O(n) and O(d)


def lr3_byD(arr,d):
    arr=arr[d:]+arr[0:d]
    return arr

print(lr3_byD([1,2,3,4,5,6,7],2))


def reverse(arr,i,j):
    while j>i:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    return arr

def lr4_byD(arr,d):
    reverse(arr,0,d-1)
    reverse(arr,d,len(arr)-1)
    reverse(arr,0,len(arr)-1)
    return arr

print(lr4_byD([1,2,3,4,5,6,7],2))

#O(n)
