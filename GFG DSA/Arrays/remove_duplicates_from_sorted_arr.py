# def remove(arr):
#     for i in range(1,len(arr)):
#         if arr[i]==arr[i-1]:
#             arr[i-1]="X"
#     print(arr)
#     for i in range(len(arr)):
#         if arr[i]=="X":
#             for j in range(i+1,len(arr)):
#                 arr[j-1]=arr[j]
#                 if j==len(arr)-1:
#                     arr[j]="X"
#     return arr


# Naive Solution

def remove(arr):
    temp=[]
    for i in range(len(arr)):
        if arr[i] not in temp :
            temp.append(arr[i])
    for j in range(len(arr)-len(temp)):
        temp.append("X")
    return temp

# print(remove([1,1,1,2,3,3,4,5]))

def remove2(arr):
    temp=["X"]*len(arr)
    temp[0]=(arr[0])
    res=1
    for i in range(1,len(arr)):
        if arr[i]!=temp[res-1]:
            temp[res]=arr[i]
            res+=1
    return temp

# print(remove2([1,1,1,2,3,3,4,5]))

def remove3(arr):
    res=1
    for i in range(1,len(arr)):
        if arr[i]!=arr[res-1]:
            arr[res]=arr[i]
            res+=1
    return arr,res

# print(remove3([1,1,1,2,3,3,4,5]))


def remove4(arr):
    i=0
    j=1
    while j<len(arr):
        if arr[i]!=arr[j]:
            arr[i+1]=arr[j]
            i+=1
            j+=1
        else:
            j+=1
    return arr,i+1

print(remove4([1,1,1,2,3,3,4,5]))


