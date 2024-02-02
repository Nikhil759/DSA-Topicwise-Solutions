# Naive Approach

def comp(x,n):
    prod = 1
    for i in range(n):
        prod=prod*x
    return prod

print(comp(2,5))


#O(n)

# Recursive solution

def comp2(x,n):
    if n==0:
        return 1
    temp = comp2(x,int(n/2))
    temp=temp*temp

    if n%2 == 0:
        return temp
    else :
        return temp*x
    
print(comp(2,6))

# O(logn)