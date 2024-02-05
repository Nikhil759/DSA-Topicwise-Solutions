# Naive solution

def largest(arr):
    maximum=0
    for i in arr:
        maximum=max(maximum,i)
    return maximum

def second_largest(arr):
    x=largest(arr)
    max2=-1
    for i in arr:
        if i!=x:
            max2=max(i,max2)
    if max2==-1:
        return -1
    return arr.index(max2)

# print(second_largest([1,2,23,4,5,46,3]))

# print(second_largest([1,1,1,1]))

def second_largest2(arr):
    x=largest(arr)
    max2=-1
    for i in range(len(arr)):
        if arr[i]!=x:
            if max2==-1:
                max2=i
            if arr[i]>arr[max2]:
                max2=i
    if max2==-1:
        return -1
    return max2

# print(second_largest2([1,2,23,4,5,46,3]))

# print(second_largest2([1,1,1,1]))

# O(2n)


def second_largest3(arr):
    second_largest=-1
    largest=0

    for i in range(1,len(arr)):
        if arr[i]>arr[largest]:
            second_largest=largest
            largest = i
        elif arr[i]<arr[largest]:
            if second_largest==-1:
                second_largest=i
            elif arr[i]>arr[second_largest]:
                second_largest=i
    return second_largest
    
print(second_largest3([1,2,23,4,5,46,3]))

print(second_largest3([1,1,1,1]))
    
print(second_largest3([12,7,12,9]))

print(second_largest3([12,12,12,9]))

print(second_largest3([12,10,12,9]))


