# Naive Approach

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

def sieve(x):
    for i in range(x+1):
        if isPrime3(i):
            print(i)

# sieve(43)

#O(n*n^0.5)


def sieve2(x):
    isprime = [True]*(x+1)
    for i in range(2,int(pow(x,0.5))):
        if isprime[i]:
            for j in range(i*2,x,i):
                isprime[j]=False
    
    for i in range(2,x+1):
        if isprime[i]:
            print(i)
    # return isprime


sieve2(46)

# O(nloglogn)  ??


# More optimised

def sieve3(x):
    isprime = [True]*(x+1)
    for i in range(2,int(pow(x,0.5))):
        if isprime[i]:
            for j in range(i*i,x,i):
                isprime[j]=False
    
    for i in range(2,x+1):
        if isprime[i]:
            print(i)
    # return isprime


# sieve3(46)