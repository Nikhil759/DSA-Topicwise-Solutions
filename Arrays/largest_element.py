def largest(arr):
    maximum=0
    for i in arr:
        maximum=max(maximum,i)
    return maximum

print(largest([1,2,3,35,22,2323,1]))

#O(n)