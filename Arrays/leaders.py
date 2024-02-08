def leaders(arr):
    largest_so_far = -1
    for i in range(len(arr)-1,-1,-1):
        if arr[i]>largest_so_far:
            largest_so_far=arr[i]
            print(largest_so_far)

leaders([7,10,4,3,6,5,2])
leaders([10,20,30])
leaders([30,20,10])


#O(n)