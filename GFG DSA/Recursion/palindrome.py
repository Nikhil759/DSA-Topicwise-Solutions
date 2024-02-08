# Note , the & operator is used here bcoz A & B will always be false if A is false, so if A is false then B is not computed ,
# this means that if str[n-1]==str[0] is False , then the recursive calls will end there itself, no need to go further

def isPalindrome(string):
    n=len(string)
    if n<2:
        return True
    return (string[n-1]==string[0])&(isPalindrome(string[1:n-1]))


print(isPalindrome("aabbaa"))


def isPalindrome2(string,i,j):
    n=len(string)
    if i>=j:
        return True
    return(string[i]==string[j])&(isPalindrome2(string,i+1,j-1))
        


print(isPalindrome2("abbaa",0,4))