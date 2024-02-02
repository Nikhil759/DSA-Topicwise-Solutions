def lcm(x,y):
    a=min(x,y)
    b=max(x,y)
    i=1
    while (a*i%b!=0):
        i+=1
    return(a*i)

print(lcm(2,8))


# More efficient approach is to use the formula : a*b = gcd(a,b)*lcm(a,b) ==> lcm(a,b)=a*b/gcd(a,b)
# Calc HCF using Euclidean Algo and then just divide a*b by hcf to get the lcm
 