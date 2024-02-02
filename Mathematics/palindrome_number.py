def ispalindrome(x):
    rev = 0
    a=x
    while(a>0):
        rev = rev*10 + a%10
        # print(rev)
        a=int(a/10)
        # print(a)
    #print(rev)

    return(rev==x)


print(ispalindrome(167464761)) 

#Time Complexity - O(d) where d is the number of digits in input

    
