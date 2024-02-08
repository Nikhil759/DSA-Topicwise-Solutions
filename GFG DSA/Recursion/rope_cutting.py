def rope(n,a,b,c):
    if n==0:
        return 0
    if n<0:
        return -1
    res = max(rope(n-a,a,b,c),rope(n-b,a,b,c),rope(n-c,a,b,c))
    if res==-1:
        return -1
    return res+1


print(rope(9,2,2,2))

#Time Complexity 