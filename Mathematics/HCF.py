# Naive solution

def hcf(x,y):
    a=min(x,y)
    while a>0:
        if x%a==0 and y%a==0:
            return a
        a-=1

print(hcf(19,15))

# Time Complexity is O(n) , where n is min(x,y)



# Optimal approach using Euclidean Algorithm