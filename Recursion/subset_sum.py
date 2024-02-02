def subset_sum(arr,sum,temp,i):
    if i==len(arr):
        print(temp)
        # print(temp)
        return 
    subset_sum(arr,sum,temp,i+1)
    temp=temp.append(arr[i])
    subset_sum(arr,sum,temp,i+1)

subset_sum([1,2,3],10,[""],0)







