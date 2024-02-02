def flip(x):
    if x=="1":
        return "0"
    else:
        return "1"

def onesAndTwosComp(x):
    n=len(x)
    ones=""
    twos=""

    for i in range(n):
        ones += flip(x[i])

    flag=0
    for i in range(n-1,-1,-1):
        if flag==1:
            twos=flip(x[i]) + twos
        elif x[i]=="0":
            twos= "0" + twos
        elif x[i]=="1":
            twos= "1"+twos
            flag=1
    
    print(ones)
    print(twos)

onesAndTwosComp("1001100")
