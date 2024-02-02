# Naive Approach

import math 

def count_set(x):
    count=0
    while x>0:
        y = int(math.log(x,2))
        x=x%pow(2,y)
        count+=1
    return count

print(count_set(7))

# O(no of set bits)

def count_set2(x):
    count=0
    while x>0:
        if x & 1 == 1:
            count+=1
        # count += x&1
        x=x>>1
    return count

print(count_set2(15))

# O(logn)

def count_set3(x):
    count=0
    while x>0:
        if x % 2 == 1:
            count+=1
        x=int(x/2)
    return count

print(count_set3(15))


# Keep making all the set bits as 0

def count_set4(x):
    count=0
    while x>0:
        x=x&(x-1) # this expression sets the right most set bit to zero
        count+=1
    return count

print(count_set4(15))

#O(num of set bits)