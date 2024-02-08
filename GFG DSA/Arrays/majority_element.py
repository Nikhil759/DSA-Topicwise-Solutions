# An element is called majority element if it occurs more than n/2 times 
# Moore's voting algo
# Return any index of the majortity element

def majority(arr):
    res=0
    count=1
    for i in range(1,len(arr)):
        if arr[i]==arr[res]:
            count+=1
        else:
            count=1
            res=i
    count=0
    for i in range(len(arr)):
        if arr[i]==arr[res]:
            count+=1
    if count<(len(arr)/2):
        return -1
    else :
        return res
        
print(majority([6,8,4,8,8]))