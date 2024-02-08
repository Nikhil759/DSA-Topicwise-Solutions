def subsets(string,curr,i):
    #base case
    print("start")
    if i == len(string):
        print (curr)
        return
    
    #exclude 
    subsets(string,curr,i+1)
    print("ex",i)
    #include
    subsets(string,curr+string[i],i+1)
    print("inc",i)

subsets("ab","",0)
