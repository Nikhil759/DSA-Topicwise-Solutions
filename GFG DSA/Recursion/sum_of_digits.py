def sum_of_digits(x):
    if x==0:
        return 0
    return x%10 + sum_of_digits(int(x/10))

print(sum_of_digits(10))