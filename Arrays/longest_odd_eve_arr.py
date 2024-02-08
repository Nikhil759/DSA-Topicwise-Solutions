def odd_eve(arr):
    if arr[0]%2==0:
        checkEven=False
        checkOdd=True
    else:
        checkEven=True
        checkOdd=False
    count=1
    maxc=0
    for i in range(1,len(arr)):
        if checkEven:
            if arr[i]%2==0:
                count+=1
                checkOdd=True
                checkEven=False
            else:
                maxc=max(count,maxc)
                count=1
                checkOdd=False
                checkEven=True
        elif checkOdd:
            if arr[i]%2==1:
                count+=1
                checkOdd=False
                checkEven=True
            else:
                maxc=max(count,maxc)
                count=1
                checkOdd=True
                checkEven=False
    maxc=max(count,maxc)
    return maxc

print(odd_eve([10,12,14,7,8]))
print(odd_eve([7,10,13,14]))
print(odd_eve([10,12,8,4]))

print("")

def odd_eve2(arr):
    count=1
    maxc=0
    for i in range(1,len(arr)):
        if (arr[i]%2==0 and arr[i-1]%2==1) or (arr[i]%2==1 and arr[i-1]%2==0):
            count+=1
            maxc=max(count,maxc)
        else:
            count=1
    return max(maxc,count)

print(odd_eve2([10,12,14,7,8]))
print(odd_eve2([7,10,13,14]))
print(odd_eve2([10,12,8,4]))