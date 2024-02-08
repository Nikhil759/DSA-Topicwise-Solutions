# Naive Solution


def one_odd(arr) :
    hash = {}
    
    for i in arr:
        if i not in hash:
            hash[i]=1
        else:
            hash[i]+=1
    
    for i in hash :
        if hash[i]%2!=0:
            return i

print(one_odd([4,3,3,3,4,4,4,5,5]))

# Time complexity : O(n), Space Complexity : O(n)


#Using bitwise XOR


def one_odd2(arr):
    res=0
    for i in arr:
        res=res ^ i
    return res

print(one_odd2([4,4,4,3,3,3,3,4,4,4,5,5,5]))

# Time complexity : O(n), Space Complexity : O(1)

