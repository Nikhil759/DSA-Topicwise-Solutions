def count_digits(x):
    res=0
    while (x>0):
        x=int(x/10)
        res+=1
    return res

print(count_digits(466868868331111))

#Time Complexity - O(d) where d is the number of digits in input

