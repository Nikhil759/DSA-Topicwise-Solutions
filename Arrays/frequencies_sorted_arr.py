def freq(arr):
    count=1
    for i in range(1,len(arr)):
        if arr[i]==arr[i-1]:
            count+=1
        if arr[i]!=arr[i-1]:
            print("Element : " + str(arr[i-1]))
            print("Frequency : " + str(count))
            count=1
    print("Element : " + str(arr[len(arr)-1]))
    print("Frequency : " + str(count))

freq([10,10,10,25,30,30])
print(" ")
freq([10,20,30])
print(" ")
freq([10])
print(" ")
freq([10,50,50,50])
print(" ")
freq([10,50,50,50,60])