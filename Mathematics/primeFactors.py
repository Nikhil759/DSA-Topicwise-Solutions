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


def prime_factors(x):
    for i in range(2,x):
        if isPrime3(i):
            a=i
            while (x%a==0):
                print(i)
                a=a*i
            


# prime_factors(500)

#Time complexity is O(n*n^0.5*logn)


#More efficient approach

def prime_factors2(x):
    if x==1:
        return("No Prime Factors")
    for i in range(2,int(pow(x,0.5))):
        # print(x)
        if isPrime3(i):
            while (x%i==0):
                print(i)
                x=x/i

prime_factors2(84)







