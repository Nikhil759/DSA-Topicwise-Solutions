# Naive solution

def two_odd(arr):
    hash = {}
    
    for i in arr:
        if i not in hash:
            hash[i]=1
        else:
            hash[i]+=1
    
    for i in hash :
        if hash[i]%2!=0:
            print (i)
        
two_odd([4,3,3,3,4,4,4,5,5,1])


# x & ~(x-1) gives a number which has only one set bit and that set bit corresponds to the last set bit of x

def two_odd2(arr):
    res=0
    for i in arr:
        res=res^i
    k=res&(~(res-1))
    res1=0
    res2=0
    for i in arr:
        if i&k!=0:
            res1=res1^i
        else:
            res2=res2^i
    return (res1,res2)

print(two_odd2([4,3,3,3,4,4,4,5,5,1]))


