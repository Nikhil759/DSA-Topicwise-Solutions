# Naive Solution

def max_scs(arr):
    maxs=0
    for i in range(len(arr)):
        sum=arr[i]
        curr_max=arr[i]
        for j in range(i+1,len(arr)+i):
            sum+=arr[j%(len(arr))]
            curr_max=max(curr_max,sum)
        maxs=max(maxs,curr_max)
    return maxs


# O(n^2)

print(max_scs([5,-2,3,4]))
print(max_scs([2,3,-4]))
print(max_scs([8,-4,3,-5,4]))
print(max_scs([-3,4,6,-2]))
print(max_scs([-8,7,6]))
print(max_scs([3,-4,5,6,-8,7]))

print("")

# Efficient Soln , modify Kadane's algo to get the min sub subarr, then subtract that from total sum of array, this will
# give the max sum circular arr, now calc the max sum normal subarr, and finally find out the max of these two


def max_scs_circ(arr):
    j=0
    mins=10000
    sum=0
    while j<len(arr):
        sum+=arr[j]
        mins=min(sum,mins)
        if sum>0:
            sum=0
        j+=1
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
    return (sum-mins)

def max_scs_normal(arr):
    j=0
    maxs=-1
    sum=0
    while j<len(arr):
        sum+=arr[j]
        maxs=max(sum,maxs)
        if sum<0:
            sum=0
        j+=1
    return maxs

def max_scs2(arr):
    return max(max_scs_normal(arr),max_scs_circ(arr))

print(max_scs2([5,-2,3,4]))
print(max_scs2([2,3,-4]))
print(max_scs2([8,-4,3,-5,4]))
print(max_scs2([-3,4,6,-2]))
print(max_scs2([-8,7,6]))
print(max_scs2([3,-4,5,6,-8,7]))
print("")
#O(n)+O(n)+O(n)= O(n)



# Easier way of finding minimum sum subarr is to negate all elements first and then find max of the negated arr
# That will give the min of the normal arr , in a negated form , now to get max circular , 
# just add sum and max of negated arr

def max_overall(arr):
    sum=0
    max_normal = max_scs_normal(arr)
    if max_normal<0:
        return max_normal
    for i in range(len(arr)):
        sum+=arr[i]
        arr[i]=(-1*arr[i])

    max_circ = sum + max_scs_normal(arr)
    return max(max_circ,max_normal)


print(max_overall([5,-2,3,4]))
print(max_overall([2,3,-4]))
print(max_overall([8,-4,3,-5,4]))
print(max_overall([-3,4,6,-2]))
print(max_overall([-8,7,6]))
print(max_overall([3,-4,5,6,-8,7]))



