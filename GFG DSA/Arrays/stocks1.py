# Can buy and sell any number if times

def stocks(arr):
    max_profit=0
    total_profit=0
    i=0
    for j in range(1,len(arr)):
        if arr[j]-arr[i]>max_profit:
            max_profit=max(max_profit,arr[j]-arr[i])
        else : 
            total_profit+=max_profit
            max_profit=0
            i=j
    total_profit+=max_profit
    return total_profit

# print(stocks([1,5,3,8,12]))
# print(stocks([30,20,10]))
# print(stocks([10,20,30]))
# print(stocks([1,5,3,1,2,8]))


def stocks2(arr):  
    total_profit=0
    for i in range(1,len(arr)):
        if arr[i]>arr[i-1]:
            total_profit+=arr[i]-arr[i-1]
    return total_profit

print(stocks2([1,5,3,8,12]))
print(stocks2([30,20,10]))
print(stocks2([10,20,30]))
print(stocks2([1,5,3,1,2,8]))


#Check recursive solution as well
    