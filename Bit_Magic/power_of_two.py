def check_p2(x):
    if x==0:
        return False
    return (x&(x-1)==0) # this expression sets the right most set bit to zero
        

print(check_p2(16)) 

#O(num of set bits)