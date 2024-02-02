# Naive Approach 
import math 

def check_kth(x,k):
    bin=[]
    while x>0:
        y = int(math.log(x,2))
        x=x%pow(2,y)
        bin.append(y+1)
    if k in bin:
        return True
    else:
        return False

print(check_kth(8,2))


#Better approach, to check if kth bit is set, just do x & 000{kth bit set}0000, eg if k is 3 then do x & 100

def check_kth2(x,k):
    if x&pow(2,k-1)==0:
        return False
    else:
        return True
    
print(check_kth2(8,2))

# O(k)


# More optimal , without using power

def check_kth3(x,k):
    if x&(1<<(k-1))==0:
        return False
    else:
        return True
    
print(check_kth3(5,1))

# Complexity O(1)

def check_kth4(x,k):
    if 1&(x>>(k-1))==0:
        return False
    else:
        return True
    
print(check_kth4(5,1))

# Complexity O(1)
