#KADANE's ALGO

def max_ss(arr):
    j=0
    maxs=-1
    sum=0
    while j<len(arr):
        sum+=arr[j]
        maxs=max(sum,maxs)
        if sum<0:
            sum=0
        j+=1
    return maxs

print(max_ss([2,3,-8,7,-1,2,3]))
print(max_ss([5,8,3]))
print(max_ss([-6,-1,-8]))
print(max_ss([1,-2,3,-1,2]))
print(max_ss([-5,1,-2,3,-1,2,-2]))

print("")

# Max subarr will be computed by iterating one by one and getting the max sum till that index, next max will either be an 
#addition of the next index or it will be only the next index itself, whichever one is bigger

def max_ss2(arr):
    res=arr[0]
    maxEnding=arr[0]
    for i in range(1,len(arr)):
        maxEnding=max(maxEnding+arr[i],arr[i])
        res=max(res,maxEnding)
    return res

print(max_ss2([2,3,-8,7,-1,2,3]))
print(max_ss2([5,8,3]))
print(max_ss2([-6,-1,-8]))
print(max_ss2([1,-2,3,-1,2]))
print(max_ss2([-5,1,-2,3,-1,2,-2]))