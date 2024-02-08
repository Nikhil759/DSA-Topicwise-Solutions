def min_flips(arr):
    con1s=0
    con0s=0
    i=1
    while i<len(arr):
        if i==len(arr)-1:
            if arr[i]==0:
                con0s+=1
            elif arr[i]==1:
                con1s+=1           
        if arr[i]==arr[i-1]:
            i+=1
        else :
            if arr[i-1]==0:
                con0s+=1
            elif arr[i-1]==1:
                con1s+=1
            i+=1
    flip_no = min(con0s,con1s)
    if flip_no==con0s:
        flip_no=0
    else:
        flip_no=1
    
    i=0
    count=0
    while i<len(arr):
        if arr[i]==flip_no:
            if count==0:
                print ("From "+ str(i) + " To ", end="")
            count+=1
            i+=1
        elif arr[i]!=flip_no:
            if count>0:
                print(i-1)
            count=0
            i+=1
    # return con0s,con1s

min_flips([1,1,0,0,0,1])
print("")
min_flips([1,0,0,0,0,1,0,0,1,1,1])
print("")
min_flips([0,1])

print("XX")

# O(n)+O(n) = O(n)


def min_flips2(arr):
    if arr[0]==arr[-1]:
        if arr[0]==0:
            flip_no=1
        else:
            flip_no=0
    else:
        flip_no=arr[0]
    
    i=0
    count=0

    while i<len(arr):
        if arr[i]==flip_no:
            if count==0:
                print ("From "+ str(i) + " To ", end="")
            count+=1
            i+=1
        elif arr[i]!=flip_no:
            if count>0:
                print(i-1)
            count=0
            i+=1

min_flips2([1,1,0,0,0,1])
print("")
min_flips2([1,0,0,0,0,1,0,0,1,1,1])
print("")
min_flips2([0,1])

print("XX")


# Always flip 2nd group only (Explained in video)

def min_flips3(arr):
    for i in range(1,len(arr)):
        if arr[i-1]!=arr[i]:
            if arr[i]!=arr[0]:
                print("From " + str(i) +" To ",end="")
            else :
                print(i-1)
    if arr[len(arr)-1]!=arr[0]:
        print(len(arr)-1)

min_flips3([1,1,0,0,0,1])
print("")
min_flips3([1,0,0,0,0,1,0,0,1,1,1])
print("")
min_flips3([0,1])
