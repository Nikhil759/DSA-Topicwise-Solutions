# Naive Approach

def all_divisors(x) : 
    for i in range(1,x+1):
        if (x%i)==0:
            print(i)

# all_divisors(100)

# O(n)

def all_divisors2(x) : 
    for i in range(1,int(pow(x,0.5)+1)):
        if i==pow(x,0.5):
            print(i)
        elif (x%i)==0:
            print(i)
            print(int(x/i))
            

# all_divisors2(100)

#O(n^0.5)


# To get the divisors in order, we iterate first from 1 to n^0.5 then from n^0.5 to 1

def all_divisors3(x) : 
    for i in range(1,int(pow(x,0.5)+1)):
        if i==pow(x,0.5):
            print(i)
        elif (x%i)==0:
            print(i)
    
    for i in range(int(pow(x,0.5))-1,0,-1):
        if (x%i)==0:
            print(int(x/i))
            

all_divisors3(100)
