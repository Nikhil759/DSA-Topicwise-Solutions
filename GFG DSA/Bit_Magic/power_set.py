def power_set(s):
    n=len(s)
    arr=[]
    for i in range(pow(2,n)):
        string = ""
        k=0
        while(k<n):
            if i&(pow(2,k))==(pow(2,k)):
                string += s[k]
            k+=1
        arr.append(string)
    return arr

print(power_set("abc"))

#Time Complexity is O(2^n.n) 

# Note 2^n can be represented as 1<<n

def power_set2(s):
    n=len(s)
    arr=[]
    for i in range(1<<n):
        string = ""
        k=0
        while(k<n):
            if i&(1<<k)==(1<<k):
                string += s[k]
            k+=1
        arr.append(string)
    return arr

print(power_set2("abcd"))

#Time Complexity is O(2^n.n)