# Can buy only once and sell only once


def stocks(arr):
    i=0
    max_prof=0
    for j in range(len(arr)):
        if arr[j]-arr[i]>max_prof:
            max_prof=arr[j]-arr[i]
        elif arr[j]<arr[i]:
            i=j
    return max_prof

print(stocks([1,5,3,8,12]))
print(stocks([30,20,10]))
print(stocks([10,20,30]))
print(stocks([1,5,3,1,2,8]))
