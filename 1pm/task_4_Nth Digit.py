# Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

def findn(n):
    appnd = ''
    i = 1
    while (len(appnd) <= n):
        appnd += str(i)
        i += 1

    val = int(appnd[n - 1])
    return val

n=11
print(findn(n))