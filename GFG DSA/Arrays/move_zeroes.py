def move(arr):
    i=0
    for j in range(0,len(arr)):
        if arr[j]!=0 and arr[i]==0:
            arr[j],arr[i]=arr[i],arr[j]
            i+=1
        elif not (arr[j]==arr[j]==0):
            i+=1
    return arr

# print(move([8,5,0,10,0,20]))
# print(move([0,0,0,10,0]))
# print(move([10,20]))

def move2(arr):
    i=0
    j=0
    while j<len(arr):
        if arr[j]!=0 and arr[i]==0:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j+=1
        elif arr[i]==arr[j]==0:
            j+=1
        else:
            i+=1
            j+=1
    return arr

        

# print(move2([8,5,0,10,0,20]))
# print(move2([0,0,0,10,0]))
# print(move2([10,20]))


def move3(arr):
    j=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[j],arr[i]=arr[i],arr[j]
            j+=1
    return arr

print(move3([8,5,0,10,0,20]))
print(move3([0,0,0,10,0]))
print(move3([10,20]))