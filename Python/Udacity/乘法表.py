def print_multiplication_table(n):
    i = 1
    while  i<=n:
        j = 1
        while j<=n:
            print(i, "*", j, "=", i * j)
            j = j + 1
        i = i + 1


print_multiplication_table(2)