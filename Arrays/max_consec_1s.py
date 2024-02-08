def max_con1s(arr):
    count=0
    maxc=0
    for i in arr:
        if i==1:
            count+=1
        if i!=1:
            maxc=max(maxc,count)
            count=0
    maxc=max(maxc,count)
    return maxc

print(max_con1s([0,1,1,0,1,0]))
print(max_con1s([1,1,1,1]))
print(max_con1s([0,0,0]))
print(max_con1s([1,0,1,1,1,1,0,1,1]))
print(max_con1s([1,1,1,1,0,0,0]))
print(max_con1s([0,0,0,1,1,1]))