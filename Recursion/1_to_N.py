def one_to_N(n):
    if n==0:
        return
    one_to_N(n-1)
    print(n)

one_to_N(15)
    