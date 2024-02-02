import math

def trail(x):
    prod=1
    if x == 0 or x == 1 :
        return 1
    while(x>0):
        prod=prod*(x)
        x=x-1
    # print(prod)
    res=0
    while (prod%10==0):
        res+=1
        prod=int(prod/10)
    return res

#This is a suboptimal solution as it will overflow for higer values


print(trail(20))




def trail2(x):
    z=int(math.log(x,5))
    count = 0
    while (z>0):
        count+=int(x/pow(5,z))
        z-=1
    return count

print(trail2(1000))


def trail3(x):
    i=1
    count=0
    while x>pow(5,i):
        count+=int(x/pow(5,i))
        i+=1
    
    return count

print(trail3(1000))

# Number of trailing zeroes is calculated by adding x/5 + x/25 + x/125 + ..........

# Both above solutions are optimal , time complexity is O(log5(n))

