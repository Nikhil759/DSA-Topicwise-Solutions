def natural_no_sum(x):
    if x==1:
        return 1
    return x + natural_no_sum(x-1)

print(natural_no_sum(2))