# Naive Approach

def isPrime(x):
    if x==1:
        return False
    a=2
    while a<x:
        if x%a==0:
            return False
        a+=1
    return True



print(isPrime(29))

# Time Complexity O(n)


# Check only from 2 to n^0.5 for optimal time complexity

def isPrime2(x):
    if x==1:
        return False
    a=2
    while a*a<=x:
        # print(a)
        if x%a==0:
            return False
        a+=1
    return True

print(isPrime2(1))

# Time Complexity O(n^0.5)


#More optimal solution is to add some more checks for 2 and 3 , and skip some iterations in between 

def isPrime3(x):    
    if x==1:
        return False
    if x==2 or x==3:
        return True
    if x%2==0 or x%3==0:
        return False
    a=5
    while a*a<=x:
        # print(a)
        if x%a==0 or x%(a+2)==0:
            return False
        a+=6
    return True

print(isPrime3(53))

# Time Complexity O(n^0.5)
