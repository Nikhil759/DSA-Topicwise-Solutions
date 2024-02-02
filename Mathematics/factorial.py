def factorial(x):
    prod=1
    if x == 0 or x == 1 :
        return 1
    while(x>0):
        prod=prod*(x)
        x=x-1
    
    return prod

print(factorial(5))

# Time Complexity is O(d), this is the optimal solution

def fact_rec(x):
    # prod=1 
    if x==1 or x==0:
        return 1
    
    return x*fact_rec(x-1)

print(fact_rec(6))

# Time Complexity is O(d) and Space Complexity also O(d)
