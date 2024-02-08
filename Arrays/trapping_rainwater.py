# Naive Solution

def trap1(arr):
    res=0
    for i in range(1,len(arr)-1):
        lmax=arr[i]
        for j in range(0,i):
            lmax=max(lmax,arr[j])
        rmax=arr[i]
        for j in range(i+1,len(arr)):
            rmax=max(rmax,arr[j])
        res+= min(lmax,rmax)-arr[i]
    return res

# print(trap1([3,0,1,2,5]))
def reverse(arr):
    i=0
    j=len(arr)-1
    while j>i:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    return arr

def trap2(arr):
    res=0
    lmax=arr[0]
    rmax=arr[len(arr)-1]
    lmaxes=[]
    rmaxes=[]
    for i in range(1,len(arr)-1):
        if arr[i]>lmax:
            lmax=max(arr[i],lmax)
        lmaxes.append(lmax)
    for i in range(len(arr)-2,0,-1):
        if arr[i]>rmax:
            rmax=max(arr[i],rmax)
        rmaxes.append(rmax)
    rmaxes = reverse(rmaxes)
    for i in range(len(lmaxes)):
        res+=min(lmaxes[i],rmaxes[i])-arr[i+1]
    print(lmaxes)
    print(rmaxes)
    return res
print(trap2([3,0,1,2,5]))
print(trap2([5,0,6,2,3]))

#O(n) and O(n)

def trap3(arr):
    res=0
    lmaxes=[0]*(len(arr))
    rmaxes=[0]*(len(arr))
    lmaxes[0]=arr[0]
    rmaxes[len(arr)-1]=arr[len(arr)-1]
    for i in range(1,len(arr)):
        lmaxes[i]=max(lmaxes[i-1],arr[i])
    for i in range(len(arr)-2,-1,-1):
        rmaxes[i]=max(rmaxes[i+1],arr[i])
    for i in range(len(lmaxes)):
        res+=min(lmaxes[i],rmaxes[i])-arr[i]
    print(lmaxes,rmaxes)
    return res
print(trap3([3,0,1,2,5]))
print(trap3([5,0,6,2,3]))

#O(n) and O(n)

