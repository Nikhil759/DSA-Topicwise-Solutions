def max_difference(arr):
    max_diff=-100
    i=0
    for j in range(1,len(arr)):
        if (arr[j]-arr[i])>max_diff:
            max_diff=arr[j]-arr[i]
        if arr[i]>arr[j]:
            i=j
    return max_diff

print(max_difference([2,3,10,6,4,8,1]))
print(max_difference([7,9,5,6,3,2]))
print(max_difference([10,20,30]))
print(max_difference([30,10,8,2]))

def max_difference2(arr):
    max_diff=-100
    min_val=arr[0]
    for j in range(1,len(arr)):
        max_diff=max(max_diff,arr[j]-min_val)
        min_val=min(min_val,arr[j])

    return max_diff

print(max_difference2([2,3,10,6,4,8,1]))
print(max_difference2([7,9,5,6,3,2]))
print(max_difference2([10,20,30]))
print(max_difference2([30,10,8,2]))